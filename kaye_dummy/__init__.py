
import time
import pandas as pd
from pathlib import Path
import json

from PySide6.QtCore import QObject, Signal, Slot, QPropertyAnimation, QEasingCurve, QRunnable, QThreadPool
from PySide6.QtWidgets import QWidget

from kaye.kaye_ui import Ui_Form
from definitions import MeasureType


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

        self.parent = parent
        self.interval = 1

        self.ser = None
        self.__ports = []

        self.sonden = {}

        self.__search_thread = None
        self.__read_thread = None

        self.thread_pool = QThreadPool.globalInstance()

        self.start_setup()


    def df_settings(self):
        return None
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
        self.sonden = {}

        max_index = self.setup_form.spin_last_id.value() + 1
        self.__search_thread = SearchKaye(max_index)
        self.__search_thread.signals.search_progress.connect(self.update_search_id)
        self.__search_thread.signals.new_kaye.connect(self.new_kay)
        self.__search_thread.signals.finished.connect(self.search_finished)
        self.thread_pool.start(self.__search_thread)

    def config_closed(self):
        pass

    def start_setup(self):
        self.setup_form = SetupFormKaye()

        # Serielle Schnittstellen auflisten
        for s in ["COM1", "COM2", "COM3"]:
            self.setup_form.combo_port.addItem(f"{s}")
            self.__ports.append(s)

        self.setup_form.btn_start.clicked.connect(self.config_closed)
        self.setup_form.action_sonde_suchen.triggered.connect(self.search)
        self.setup_form.btn_sonde_suchen.clicked.connect(self.search)

        self.setup_form.show()        

    @Slot(int)
    def update_search_id(self, nr):
        self.setup_form.lbl_search_id.setText(f"{nr:02d}")

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
        

class SetupFormKaye(QWidget, Ui_Form):

    start = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start_instrument)

    def start_instrument(self):
        self.start.emit()


class SearchKayeSignals(QObject):
    new_kaye = Signal(int, dict)
    search_progress = Signal(int)
    finished = Signal()

class SearchKaye(QRunnable):

    def __init__(self, max_index):
        super().__init__()
        self.signals = SearchKayeSignals()
        self.max_index = max_index
        print("Suche initialisiert")

    @Slot()
    def run(self):
        for i in range(1, self.max_index):
            self.signals.search_progress.emit(i)            
            if i == 3:
                time.sleep(2)
                sonde_details = {
                    'ID': "TEST 1",
                    'LB': "Label",
                    'UL': "User-Label",
                    'CL': "SCS-2022-01-15",
                    'TS': "ITS90",
                    'R0': 200.123,
                    'AL': 1.23456E+3,
                    'DE': 2.34566E+4,
                    'A4': 3.45678E+5,
                    'C4': 4.56786E+6
                }
            elif i == 7:
                time.sleep(2)
                sonde_details = {
                    'ID': "TEST 2",
                    'LB': "Label",
                    'UL': "User-Label",
                    'CL': "SCS-2022-01-15",
                    'TS': "ITS90",
                    'R0': 200.123,
                    'AL': 1.23456E+3,
                    'DE': 2.34566E+4,
                    'A4': 3.45678E+5,
                    'C4': 4.56786E+6
                }
            else:
                time.sleep(1)
                continue
            self.signals.new_kaye.emit(i, sonde_details)
        self.signals.finished.emit()
