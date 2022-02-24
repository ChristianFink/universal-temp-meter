#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Filename: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer/kaye/__init__.py
Path: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer/kaye
Created Date: Sunday, February 13th 2022, 10:54:36 am
Author: Christian Fink

Copyright (c) 2022 Your Company
"""

import sys
import time
from PySide6.QtCore import QObject, Signal, Slot, QTimer, QPropertyAnimation, QEasingCurve, QRunnable, QThreadPool
from PySide6.QtWidgets import QWidget, QApplication

from kaye.kaye_ui import Ui_Form
from definitions import MeasureType
import serial
import serial.tools.list_ports
import time
import pandas as pd
import datetime
import json
# import asyncio
from pathlib import Path


class DataReceiveSignals(QObject):
    finished = Signal()
    #new_value = Signal(int, float)
    new_value = Signal(QObject, float, float)

class DataReceive(QRunnable):

    def __init__(self, ser, sonden):
        super().__init__()
        self.signals = DataReceiveSignals()
        self.sonden = sonden
        self.abort = False
        self.ser = ser
        
    def abbruch(self):
        self.abort = True
        print("Thread stoppen")

    @Slot()
    def run(self):
        print("Thread starten")
        time.sleep(1)

        while not self.abort:
            e = 0
            for id, details in self.sonden.items():
                print(details)
                #print(f"Abfrage von Sonde {id} [{e}]")
                res = None
                if (msg := self.send_command(id, "VO", length=12)):
                    cmd, str_res = self.decode_message(msg)
                    if cmd == "VO":
                        try:
                            res = float(str_res)
                            # self.signals.new_value.emit(details, 0, res)
                            #self.signals.new_value.emit(e * 2, res)
                        except ValueError:
                            pass
                temp = None
                if (msg := self.send_command(id, "VC", length=12)):
                    cmd, str_temp = self.decode_message(msg)
                    if cmd == "VC":
                        temp = float(str_temp)
                        # self.signals.new_value.emit(e * 2 + 1, temp)
                # self.__read_channel += 1
                # if self.__read_channel >= (2 * len(self.sonden)):
                #     self.__read_channel = 0
                if res and temp:
                    self.signals.new_value.emit(details, res, temp)
                e += 1
                time.sleep(1)

    def decode_message(self, msg):
        sp = msg.split("=")
        cmd = sp[0].strip()
        data = sp[1].strip()
        return cmd, data

    def send_command(self, id, command, length=16):
        self.ser.write(f"#{id:02d}{command}\r".encode('utf-8'))
        if (a := self.ser.read(length)) != b"":
            return a.decode('utf-8')
        return None

class SearchKayeSignals(QObject):
    new_kaye = Signal(int, dict)
    search_progress = Signal(int)
    finished = Signal()

class SearchKaye(QRunnable):

    def __init__(self, ser, max_index):
        super().__init__()
        self.signals = SearchKayeSignals()
        self.ser = ser
        self.max_index = max_index

    def decode_message(self, msg):
        sp = msg.split("=")
        cmd = sp[0].strip()
        data = sp[1].strip()
        return cmd, data

    def send_command(self, id, command, length=16):
        self.ser.write(f"#{id:02d}{command}\r".encode('utf-8'))
        if (a := self.ser.read(length)) != b"":
            return a.decode('utf-8')
        return None

    @Slot()
    def run(self):
        for i in range(1, self.max_index):
            self.signals.search_progress.emit(i)
            
            c = f"#{i:02d}AD\r"
            self.ser.write(c.encode('utf-8'))
            a = self.ser.read(16)
            print(a)
            if a == b'':
                continue

            cmd, data = self.decode_message(a.decode('utf-8'))
            sonde_details = {}
            
            cmds = [
                ('ID', str),
                ('LB', str),
                ('UL', str),
                ('CL', str),
                ('TS', str),
                ('R0', float),  # ro
                ('AL', float),  # alpha
                ('DE', float),  # delta
                ('A4', float),  # a4
                ('C4', float)   # c4
            ]
            for cmd, fnc in cmds:
                if (msg := self.send_command(i, cmd)) is None:
                    continue
                cmd, data = self.decode_message(msg)
                sonde_details[cmd] = data
            self.signals.new_kaye.emit(i, sonde_details)
        self.signals.finished.emit()

class KayeSonde(QObject):

    existing_data_found = Signal(bool)

    def __init__(self, kaye, details):
        super().__init__()
        self.kaye = kaye
        self.id = details.get('ID')
        self.label = details.get('LB')
        self.user_label = details.get('UL')
        self.calibration = details.get('CL')
        self.temp_system = details.get('TS')
        self.r0 = details.get('R0')
        self.alpha = details.get('AL')
        self.delta = details.get('DE')
        self.a4 = details.get('A4')
        self.c4 = details.get('C4')
        self.record_values = pd.DataFrame()
        self.values = []
        self.data = pd.DataFrame()
        self.columns = [f"{self.id} R", f"{self.id} T"]
        self.channel_types = [MeasureType.PT100, MeasureType.TEMP]

        if self.filename.is_file():
            print("Existierende Daten gefunden")
            with self.filename.open("r") as fd:
                j = json.load(fd)
                identisch = self.compare_settings(j)
                self.existing_data_found.emit(
                    identisch
                )
                if identisch:
                    self.values = j['values']
        else:
            with self.filename.open("w") as fd:
                json.dump({
                    'settings': self.dict_settings,
                    'values': self.values
                }, fd)

    @property
    def filename(self):
        return Path(__file__).parent.joinpath(self.id)
        #return Path(__file__).parent.joinpath(f'{self.id} {self.kaye.str_start_time}.xlsx')

    @property    
    def dict_settings(self):
        return {
            'ID': self.id,
            'Label': self.label,
            'User Label': self.user_label,
            'Kalibrierung': self.calibration,
            'Temperatur System': self.temp_system,
            'R0': self.r0,
            'Alpha': self.alpha,
            'Delta': self.delta,
            'A4': self.a4,
            'C4': self.c4
        }

    def compare_settings(self, loaded_settings):
        l = [('ID', 'id'),
            ('Label', 'label'),
            ('User Label', 'user_label'),
            ('Kalibrierung', 'calibration'),
            ('Temperatur System', 'temp_system'),
            ('R0', 'r0'),
            ('Alpha', 'alpha'),
            ('Delta', 'delta'),
            ('A4', 'a4'),
            ('C4', 'c4')]
        return all([
            loaded_settings['settings'][k_l] == getattr(self, k_n) for k_l, k_n in l
        ])

    @property
    def df_settings(self):

        d = {
            'Bezeichnung': [
                'ID',
                'Label',
                'User Label',
                'Kalibrierung',
                'Temperatur System',
                'R0',
                'Alpha',
                'Delta',
                'A4',
                'C4'
            ],
            'Wert': [
                self.id,
                self.label,
                self.user_label,
                self.calibration,
                self.temp_system,
                self.r0,
                self.alpha,
                self.delta,
                self.a4,
                self.c4
            ]
        }
        return pd.DataFrame.from_dict(d)

    def add_act_values(self, ref):
        temp = self.data.iloc[-1][self.columns[1]]
        df = pd.DataFrame({
            't ref': [ref],
            'R ist': [self.data.iloc[-1][self.columns[0]]],
            't ist': [temp],
            't ref - t ist': [ref - temp]
        }, index=[
            int(
                time.mktime(
                    datetime.datetime.now().timetuple()
                )
            )
        ])
        self.record_values = pd.concat([self.record_values, df])
        self.export()

    def add_values(self, ref, max_res, min_res, mean_res, max_temp, min_temp, mean_temp):
        df = pd.DataFrame({
            't ref': ref,
            'R max': max_res,
            'R min': min_res,
            'R mittel': mean_res,
            't max': max_temp,
            't min': min_temp,
            't mittel': mean_temp,
            't ref - t mittel': ref - mean_temp
        })
        self.record_values = pd.concat([self.record_values, df])

    def add_value(self, res, temp):
        self.data = pd.concat(
            [
                self.data,
                pd.DataFrame(
                    {self.columns[0]: [res], self.columns[1]: [temp]},
                    index=[
                        int(
                            time.mktime(
                                datetime.datetime.now().timetuple()
                            )
                        )
                    ]
                )
            ]
        )

    def export(self):
        with pd.ExcelWriter(f"{self.filename}.xlsx") as writer:
            self.record_values.to_excel(writer, sheet_name="Daten")
            self.df_settings.to_excel(writer, sheet_name="Parameter")

class Kaye(QObject):

    config_ready = Signal()
    new_value = Signal(int, float)

    def __init__(self, parent):
        super().__init__()
        self.startTime = datetime.datetime.now()
        self.record_filename = Path(__file__).parent.joinpath(f"Record {self.startTime.strftime('%Y-%m-%d %H:%M')}.xlsx")
        self.interval = 1
        self.__read_channel = 0
        self.parent = parent
        self.ser = None
        self.id = None
        self.__ports = []
        self.settings = {}
        #self.data = []
        self.sonden = {}
        self.__search_thread = None
        self.__read_thread = None
        self.thread_pool = QThreadPool.globalInstance()
        self.record = pd.DataFrame()
        self.start_setup()

    @property
    def data(self):
        return pd.concat([
            snd.data for id, snd in self.sonden.items()
        ])

    @property
    def str_start_time(self):
        return self.startTime.strftime('%Y-%m-%d %H:%M')

    def stop(self):
        print("Messgerät stoppen")
        self.__read_thread.abbruch()
        # if self.t.isActive():
        #     self.t.stop()

    def df_settings(self):
        return None
        #
        #{
        #   3: {
        # 'ID': 'HALLO-1234567', 'LB': 'HALLO-LABEL12', 'UL': 'USER-LABEL123', 'CL': 'SCS-22-Feb-13', 'TS': 'ITS-90', 'R0': '+200.000', 'AL': '+1.5312578E-4', 'DE': '+1.5312578E-4', 'A4': '+1.5312578E-4', 'C4': '+1.5312578E-4'}, 
        #   7: {
        # 'ID': 'HALLO-1234567', 'LB': 'HALLO-LABEL12', 'UL': 'USER-LABEL123', 'CL': 'SCS-22-Feb-13', 'TS': 'ITS-90', 'R0': '+200.000', 'AL': '+1.5312578E-4',
        # 'DE': '+1.5312578E-4', 'A4': '+1.5312578E-4', 'C4': '+1.5312578E-4'}}


        
        
        return pd.DataFrame(
            [
                {
                    'ID': v['ID'],
                    'Label': v['LB'],
                    'User Label': v['UL'],
                    'Kalibriert': v['CL'],
                    'Temperatur System': v['TS'],
                    'R0': v['R0'],
                    'Alpha': v['AL'],
                    'Delta': v['DE'],
                    'A4': v['A4'],
                    'C4': v['C4']
                } for id, v in self.sonden.items()
            ],
            index=list(self.sonden.keys())
        )
        
        # return {
        #     f"{v['ID']} ({id})": pd.DataFrame({
        #         'ID': v['ID'],
        #         'Label': v['LB'],
        #         'User Label': v['UL'],
        #         'Kalibriert': v['CL'],
        #         'Temperatur System': v['TS'],
        #         'R0': v['R0'],
        #         'Alpha': v['AL'],
        #         'Delta': v['DE'],
        #         'A4': v['A4'],
        #         'C4': v['C4']
        #     }, index=[0]) for id, v in self.sonden.items()
        # }
        #print(self.settings)

    def add_record(self, ref_value):

        pass
        # for 

        # df = pd.DataFrame({

        # })

    def save_values(self, ref_value, selection, idx, values):
        for id, snd in self.sonden.items():
            snd.add_act_values(ref_value)
        # if selection == 1:
        #     for v in values:
        #         print(f"→→→ {v}")
            # for id, sonde in self.sonden.items():
            #     sonde.add_act_values(ref_value, )

    @property
    def channel_def(self):
        ret_dict = {
            'channels': 2 * len(self.sonden),
            'channel_types' : [],
            'channel_names': []
        }
        for id, d in self.sonden.items():
            ret_dict['channel_types'].extend(
                d.channel_types
            )
            ret_dict['channel_names'].extend(
                d.columns
            )
        return ret_dict

    def start_setup(self):
        self.setup_form = SetupFormKaye()

        for s in serial.tools.list_ports.comports(include_links=True):
            #print(s.device)
            self.setup_form.combo_port.addItem(f"{s.device} [{s.description}]")
            self.__ports.append(s)
            # print(s.name)
            # print(s.description)
            # print(s.hwid)
            # print(s.vid)
            # print(s.pid)
            # print(s.manufacturer)
            # print(s.interface)

        self.setup_form.btn_start.clicked.connect(self.config_closed)
        self.setup_form.action_sonde_suchen.triggered.connect(self.search)
        self.setup_form.btn_sonde_suchen.clicked.connect(self.search)

        self.setup_form.show()

    def show_hide_search(self, show=None):
        width = self.setup_form.frame_search.width()
        if show is None:
            if width == 0:
                show = True
                new_width = 105
            else:
                show = False
                new_width = 0
        elif show:
            new_width = 105
        else:
            new_width = 0
        
        #self.setup_form.frame_search.setMaximumWidth(new_width)
        self.animation = QPropertyAnimation(self.setup_form.frame_search, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()
        # if show:
        #     self.animation.finished.connect(self.__start_search)
        #QApplication.processEvents()

    def search(self):
        self.show_hide_search(True)
        self.ser_port = self.__ports[self.setup_form.combo_port.currentIndex()]
        self.baudrate = int(self.setup_form.combo_baud.currentText())
        if self.ser:
            self.ser.close()
            self.id = None
        self.sonden = {}
        self.ser = serial.Serial(
            self.ser_port.device,
            baudrate=self.baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=1,
            xonxoff=0,
            dsrdtr=False,
            rtscts=False,
        )
        time.sleep(2)
        self.ser.reset_input_buffer()
        max_index = self.setup_form.spin_last_id.value() + 1

        self.__search_thread = SearchKaye(self.ser, max_index)
        self.__search_thread.signals.search_progress.connect(self.update_search_id)
        self.__search_thread.signals.new_kaye.connect(self.new_kay)
        self.__search_thread.signals.finished.connect(self.search_finished)
        self.thread_pool.start(self.__search_thread)

    @Slot(int, dict)
    def new_kay(self, nr, details):
        print(f"Neue Sonde. ID: {nr}")

        #print(details)
        self.sonden[nr] = KayeSonde(self, details)
        print(self.sonden[nr].filename)
        print(self.sonden[nr].df_settings)
        #self.setup_form.radio_sonde_0.setText(f"ID: {i:02d}")
        #self.setup_form.radio_sonde_0.setChecked(True)
        # x = getattr(self.setup_form, f"text_AD").setText(f"{i:02d}")
        # #x.setText(data)
        # x = getattr(self.setup_form, f"text_{cmd}")

    @Slot(int)
    def update_search_id(self, nr):
        self.setup_form.lbl_search_id.setText(f"{nr:02d}")

    @Slot()
    def search_finished(self):
        #print(self.sonden)
        print(self.df_settings())
        # with pd.ExcelWriter(self.record_filename) as writer:
        #     for k, df in self.df_settings().items():
        #         print(f"==== {k} ===")
        #         print(df)
        #         df.to_excel(writer, sheet_name=k)

            # writer.save()

        self.show_hide_search(False)
        
    def decode_message(self, msg):
        sp = msg.split("=")
        cmd = sp[0].strip()
        data = sp[1].strip()
        return cmd, data

    def send_command(self, id, command, length=16):
        # print(self.sonden.keys())
        # id = list(self.sonden.keys())[0]
        self.ser.write(f"#{id:02d}{command}\r".encode('utf-8'))
        #self.ser.write(f"#{self.id:02d}{command}\r".encode('utf-8'))
        if (a := self.ser.read(length)) != b"":
            return a.decode('utf-8')
        return None

    def read_values(self):
        return
        #id = list(self.sonden.keys())[int(self.__read_channel / 2)]
        for e, id in enumerate(self.sonden):
            print(id)
            if (self.__read_channel % 2) == 0:
                if (msg := self.send_command(id, "VO", length=12)):
                    cmd, str_res = self.decode_message(msg)
                    if cmd == "VO":
                        res = float(str_res)
                        # print(f"Widerstand : {res}")
                        # self.new_value.emit(e * 2, res)
                        self.new_value.emit(self.__read_channel, res)
            else:
                if (msg := self.send_command(id, "VC", length=12)):
                    cmd, str_temp = self.decode_message(msg)
                    if cmd == "VC":
                        temp = float(str_temp)
                        # print(f"Temperatur : {temp}")
                        # self.new_value.emit(e * 2 + 1, temp)
                        self.new_value.emit(self.__read_channel, temp)
            self.__read_channel += 1
            if self.__read_channel >= (2 * len(self.sonden)):
                self.__read_channel = 0

    def config_closed(self):
        print("Konfiguration geschlossen")
        self.setup_form.hide()

        #self.lastValue = random.randint(50, 150)
        # self.t = QTimer()
        # self.t.timeout.connect(self.read_values)
        self.start()
        self.config_ready.emit()

    @Slot(QObject, float, float)
    def get_new_value(self, sonde, res, temp):
        sonde.add_value(res, temp)
        #print(f"Daten von {sonde}: Wid: {res} Temp: {temp}")
        self.new_value.emit(1, 0.0)
        # self.new_value.emit(nr, wert)

    def start(self):
        self.__read_thread = DataReceive(self.ser, self.sonden)
        self.__read_thread.signals.new_value.connect(self.get_new_value)
        #self.__read_thread.signals.new_kaye.connect(self.new_kay)
        #self.__read_thread.signals.finished.connect(self.search_finished)
        self.thread_pool.start(self.__read_thread)


        # if self.t.isActive():
        #     self.t.stop()

        # if not self.t.isActive():
        #     self.t.start(1000)


class SetupFormKaye(QWidget, Ui_Form):

    start = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start_instrument)

    def start_instrument(self):
        self.start.emit()


if __name__ == "__main__":
    pass
