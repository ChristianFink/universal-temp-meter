#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Filename: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer/dummy.py
Path: /home/christian/Programmieren/Python/Messen/Sammlung/SuperThermometer
Created Date: Saturday, January 29th 2022, 3:41:49 pm
Author: Christian Fink

Copyright (c) 2022 Your Company
"""

import sys
# import time
# import asyncio
# from pathlib import Path
import random
from definitions import MeasureType

from multi_sensor_instrument import Ui_SetupForm
# from ui_mainwindow import Ui_MainWindow
# import time

from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtWidgets import QWidget

class DummyMeter(QObject):

    new_value = Signal(int, float)
    config_ready = Signal()

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.cb = None
        self.interval = 1000
        #self.config_closed()

    def config_closed(self):
        self.lastValue = random.randint(50, 150)
        self.t = QTimer()
        self.t.timeout.connect(self.new_res)
        self.config_ready.emit()

    @property
    def channel_def(self):
        return {
            'channels': 2,
            'channel_types': [MeasureType.PT100],
            'channel_names': ['Widerstand']
        }

    def setInterval(self, interval):
        if interval != self.interval:
            self.interval = interval
        
        if self.t.isActive():
            self.t.stop()
            if not self.t.isActive():
                self.t.start(self.interval)

    def start(self, interval=None):
        if interval and (self.interval != interval):
            self.interval = interval
            if self.t.isActive():
                self.t.stop()

        if not self.t.isActive():
            self.t.start(self.interval)
                
    def stop(self):
        print("Messgerät stoppen")
        if self.t.isActive():
            self.t.stop()

    def add_callback(self, cb):
        self.cb = cb

    def new_res(self):
        new_value = random.randint(
            int(self.lastValue * 990),
            int(self.lastValue * 1010)
        ) / 1000
        if new_value > 200:
            new_value = 200
        if new_value < 20:
            new_value = 20
        self.lastValue = new_value
        if self.cb:
            self.cb(new_value)
        self.new_value.emit(0, new_value)

class SetupFormDummyTempMeter(QWidget, Ui_SetupForm):

    start = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start_instrument)

    def start_instrument(self):
        print("START")
        self.start.emit()


class DummyTempMeter(QObject):

    new_value = Signal(int, float)
    config_ready = Signal()

    def __init__(self, main):
        super().__init__()
        self.main = main
        self.combine_scan = True
        self.__channels = 10

        self.max_temp = 660
        self.min_temp = -196
        
        self.cb = None
        self.interval = 1000
        self.next_scan_channel = 0

        self.setup_form = SetupFormDummyTempMeter()
        self.setup_form.show()
        self.setup_form.start.connect(self.config_closed)
        if self.combine_scan:
            self.setup_form.spin_interval.setValue(int(self.interval / 1000))
        else:
            self.setup_form.spin_interval.setValue(int((self.interval * self.__channels )/ 1000))
        self.setup_form.check_common.setChecked(self.combine_scan)
        self.setup_form.spin_probes_count.setValue(self.__channels)

    def config_closed(self):
        self.combine_scan = self.setup_form.check_common.isChecked()
        self.__channels = self.setup_form.spin_probes_count.value()

        if self.combine_scan:
            self.interval = self.setup_form.spin_interval.value() * 1000
        else:
            self.interval = self.setup_form.spin_interval.value() * 1000 / self.__channels

        self.setup_form.close()
        self.last_values = [
            random.randint(int(self.min_temp), int(self.max_temp)) for x in range(self.__channels)
        ]
        self.t = QTimer()
        self.t.timeout.connect(self.new_temp)
        self.config_ready.emit()

    @property
    def channel_def(self):
        return {
            'channels': self.__channels,
            'channel_types': [MeasureType.TEMP for x in range(self.__channels)],
            'channel_names': [f"M{x:02d}" for x in range(self.__channels)]
        }

    def setInterval(self, interval):
        if interval != self.interval:
            self.interval = interval
        
        if self.t.isActive():
            self.t.stop()
            if not self.t.isActive():
                self.t.start(self.interval)

    def start(self, interval=None):
        if interval and (self.interval != interval):
            self.interval = interval
            if self.t.isActive():
                self.t.stop()

        if not self.t.isActive():
            self.t.start(self.interval)

    def stop(self):
        print("Messgerät stoppen")
        if self.t.isActive():
            self.t.stop()

    def add_callback(self, cb):
        self.cb = cb

    def new_temp(self):
        if self.combine_scan:
            for x in range(self.__channels):
                lv = self.last_values[x]
                _v = [int(lv * 950), int(lv * 1050)]
                new_value = random.randint(min(_v), max(_v)) / 1000
                if new_value > self.max_temp:
                    new_value = self.max_temp
                if new_value < self.min_temp:
                    new_value = self.min_temp
                self.last_values[x] = new_value
                if self.cb:
                    self.cb(x, new_value)
                self.new_value.emit(x, new_value)
        else:
            lv = self.last_values[self.next_scan_channel]
            _v = [int(lv * 950), int(lv * 1050)]
            new_value = random.randint(min(_v), max(_v)) / 1000
            if new_value > self.max_temp:
                new_value = self.max_temp
            if new_value < self.min_temp:
                new_value = self.min_temp
            self.last_values[self.next_scan_channel] = new_value
            if self.cb:
                self.cb(self.next_scan_channel, new_value)
            self.new_value.emit(self.next_scan_channel, new_value)
            self.next_scan_channel += 1
            if self.next_scan_channel >= self.__channels:
                self.next_scan_channel = 0
