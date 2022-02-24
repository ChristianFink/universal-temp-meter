# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDoubleSpinBox, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QRadioButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableView, QTimeEdit, QToolBar,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 905)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        icon = QIcon()
        icon.addFile(u":/icons/exit", QSize(), QIcon.Normal, QIcon.Off)
        self.action_quit.setIcon(icon)
        self.action_follow = QAction(MainWindow)
        self.action_follow.setObjectName(u"action_follow")
        self.action_follow.setCheckable(True)
        self.action_follow.setChecked(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/play", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icons/pause", QSize(), QIcon.Normal, QIcon.On)
        self.action_follow.setIcon(icon1)
        self.action_1_min = QAction(MainWindow)
        self.action_1_min.setObjectName(u"action_1_min")
        self.action_5_min = QAction(MainWindow)
        self.action_5_min.setObjectName(u"action_5_min")
        self.action_10_min = QAction(MainWindow)
        self.action_10_min.setObjectName(u"action_10_min")
        self.action_20_min = QAction(MainWindow)
        self.action_20_min.setObjectName(u"action_20_min")
        self.action_30_min = QAction(MainWindow)
        self.action_30_min.setObjectName(u"action_30_min")
        self.action_40_min = QAction(MainWindow)
        self.action_40_min.setObjectName(u"action_40_min")
        self.action_kaye_sonde = QAction(MainWindow)
        self.action_kaye_sonde.setObjectName(u"action_kaye_sonde")
        icon2 = QIcon()
        icon2.addFile(u":/icons/IRTD", QSize(), QIcon.Normal, QIcon.Off)
        self.action_kaye_sonde.setIcon(icon2)
        self.action_show_hide_big_values = QAction(MainWindow)
        self.action_show_hide_big_values.setObjectName(u"action_show_hide_big_values")
        self.action_show_hide_big_values.setCheckable(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/burger", QSize(), QIcon.Normal, QIcon.Off)
        self.action_show_hide_big_values.setIcon(icon3)
        self.action_save_values = QAction(MainWindow)
        self.action_save_values.setObjectName(u"action_save_values")
        icon4 = QIcon()
        icon4.addFile(u":/icons/save", QSize(), QIcon.Normal, QIcon.Off)
        self.action_save_values.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.group_aktuell = QGroupBox(self.centralwidget)
        self.group_aktuell.setObjectName(u"group_aktuell")
        self.horizontalLayout_4 = QHBoxLayout(self.group_aktuell)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_temp_act = QLabel(self.group_aktuell)
        self.lbl_temp_act.setObjectName(u"lbl_temp_act")
        font = QFont()
        font.setFamilies([u"Typewriter"])
        font.setPointSize(20)
        self.lbl_temp_act.setFont(font)

        self.horizontalLayout_4.addWidget(self.lbl_temp_act)

        self.lbl_res_act = QLabel(self.group_aktuell)
        self.lbl_res_act.setObjectName(u"lbl_res_act")
        self.lbl_res_act.setFont(font)

        self.horizontalLayout_4.addWidget(self.lbl_res_act)


        self.horizontalLayout.addWidget(self.group_aktuell)

        self.group_mittelwert = QGroupBox(self.centralwidget)
        self.group_mittelwert.setObjectName(u"group_mittelwert")
        self.horizontalLayout_5 = QHBoxLayout(self.group_mittelwert)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_temp_mean = QLabel(self.group_mittelwert)
        self.lbl_temp_mean.setObjectName(u"lbl_temp_mean")
        self.lbl_temp_mean.setFont(font)

        self.horizontalLayout_5.addWidget(self.lbl_temp_mean)

        self.lbl_res_mean = QLabel(self.group_mittelwert)
        self.lbl_res_mean.setObjectName(u"lbl_res_mean")
        self.lbl_res_mean.setFont(font)

        self.horizontalLayout_5.addWidget(self.lbl_res_mean)


        self.horizontalLayout.addWidget(self.group_mittelwert)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.stat2 = QWidget()
        self.stat2.setObjectName(u"stat2")
        self.verticalLayout_2 = QVBoxLayout(self.stat2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label = QLabel(self.stat2)
        self.label.setObjectName(u"label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label)

        self.text_stat_res_time_2 = QLabel(self.stat2)
        self.text_stat_res_time_2.setObjectName(u"text_stat_res_time_2")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.text_stat_res_time_2)


        self.verticalLayout_2.addLayout(self.formLayout_3)

        self.table_statistic = QTableView(self.stat2)
        self.table_statistic.setObjectName(u"table_statistic")

        self.verticalLayout_2.addWidget(self.table_statistic)

        self.tabWidget.addTab(self.stat2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_3.addWidget(self.tableView)

        self.tabWidget.addTab(self.tab, "")
        self.tab_stab = QWidget()
        self.tab_stab.setObjectName(u"tab_stab")
        self.gridLayout = QGridLayout(self.tab_stab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.radio_stab_temp = QRadioButton(self.tab_stab)
        self.radio_stab_temp.setObjectName(u"radio_stab_temp")

        self.gridLayout.addWidget(self.radio_stab_temp, 2, 0, 1, 1)

        self.radio_stab_off = QRadioButton(self.tab_stab)
        self.radio_stab_off.setObjectName(u"radio_stab_off")
        self.radio_stab_off.setChecked(True)

        self.gridLayout.addWidget(self.radio_stab_off, 0, 0, 1, 1)

        self.radio_stab_res = QRadioButton(self.tab_stab)
        self.radio_stab_res.setObjectName(u"radio_stab_res")

        self.gridLayout.addWidget(self.radio_stab_res, 1, 0, 1, 1)

        self.dblSpinBox_stab_res = QDoubleSpinBox(self.tab_stab)
        self.dblSpinBox_stab_res.setObjectName(u"dblSpinBox_stab_res")
        self.dblSpinBox_stab_res.setDecimals(3)
        self.dblSpinBox_stab_res.setSingleStep(0.001000000000000)
        self.dblSpinBox_stab_res.setValue(0.005000000000000)

        self.gridLayout.addWidget(self.dblSpinBox_stab_res, 1, 1, 1, 1)

        self.text_stab_status = QLabel(self.tab_stab)
        self.text_stab_status.setObjectName(u"text_stab_status")

        self.gridLayout.addWidget(self.text_stab_status, 3, 1, 1, 1)

        self.lbl_stab_status = QLabel(self.tab_stab)
        self.lbl_stab_status.setObjectName(u"lbl_stab_status")
        self.lbl_stab_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.lbl_stab_status, 3, 0, 1, 1)

        self.time_edit_stab = QTimeEdit(self.tab_stab)
        self.time_edit_stab.setObjectName(u"time_edit_stab")
        self.time_edit_stab.setCurrentSection(QDateTimeEdit.HourSection)
        self.time_edit_stab.setTime(QTime(0, 10, 0))

        self.gridLayout.addWidget(self.time_edit_stab, 0, 1, 1, 1)

        self.dblSpinBox_stab_temp = QDoubleSpinBox(self.tab_stab)
        self.dblSpinBox_stab_temp.setObjectName(u"dblSpinBox_stab_temp")
        self.dblSpinBox_stab_temp.setDecimals(3)
        self.dblSpinBox_stab_temp.setMaximum(3.000000000000000)
        self.dblSpinBox_stab_temp.setSingleStep(0.001000000000000)
        self.dblSpinBox_stab_temp.setValue(0.020000000000000)

        self.gridLayout.addWidget(self.dblSpinBox_stab_temp, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tab_stab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.verticalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 30))
        self.menuIntervall = QMenu(self.menubar)
        self.menuIntervall.setObjectName(u"menuIntervall")
        self.menuGer_t = QMenu(self.menubar)
        self.menuGer_t.setObjectName(u"menuGer_t")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setIconSize(QSize(32, 32))
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuGer_t.menuAction())
        self.menubar.addAction(self.menuIntervall.menuAction())
        self.menuIntervall.addAction(self.action_1_min)
        self.menuIntervall.addAction(self.action_5_min)
        self.menuIntervall.addAction(self.action_10_min)
        self.menuIntervall.addAction(self.action_20_min)
        self.menuIntervall.addAction(self.action_30_min)
        self.menuIntervall.addAction(self.action_40_min)
        self.menuGer_t.addAction(self.action_kaye_sonde)
        self.toolBar.addAction(self.action_follow)
        self.toolBar.addAction(self.action_save_values)
        self.toolBar.addAction(self.action_show_hide_big_values)
        self.toolBar.addAction(self.action_quit)
        self.toolBar.addAction(self.action_1_min)
        self.toolBar.addAction(self.action_5_min)
        self.toolBar.addAction(self.action_10_min)
        self.toolBar.addAction(self.action_20_min)
        self.toolBar.addAction(self.action_30_min)
        self.toolBar.addAction(self.action_40_min)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fluke-Superthermometer", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
#if QT_CONFIG(tooltip)
        self.action_quit.setToolTip(QCoreApplication.translate("MainWindow", u"Beendet das Programm", None))
#endif // QT_CONFIG(tooltip)
        self.action_follow.setText(QCoreApplication.translate("MainWindow", u"Follow", None))
#if QT_CONFIG(tooltip)
        self.action_follow.setToolTip(QCoreApplication.translate("MainWindow", u"Automatisch verfolgen", None))
#endif // QT_CONFIG(tooltip)
        self.action_1_min.setText(QCoreApplication.translate("MainWindow", u"1 Min.", None))
#if QT_CONFIG(tooltip)
        self.action_1_min.setToolTip(QCoreApplication.translate("MainWindow", u"1 Minute", None))
#endif // QT_CONFIG(tooltip)
        self.action_5_min.setText(QCoreApplication.translate("MainWindow", u"5 Min.", None))
#if QT_CONFIG(tooltip)
        self.action_5_min.setToolTip(QCoreApplication.translate("MainWindow", u"5 Minuten", None))
#endif // QT_CONFIG(tooltip)
        self.action_10_min.setText(QCoreApplication.translate("MainWindow", u"10 Min.", None))
#if QT_CONFIG(tooltip)
        self.action_10_min.setToolTip(QCoreApplication.translate("MainWindow", u"10 Minuten", None))
#endif // QT_CONFIG(tooltip)
        self.action_20_min.setText(QCoreApplication.translate("MainWindow", u"20 Min", None))
#if QT_CONFIG(tooltip)
        self.action_20_min.setToolTip(QCoreApplication.translate("MainWindow", u"20 Minuten", None))
#endif // QT_CONFIG(tooltip)
        self.action_30_min.setText(QCoreApplication.translate("MainWindow", u"30 Min.", None))
#if QT_CONFIG(tooltip)
        self.action_30_min.setToolTip(QCoreApplication.translate("MainWindow", u"30 Minuten", None))
#endif // QT_CONFIG(tooltip)
        self.action_40_min.setText(QCoreApplication.translate("MainWindow", u"40 Min", None))
#if QT_CONFIG(tooltip)
        self.action_40_min.setToolTip(QCoreApplication.translate("MainWindow", u"40 Minuten", None))
#endif // QT_CONFIG(tooltip)
        self.action_kaye_sonde.setText(QCoreApplication.translate("MainWindow", u"Kaye-Sonde", None))
        self.action_show_hide_big_values.setText(QCoreApplication.translate("MainWindow", u"Grosse Werte", None))
#if QT_CONFIG(tooltip)
        self.action_show_hide_big_values.setToolTip(QCoreApplication.translate("MainWindow", u"Zeigt / Versteckt grosse Werte", None))
#endif // QT_CONFIG(tooltip)
        self.action_save_values.setText(QCoreApplication.translate("MainWindow", u"Werte Speichern", None))
#if QT_CONFIG(tooltip)
        self.action_save_values.setToolTip(QCoreApplication.translate("MainWindow", u"Speichert die aktuellen Messwerte", None))
#endif // QT_CONFIG(tooltip)
        self.group_aktuell.setTitle(QCoreApplication.translate("MainWindow", u"Aktuell", None))
        self.lbl_temp_act.setText(QCoreApplication.translate("MainWindow", u"t: 0.0000 \u00b0C", None))
        self.lbl_res_act.setText(QCoreApplication.translate("MainWindow", u"R: 0.0000 \u03a9", None))
        self.group_mittelwert.setTitle(QCoreApplication.translate("MainWindow", u"Mittelwert", None))
        self.lbl_temp_mean.setText(QCoreApplication.translate("MainWindow", u"t: 0.0000 \u00b0C", None))
        self.lbl_res_mean.setText(QCoreApplication.translate("MainWindow", u"R: 0.0000 \u03a9", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zeitraum:", None))
        self.text_stat_res_time_2.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stat2), QCoreApplication.translate("MainWindow", u"Statistik", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tabelle", None))
        self.radio_stab_temp.setText(QCoreApplication.translate("MainWindow", u"Temperatur", None))
        self.radio_stab_off.setText(QCoreApplication.translate("MainWindow", u"Aus", None))
        self.radio_stab_res.setText(QCoreApplication.translate("MainWindow", u"Widerstand", None))
        self.dblSpinBox_stab_res.setSuffix(QCoreApplication.translate("MainWindow", u" \u03a9", None))
        self.text_stab_status.setText(QCoreApplication.translate("MainWindow", u"keine Stabilit\u00e4t", None))
        self.lbl_stab_status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.time_edit_stab.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.dblSpinBox_stab_temp.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0C", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stab), QCoreApplication.translate("MainWindow", u"Stabilit\u00e4t", None))
        self.menuIntervall.setTitle(QCoreApplication.translate("MainWindow", u"Intervall", None))
        self.menuGer_t.setTitle(QCoreApplication.translate("MainWindow", u"Ger\u00e4t", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

