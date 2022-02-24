#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Filename: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer/main.py
Path: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer
Created Date: Sunday, January 16th 2022, 4:47:23 pm
Author: Christian Fink

Copyright (c) 2022 Your Company
"""

import sys



from PySide6.QtWidgets import QApplication, QMainWindow, QToolButton, QMenu, QDialog
from PySide6.QtCore import QFile, QObject, Signal, Slot, QTimer, QAbstractTableModel, Qt, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QBrush, QColor, QAction, QIcon
from ui_mainwindow import Ui_MainWindow
from dialog_reftemp import Ui_dlg_referenz
import datetime

from UliEngineering.Physics import RTD
import pandas as pd
import pyqtgraph as pg
import random
import time

from dummyDevices import DummyMeter, DummyTempMeter
from kaye import Kaye
from definitions import MeasureType
# import asyncio
# from pathlib import Path

class DateAxisItem(pg.AxisItem):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def tickValues(self, minVal, max_val, size):
        pass

class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Zeit', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [
            datetime.datetime.fromtimestamp(value).strftime("%H:%M:%S")
            for value in values
        ]

class StatisticModel(QAbstractTableModel):

    show_hide_graph = Signal(int, bool)

    def __init__(self, parent, definition):
        QAbstractTableModel.__init__(self, parent)
        self.nr_channels = definition.get('channels', 1)
        self.hor_headers = definition.get('channel_names')
        self.ch_types = definition.get('channel_types')
        self.colors = definition.get('colors')
        self.vert_headers = [
            'Max',
            'Min',
            'Mittel',
            'Diff',
            'StAbw',
            'Stabil',
            'Auswahl'
        ]
        # return {
        #     'channels': self.__channels,
        #     'channel_types': [MeasureType.TEMP for x in range(self.__channels)],
        #     'channel_names': [f"M{x:02d}" for x in range(self.__channels)]
        # }
        

        self.__data = []
        self.check_states = []
        for i in range(self.nr_channels):
            self.__data.append((0, 0, 0, 0, 0, False))
            self.check_states.append(Qt.Checked)

    def update(self, statistic):
        self.__data = statistic
        self.layoutChanged.emit()

    def rowCount(self, parent):
        return len(self.vert_headers)

    def columnCount(self, parent):
        return len(self.hor_headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        
        c = index.column()
        if role == Qt.CheckStateRole:
            if index.row() == 6:
                return self.check_states[c]
            return None
        if index.row() > 5:
            return None
        if role == Qt.DisplayRole:
            if index.row() == 5:
                if self.__data[c][5]:
                    return "STABIL"
                else:
                    return "---"
            else:
                if self.ch_types[c] == MeasureType.PT100:
                    return f"{self.__data[c][index.row()]:5.4f} Ω"
                if self.ch_types[c] == MeasureType.PT1000:
                    return f"{self.__data[c][index.row()]:5.4f} Ω"
                else:
                    return f"{self.__data[c][index.row()]:5.4f} °C"
        if role == Qt.TextAlignmentRole:
            if index.row() < 5:
                return int(Qt.AlignRight | Qt.AlignVCenter)
            else:
                return int(Qt.AlignHCenter | Qt.AlignVCenter)

        if role == Qt.BackgroundRole:
            if index.row() == 5:
                if self.__data[c][5]:
                    return QBrush(QColor(0, 255 , 0, 50))
                else:
                    return QBrush(QColor(255, 0 , 0, 50))

        return None
    
    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role == Qt.CheckStateRole:
            c = index.column()
            self.check_states[c] = value
            self.show_hide_graph.emit(c, value == 2)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return None
        if index.row() == 6:
            return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable
        return Qt.ItemIsSelectable

    def headerData(self, col, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self.hor_headers[col])
            elif orientation == Qt.Vertical:
                return str(self.vert_headers[col])
            else:
                return None
        if role == Qt.CheckStateRole:
            return self.check_states[c]
        if role == Qt.BackgroundRole:
            if orientation == Qt.Horizontal:
                return self.colors[col].qbrush

        if role == Qt.ForegroundRole:
            if orientation == Qt.Horizontal:
                # return self.colors[col].qbrush_inverted
                return QBrush(QColor(*self.colors[col].text_color))
                # return self.colors[col].text_color
        else:
            return None



    # @property
    # def selection_channels(self):
    #     print(self.__data)
    #     return [
    #         d[5] for d in self.__data
    #     ]

class Colors:

    # color_palette = [
    #     (228,26,28),
    #     (55,126,184),
    #     (77,175,74),
    #     (152,78,163),
    #     (255,127,0),
    #     (255,255,51),
    #     (166,86,40),
    #     (247,129,191),
    #     (153,153,153)
    # ]
    color_palette = [
        (0, 255, 255),
        (0, 0, 255),
        (165, 42, 42),
        (127, 255, 0),
        (210, 105, 30),
        (220, 20, 60),
        (0, 0, 139),
        (153, 50, 204),
        (255, 20, 147),
        ( 34, 139, 34),
        (255, 192, 203),
        (124, 252, 0)
    ]

    def __init__(self, nr):
        self.nr = nr

    @property
    def rgb_color(self):
        if self.nr <= (len(self.color_palette)-1):
            return self.color_palette[self.nr]
        return (255, 255, 255)
    
    @property
    def rgb_color_inverted(self):
        if self.nr <= (len(self.color_palette)-1):
            r, g, b = self.color_palette[self.nr]
            return (255-r, 255-g, 255-b)
        return (0, 0, 0)

    def rgba_color_inverted(self, alpha=50):
        if self.nr <= (len(self.color_palette)-1):
            r, g, b = self.color_palette[self.nr]
            return (255-r, 255-g, 255-b, alpha)
        return (0, 0, 0, alpha)


    def rgba_color(self, alpha=50):
        if self.nr <= (len(self.color_palette)-1):
            d = list(self.color_palette[self.nr])
            d.append(alpha)
            return d
        return (255, 255, 255, alpha)

    @property
    def text_color(self):
        # if self.nr <= (len(self.color_palette)-1):
        #     r, g, b = self.color_palette[self.nr]
        #     return (255-r, 255-g, 255-b)
        # return (255, 255, 255)
        return (0, 0, 0)


    @property
    def pen(self):
        return pg.mkPen(color=self.rgb_color)

    @property
    def qbrush(self):
        return QBrush(QColor(*self.rgba_color(100)))

    @property
    def qbrush_inverted(self):
        return QBrush(QColor(*self.rgba_color_inverted(100)))

class IntervalToolButton(QToolButton):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPopupMode(QToolButton.MenuButtonPopup)
        self.triggered.connect(self.setDefaultAction)


    # def setDefaultAction(self):
    #     print("ACTION")
    #     super().setDefaultAction()

class MainWindow(QMainWindow):
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.plot_data = []
        self.update_data = {}
        self.time_delta = 1.5 * 60


        self.selection_record_type = None

        self.ui.graphicsView.setAxisItems(
            {'bottom': TimeAxisItem(orientation='bottom')}
        )       

        self.ui.graphicsView.setMouseEnabled(x=True, y=False)
        self.ui.graphicsView.setAutoVisible(x=False, y=True)

        self.ui.action_1_min.triggered.connect(self.select_interval)
        self.ui.action_5_min.triggered.connect(self.select_interval)
        self.ui.action_10_min.triggered.connect(self.select_interval)
        self.ui.action_20_min.triggered.connect(self.select_interval)
        self.ui.action_30_min.triggered.connect(self.select_interval)
        self.ui.action_40_min.triggered.connect(self.select_interval)
        self.ui.action_show_hide_big_values.triggered.connect(self.show_hide_big_values)

        #self.ui.action_dummy_widerstand.triggered.connect(self.new_instrument_widerstand)
        #self.ui.action_dummy_mehrkanal.triggered.connect(self.new_instrument_mehrkanal)

        self.ui.action_kaye_sonde.triggered.connect(self.new_kaye)

        self.dropDown_menu_interval = QMenu(self)
        self.dropDown_menu_interval.addAction(self.ui.action_1_min)
        self.dropDown_menu_interval.addAction(self.ui.action_5_min)
        self.dropDown_menu_interval.addAction(self.ui.action_10_min)
        self.dropDown_menu_interval.addAction(self.ui.action_20_min)
        self.dropDown_menu_interval.addAction(self.ui.action_30_min)
        self.dropDown_menu_interval.addAction(self.ui.action_40_min)

        #self.dropDown_menu_interval.setCurrentIndex(2)

        self.interval_button = IntervalToolButton()
        self.interval_button.setMenu(self.dropDown_menu_interval)
        self.ui.toolBar.addWidget(self.interval_button)
            

        self.ui.action_quit.triggered.connect(self.__quit)
        self.ui.action_save_values.triggered.connect(self.save_values)
        # self.m.start()

    def __del__(self):
        self.m.stop()

    def __add_pt100(self):
        self.show_hide_big_values(True)
        self.data = pd.DataFrame(
            {0: [], 1:[]},
            index=[]
        )
        self.definition = self.m.channel_def
        self.definition['channel_types'].append(MeasureType.TEMP)
        self.definition['channel_names'].append("Temperatur")
        self.definition['colors'] = [Colors(0), Colors(1)]

        self.stat_model = StatisticModel(self, self.definition)
        self.ui.table_statistic.setModel(self.stat_model)

        self.stat_model.show_hide_graph.connect(self.show_hide_graph)
        # return {
        #     'channels': 1,
        #     'channel_types': [MeasureType.PT100],
        #     'channel_names': ['Widerstand']
        # }
        
        self.ui.graphicsView.showAxis('left')
        self.ui.graphicsView.showAxis('right')
        
        self.ui.graphicsView.setLabel('left', "Widerstand", units="<font>&Omega;</font>")
        self.ui.graphicsView.setLabel('right', "Temperatur", units="<font>°C</font>")

        self.view_boxes = [
            pg.ViewBox(),
            pg.ViewBox()
        ]

        self.ui.graphicsView.scene().addItem(self.view_boxes[0])
        self.ui.graphicsView.scene().addItem(self.view_boxes[1])

        self.ui.graphicsView.getAxis('left').linkToView(self.view_boxes[0])
        self.ui.graphicsView.getAxis('right').linkToView(self.view_boxes[1])

        
        # self.view_boxes[0].setXLink(self.view_boxes[1])
        # self.ui.graphicsView.setXLink(self.view_boxes[0])
        # self.ui.graphicsView.setXLink(self.view_boxes[1])
        self.view_boxes[0].setXLink(self.ui.graphicsView)
        self.view_boxes[1].setXLink(self.ui.graphicsView)

        self.curves = [
            pg.PlotCurveItem(x=[], y=[],
                pen=self.definition['colors'][0].pen
            ),
            pg.PlotCurveItem(x=[], y=[],
                pen=self.definition['colors'][1].pen
            )
        ]
        self.view_boxes[0].addItem(self.curves[0])
        self.view_boxes[1].addItem(self.curves[1])

        self.view_boxes[0].enableAutoRange(axis=pg.ViewBox.YAxis)
        self.view_boxes[1].enableAutoRange(axis=pg.ViewBox.YAxis)
        
        # self.ui.graphicsView.enableAutoRange(axis=pg.ViewBox.XAxis)

        self.ui.graphicsView.setXRange(
            self.pd_time(),
            self.pd_time()+10,
            update=True
        )
        # self.ui.graphicsView.enableAutoRange(axis=pg.ViewBox.XAxis)
        
        # self.view_boxes[0].enableAutoRange(axis=pg.ViewBox.XAxis)
        # self.view_boxes[0].enableAutoRange(axis=pg.ViewBox.XAxis)
        # self.view_boxes[1].enableAutoRange(axis=pg.ViewBox.XAxis)

        self.updateViews()
        
        self.ui.graphicsView.getViewBox().sigResized.connect(self.updateViews)
        self.ui.graphicsView.getViewBox().sigXRangeChanged.connect(self.update_statistic)

        self.ui.graphicsView.getViewBox().sigRangeChangedManually.connect(self.manualy_changed)

    def __quit(self):
        self.app.exit(0)

    @property
    def data(self):
        return self.m.data

    @Slot()
    def config_ready(self):
        print("Konfiguration bereit")
        self.show_hide_big_values(True)
        self.definition = self.m.channel_def

        channels = self.definition.get('channels', 1)
        self.definition['colors'] = [Colors(i) for i in range(channels)]

        # self.data = pd.DataFrame(
        #     {e: [] for e in range(channels)},
        #     index=[]
        # )

        self.stat_model = StatisticModel(self, self.definition)
        self.ui.table_statistic.setModel(self.stat_model)

        self.stat_model.show_hide_graph.connect(self.show_hide_graph)
        # return {
        #     'channels': 1,
        #     'channel_types': [MeasureType.PT100],
        #     'channel_names': ['Widerstand']
        # }
        
        self.ui.graphicsView.showAxis('left')
        self.ui.graphicsView.showAxis('right')
        
        self.ui.graphicsView.setLabel('left', "Widerstand", units="<font>&Omega;</font>")
        self.ui.graphicsView.setLabel('right', "Temperatur", units="<font>°C</font>")


        self.view_boxes = [pg.ViewBox() for i in range(channels)]
        self.curves = []
        
        for e, ch_type in enumerate(self.definition.get('channel_types', [])):
            self.ui.graphicsView.scene().addItem(self.view_boxes[e])
            if ch_type == MeasureType.PT100:
                self.ui.graphicsView.getAxis('left').linkToView(self.view_boxes[e])
            elif ch_type == MeasureType.TEMP:
                self.ui.graphicsView.getAxis('right').linkToView(self.view_boxes[e])
            # self.ui.graphicsView.scene().addItem(self.view_boxes[1])
            self.view_boxes[e].setXLink(self.ui.graphicsView)
            self.curves.append(
                pg.PlotCurveItem(x=[], y=[],
                    pen=self.definition['colors'][e].pen
                ),
            )
            self.view_boxes[e].addItem(self.curves[e])
            self.view_boxes[e].enableAutoRange(axis=pg.ViewBox.YAxis)
        
        # self.view_boxes[0].setXLink(self.view_boxes[1])
        # self.ui.graphicsView.setXLink(self.view_boxes[0])
        # self.ui.graphicsView.setXLink(self.view_boxes[1])
        # self.view_boxes[1].setXLink(self.ui.graphicsView)

        # self.curves = [
        #     pg.PlotCurveItem(x=[], y=[],
        #         pen=self.definition['colors'][1].pen
        #     )
        # ]
        # self.view_boxes[1].addItem(self.curves[1])

        #self.view_boxes[1].enableAutoRange(axis=pg.ViewBox.YAxis)
        
        # self.ui.graphicsView.enableAutoRange(axis=pg.ViewBox.XAxis)

        self.ui.graphicsView.setXRange(
            self.pd_time(),
            self.pd_time()+10,
            update=True
        )
        # self.ui.graphicsView.enableAutoRange(axis=pg.ViewBox.XAxis)
        
        # self.view_boxes[0].enableAutoRange(axis=pg.ViewBox.XAxis)
        # self.view_boxes[0].enableAutoRange(axis=pg.ViewBox.XAxis)
        # self.view_boxes[1].enableAutoRange(axis=pg.ViewBox.XAxis)

        self.updateViews()
        
        self.ui.graphicsView.getViewBox().sigResized.connect(self.updateViews)
        self.ui.graphicsView.getViewBox().sigXRangeChanged.connect(self.update_statistic)

        self.ui.graphicsView.getViewBox().sigRangeChangedManually.connect(self.manualy_changed)

        
        self.m.start()
        #config_ready

    @Slot()
    def config_ready_mehrkanal(self):
        self.__add_temp_channels(self.m.channel_def)
        self.m.start()

    @Slot()
    def config_ready_widerstand(self):
        print("Messgerät mit PT100 bereit")
        self.__add_pt100()
        self.m.start()

    def new_instrument_widerstand(self):
        self.m = DummyMeter(self)
        self.m.new_value.connect(self.callback_pt100)
        self.m.config_ready.connect(self.config_ready_widerstand)

        self.m.config_closed()
        
    def new_instrument_mehrkanal(self):
        self.m = DummyTempMeter(self)
        self.m.new_value.connect(self.callback_temp)
        self.m.config_ready.connect(self.config_ready_mehrkanal)
        
    def new_kaye(self):
        self.m = Kaye(self)
        self.m.new_value.connect(self.callback_values)
        self.m.config_ready.connect(self.config_ready)
        #self.m.

    def save_values(self):
        dialog = QDialog()
        dialog.ui = Ui_dlg_referenz()
        dialog.ui.setupUi(dialog)
        if self.selection_record_type is None:
            dialog.ui.group_type.maximumHeight = 92
        else:
            dialog.ui.group_type.maximumHeight = 0
        # dialog.setAttribute(Qt.WA_DeleteOnClose)
        dialog.exec()

        try:
            wert = float(dialog.ui.edit_ref_temp.text())
        except:
            print("kein Wert übergeben! Nicht gespeichert!")
            return
        
        print(f"Eingegebene Referenz: {wert}")
        print(f"TYP : {self.selection_record_type}")
        if self.selection_record_type is None:
            print(f"AUSWAHL : {dialog.ui.radio_act.isChecked()}")
            print(f"AUSWAHL : {dialog.ui.radio_stat.isChecked()}")
            if dialog.ui.radio_act.isChecked():
                self.selection_record_type = 1
            elif dialog.ui.radio_stat.isChecked():
                self.selection_record_type = 2
        if self.selection_record_type == 1:
            # Nur Aktueller Wert
            print("Nur aktuelle Werte")
            self.m.save_values(
                wert,
                self.selection_record_type,
                self.data.index[-1],
                self.data.iloc[-1]
            )

        if self.selection_record_type == 2:
            self.m.save_values(wert)

    @Slot(object)
    def manualy_changed(self, obj):
        self.ui.action_follow.setChecked(False)
        data_selection = self.update_statistic()
        #(xmin, xmax), (ymin, ymax) = self.view_boxes[0].viewRange()
        self.time_delta = data_selection.index[-1] - data_selection.index[0]
        #self.time_delta = xmax - xmin
        #self.x_auto_range = False
        # self.ui.graphicsView.getViewBox().enableAutoRange(axis=pg.ViewBox.XAxis, enable=False)

    def __add_temp_channels(self, channels):
        self.show_hide_big_values(False)
        self.definition = channels
        nr_channels = channels['channels']
        print(f"Messgerät mit {nr_channels} Kanälen")

        self.data = pd.DataFrame(
            {x: [] for x in range(nr_channels)}, index=[])

        self.definition['colors'] = [
            Colors(e) for e in range(nr_channels)
        ]

        self.stat_model = StatisticModel(self, self.definition)
        self.ui.table_statistic.setModel(self.stat_model)
        self.stat_model.show_hide_graph.connect(self.show_hide_graph)

        self.ui.graphicsView.showAxis('left')
        self.ui.graphicsView.setLabel('left', "Temperatur", units="<font>°C</font>")

        self.view_boxes = [
            pg.ViewBox() for x in range(nr_channels)
        ]

        self.curves = [
            pg.PlotCurveItem(
                x=[],
                y=[],
                pen=self.definition['colors'][e].pen)
            for e in range(nr_channels)
        ]

        print(f"Es sind {len(self.curves)} Kurven")

        for e, vb in enumerate(self.view_boxes):
            self.ui.graphicsView.scene().addItem(vb)
            vb.setXLink(self.ui.graphicsView)
            vb.setYLink(self.ui.graphicsView)
            # self.ui.graphicsView.getAxis('left').linkToView(vb)
            # vb.linkToView(self.ui.graphicsView)
            # self.ui.graphicsView.getAxis('left').linkToView(vb)

            vb.addItem(self.curves[e])
            # vb.enableAutoRange(axis=pg.ViewBox.YAxis)
            # self.
            # self.plot_data.append(self.ui.graphicsView.plot(pen=pg.mkPen(color=(255, 255, 0))))
            # self.plot_data.append(self.ui.graphicsView.plot(pen=pg.mkPen(pg.intColor(e))))
            # self.plot_data.append(
            #     self.ui.graphicsView.plot(pen=self.definition['colors'][e].pen)
            # )
            
            #self.ui.graphicsView.scene().addItem(vb)
            # vb.setXLink(self.ui.graphicsView)
            # vb.addItem(self.plot_data[e])
            #self.view_boxes[0].addItem(self.plot_data[-1])

        self.ui.graphicsView.setXRange(
            self.pd_time(),
            self.pd_time()+10,
            update=True
        )


        self.updateViews()
        self.ui.graphicsView.getViewBox().sigResized.connect(self.updateViews)
        self.ui.graphicsView.getViewBox().sigXRangeChanged.connect(self.update_statistic)
        self.ui.graphicsView.getViewBox().sigRangeChangedManually.connect(self.manualy_changed)

    def update_statistic(self):
        (xmin, xmax), (ymin, ymax) = self.view_boxes[0].viewRange()
        mask = (self.data.index >= xmin) & (self.data.index <= xmax)
        data = self.data.loc[mask]
        _diff = data.index[-1] - data.index[0]
        _h, _sek = divmod(_diff, 3600)
        _m, _sek = divmod(_sek, 60)

        statistic = [
            (
                data[k].min(),
                data[k].max(),
                data[k].mean(),
                abs(data[k].max() - data[k].min()),
                data[k].std(),
                data[k].std() < 0.3
            ) for k in data.keys()
        ]
        self.stat_model.update(statistic)
        # max_values = [data[k].max() for k in data.keys()]

        # temp_min = data['temp'].min()
        # temp_max = data['temp'].max()
        # temp_mean = data['temp'].mean()

        # res_min = data['res'].min()
        # res_max = data['res'].max()
        # res_mean = data['res'].mean()
        #         return {
        #     'channels': 1,
        #     'channel_types': [MeasureType.PT100]
        # }
        self.ui.text_stat_res_time.setText(f"{int(_h):02d}:{int(_m):02d}:{int(_sek):02d}")
        self.ui.text_stat_temp_time.setText(f"{int(_h):02d}:{int(_m):02d}:{int(_sek):02d}")
        self.ui.text_stat_res_time_2.setText(f"{int(_h):02d}:{int(_m):02d}:{int(_sek):02d}")
        
        ch_def = self.m.channel_def

        if ch_def['channels'] == 1:
            if (ch_def['channel_types'][0] == MeasureType.PT100) or (ch_def['channel_types'][0] == MeasureType.PT1000):
                self.ui.text_stat_res_min.setText(f"{statistic[0][0]:5.4f} Ω")
                self.ui.text_stat_temp_min.setText(f"{statistic[1][0]:5.4f} °C")

                self.ui.text_stat_res_max.setText(f"{statistic[0][1]:5.4f} Ω")
                self.ui.text_stat_temp_max.setText(f"{statistic[1][1]:5.4f} °C")

                self.ui.text_stat_res_mean.setText(f"{statistic[0][2]:5.4f} Ω")
                self.ui.text_stat_temp_mean.setText(f"{statistic[1][2]:5.4f} °C")

                self.ui.text_stat_res_diff.setText(f"{statistic[0][3]:5.4f} Ω")
                self.ui.text_stat_temp_diff.setText(f"{statistic[1][3]:5.4f} °C")
            
                self.ui.text_stat_res_std.setText(f"{statistic[0][4]:5.4f} Ω")
                self.ui.text_stat_temp_std.setText(f"{statistic[1][4]:5.4f} °C")

                self.ui.lbl_res_mean.setText(f"R: {statistic[0][2]:5.4f} Ω")
                self.ui.lbl_temp_mean.setText(f"t: {statistic[1][2]:5.4f} °C")

            else:
                self.ui.text_stat_temp_min.setText(f"{statistic[0][0]:5.4f} °C")
                self.ui.text_stat_temp_max.setText(f"{statistic[0][1]:5.4f} °C")
                self.ui.text_stat_temp_mean.setText(f"{statistic[0][2]:5.4f} °C")
                self.ui.text_stat_temp_diff.setText(f"{statistic[0][3]:5.4f} °C")
                self.ui.text_stat_temp_std.setText(f"{statistic[0][4]:5.4f} °C")
                self.ui.lbl_temp_mean.setText(f"t: {statistic[0][2]:5.4f} °C")

        elif len(self.m.data.columns) == 2:
            self.ui.lbl_res_mean.setText(f"R: {statistic[0][2]:5.4f} Ω")
            self.ui.lbl_temp_mean.setText(f"t: {statistic[1][2]:5.4f} °C")

        
        return data

    @Slot(int, bool)
    def show_hide_graph(self, graph_nr, state):
        if state:
            self.curves[graph_nr].show()
            #self.view_boxes[graph_nr].addItem(self.curves[graph_nr])
        else:
            self.curves[graph_nr].hide()
            # self.view_boxes[graph_nr].removeItem(self.curves[graph_nr])

    @Slot(int, float)
    def callback_pt100(self, channel_nr, value):
        temp = RTD.pt100_temperature(value)
        df = pd.DataFrame(
            {
                0: value,
                1: temp
            },
            index=[self.pd_time()]
        )
        
        self.ui.lbl_temp_act.setText(f"t: {temp:5.4f} °C")
        self.ui.lbl_res_act.setText(f"R: {value:5.4f} Ω")
        self.add_value(df)

    @Slot(int, float)
    def callback_temp(self, channel_nr, value):
        if channel_nr in self.update_data:            
            df = pd.DataFrame(
                self.update_data,
                index=[self.pd_time()]
            )
            self.data = self.data.append(df)

            for e, curve in enumerate(self.curves):
                curve.setData(
                    x=list(self.data.index),
                    y=list(self.data[e])                    
                )
            self.update_data = {}
            self.update_graph()

            # seconds = None
            # if self.ui.radio_stab_temp.isChecked():
            #     t = self.ui.time_edit_stab.time()
            #     seconds = t.hour() * 3600 + t.minute() * 60 + t.second()
            #     selection = self.data_selection(seconds)
            # else:
            #     selection = self.data

            # if seconds is not None:
            #     print(f"ANZAHL SEKUNDEN : {seconds}")
            #     if self.data.index[0] > (self.pd_time() - seconds):
            #         self.ui.graphicsView.setXRange(self.data.index[0], self.pd_time(), update=False)

            #         self.view_boxes[0].setYRange(res_min, res_max)
            #         self.view_boxes[1].setYRange(temp_min, temp_max)
            #     else:
            #         self.ui.graphicsView.setXRange(self.pd_time() - seconds, self.pd_time(), update=False)

            #         self.view_boxes[0].setYRange(res_min, res_max)
            #         self.view_boxes[1].setYRange(temp_min, temp_max)



        self.update_data[channel_nr] = value

    @Slot(int, float)
    def callback_values(self, channel_nr, value):
        # if channel_nr in self.update_data:         
        #     df = pd.DataFrame(
        #         self.update_data,
        #         index=[self.pd_time()]
        #     )
        #     self.data = self.data.append(df)
        cols = list(self.m.data.columns)
        for e, curve in enumerate(self.curves):
            curve.setData(
                x=list(self.m.data.index),
                y=list(self.m.data[cols[e]])                    
            )
        self.update_data = {}
        self.update_graph()
        if len(cols) == 2:
            # Nur eine Sonde vorhanden
            res_value = self.m.data.iloc[-1][cols[0]]
            temp_value = self.m.data.iloc[-1][cols[1]]
            self.show_hide_big_values(show=True)
            self.ui.lbl_res_act.setText(f"R: {res_value:5.4f} Ω")
            self.ui.lbl_temp_act.setText(f"t: {temp_value:5.4f} °C")

        else:
            self.show_hide_big_values(show=False)
        
        #self.update_data[channel_nr] = value
        
        # if self.definition['channel_types'][channel_nr] == MeasureType.TEMP:
        # elif self.definition['channel_types'][channel_nr] == MeasureType.PT100:

    def select_interval(self):
        button = self.sender()
        minuten = int(button.objectName().split("_")[1])
        self.time_delta = minuten * 60

    def show_hide_big_values(self, show=None):
        height = self.ui.frame_big_values.height()
        if show is None:
            if height == 0:
                new_height = 84
            else:
                new_height = 0
        elif show:
            new_height = 84
        else:
            new_height = 0
        self.animation = QPropertyAnimation(self.ui.frame_big_values, b"maximumHeight")
        self.animation.setDuration(500)
        self.animation.setStartValue(height)
        self.animation.setEndValue(new_height)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        # if self.ui.action_show_hide_big_values.isChecked():

        #     self.ui.frame_big_values

    def data_selection(self, seconds=None):
        if seconds is None or seconds <= 0:
            return self.m.data        
        _now = self.pd_time()
        mask = (self.m.data.index > (_now - seconds)) & (self.m.data.index <= _now)
        return self.m.data.loc[mask]

    def add_value(self, df):
        self.data = dp.combine([self.data, df])
        # self.data = self.data.append(df)

        for e, curve in enumerate(self.curves):
            curve.setData(x=list(self.data.index), y=list(self.data[e]))
        self.update_graph()

    def updateViews(self):
        # print(self.ui.graphicsView.getViewBox())
        for vb in self.view_boxes:
            #print(vb.getState())
            vb.setGeometry(
                self.ui.graphicsView.getViewBox().sceneBoundingRect())
            # vb.linkedViewChanged(
            #     self.ui.graphicsView.getViewBox(),
            #     vb.XAxis
            # )

    def update_graph(self):
        seconds = None
        if self.ui.radio_stab_temp.isChecked():
            t = self.ui.time_edit_stab.time()
            seconds = t.hour() * 3600 + t.minute() * 60 + t.second()
            selection = self.data_selection(seconds)
        else:
            selection = self.data
        # self.ui.dblSpinBox_stab_temp
        data_selection = self.update_statistic()

        # agg = data_selection.agg(['min', 'max'])

        _min = []
        _max = []
        cols = list(self.m.data.columns)
        for e, s in enumerate(self.stat_model.check_states):
            if not s:
                continue
            
            mi, mx = data_selection[cols[e]].agg(['min', 'max'])
            _min.append(mi)
            _max.append(mx)
            
        self.ui.graphicsView.setYRange(
            min(_min),
            max(_max),
            update=True
        )

        if self.ui.action_follow.isChecked():
            __delta = data_selection.index[-1] - data_selection.index[0]

            if __delta < self.time_delta:
                self.ui.graphicsView.setXRange(
                    self.data.index[0], self.pd_time(), update=True)
            else:
                self.ui.graphicsView.setXRange(
                    self.pd_time() - self.time_delta, self.pd_time(), update=True)

        return

        if seconds is not None:
            print(f"===== SECONDS {seconds}")
            if self.data.index[0] > (self.pd_time() - seconds):
                self.ui.graphicsView.setXRange(self.data.index[0], self.pd_time(), update=False)

                self.view_boxes[0].setYRange(res_min, res_max)
                self.view_boxes[1].setYRange(temp_min, temp_max)
            else:
                self.ui.graphicsView.setXRange(self.pd_time() - seconds, self.pd_time(), update=False)

                self.view_boxes[0].setYRange(res_min, res_max)
                self.view_boxes[1].setYRange(temp_min, temp_max)

    def pd_time(self):
        return int(time.mktime(datetime.datetime.now().timetuple()))    

if __name__ == "__main__":
    # a = time.time()
    # a = datetime.datetime.now()
    # print(a)
    # b = pd.to_datetime(int(a.), unit='s')

    # print(b)

    # a = datetime.datetime.fromtimestamp(time.time())
    # print(a)
    # print(time.time())
    # print(datetime.datetime.timestamp(a))

    # exit()

    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.show()

    sys.exit(app.exec())
