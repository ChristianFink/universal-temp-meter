# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kaye.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)
import ressource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(675, 934)
        icon = QIcon()
        icon.addFile(u":/icons/IRTD", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.action_sonde_suchen = QAction(Form)
        self.action_sonde_suchen.setObjectName(u"action_sonde_suchen")
        self.action_sonde_suchen.setIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.label)

        self.btn_sonde_suchen = QToolButton(self.frame_3)
        self.btn_sonde_suchen.setObjectName(u"btn_sonde_suchen")
        self.btn_sonde_suchen.setIcon(icon)
        self.btn_sonde_suchen.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.btn_sonde_suchen)


        self.verticalLayout.addWidget(self.frame_3)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(16777215, 88))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.textEdit.setFont(font1)
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_15)

        self.combo_baud = QComboBox(self.frame)
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.addItem("")
        self.combo_baud.setObjectName(u"combo_baud")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.combo_baud.sizePolicy().hasHeightForWidth())
        self.combo_baud.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.combo_baud)

        self.combo_port = QComboBox(self.frame)
        self.combo_port.setObjectName(u"combo_port")
        sizePolicy2.setHeightForWidth(self.combo_port.sizePolicy().hasHeightForWidth())
        self.combo_port.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.combo_port)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_18)

        self.spin_last_id = QSpinBox(self.frame)
        self.spin_last_id.setObjectName(u"spin_last_id")
        self.spin_last_id.setMinimum(5)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spin_last_id)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.frame_search = QFrame(self.frame)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 0))
        self.frame_search.setMaximumSize(QSize(0, 84))
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_search)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label_16 = QLabel(self.frame_search)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_2.addWidget(self.label_16)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_17 = QLabel(self.frame_search)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setPointSize(16)
        self.label_17.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_17)

        self.lbl_search_id = QLabel(self.frame_search)
        self.lbl_search_id.setObjectName(u"lbl_search_id")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.lbl_search_id.setFont(font3)
        self.lbl_search_id.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_search_id)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addWidget(self.frame_search)


        self.verticalLayout.addWidget(self.frame)

        self.btn_sonde_suchen_2 = QPushButton(Form)
        self.btn_sonde_suchen_2.setObjectName(u"btn_sonde_suchen_2")

        self.verticalLayout.addWidget(self.btn_sonde_suchen_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_id_sonden = QFrame(self.groupBox)
        self.frame_id_sonden.setObjectName(u"frame_id_sonden")
        self.frame_id_sonden.setFrameShape(QFrame.StyledPanel)
        self.frame_id_sonden.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_id_sonden)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radio_sonde_0 = QRadioButton(self.frame_id_sonden)
        self.radio_sonde_0.setObjectName(u"radio_sonde_0")

        self.horizontalLayout_4.addWidget(self.radio_sonde_0)


        self.verticalLayout_3.addWidget(self.frame_id_sonden)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_10)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_12)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_14)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.line)

        self.text_AD = QLineEdit(self.frame_2)
        self.text_AD.setObjectName(u"text_AD")
        self.text_AD.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.text_AD)

        self.text_ID = QLineEdit(self.frame_2)
        self.text_ID.setObjectName(u"text_ID")
        self.text_ID.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.text_ID)

        self.text_LB = QLineEdit(self.frame_2)
        self.text_LB.setObjectName(u"text_LB")
        self.text_LB.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.text_LB)

        self.text_UL = QLineEdit(self.frame_2)
        self.text_UL.setObjectName(u"text_UL")
        self.text_UL.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.text_UL)

        self.text_CL = QLineEdit(self.frame_2)
        self.text_CL.setObjectName(u"text_CL")
        self.text_CL.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.text_CL)

        self.text_AL = QLineEdit(self.frame_2)
        self.text_AL.setObjectName(u"text_AL")
        self.text_AL.setReadOnly(True)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.text_AL)

        self.text_A4 = QLineEdit(self.frame_2)
        self.text_A4.setObjectName(u"text_A4")
        self.text_A4.setReadOnly(True)

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.text_A4)

        self.text_DE = QLineEdit(self.frame_2)
        self.text_DE.setObjectName(u"text_DE")
        self.text_DE.setReadOnly(True)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.text_DE)

        self.text_TS = QLineEdit(self.frame_2)
        self.text_TS.setObjectName(u"text_TS")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.text_TS)

        self.text_C4 = QLineEdit(self.frame_2)
        self.text_C4.setObjectName(u"text_C4")
        self.text_C4.setReadOnly(True)

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.text_C4)

        self.text_R0 = QLineEdit(self.frame_2)
        self.text_R0.setObjectName(u"text_R0")
        self.text_R0.setReadOnly(True)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.text_R0)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.btn_save_parameter = QPushButton(Form)
        self.btn_save_parameter.setObjectName(u"btn_save_parameter")

        self.verticalLayout.addWidget(self.btn_save_parameter)

        self.btn_start = QPushButton(Form)
        self.btn_start.setObjectName(u"btn_start")

        self.verticalLayout.addWidget(self.btn_start)


        self.retranslateUi(Form)
        self.btn_sonde_suchen.triggered.connect(self.action_sonde_suchen.trigger)
        self.btn_sonde_suchen_2.clicked.connect(self.action_sonde_suchen.trigger)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Setup Kaye-Sonde", None))
        self.action_sonde_suchen.setText(QCoreApplication.translate("Form", u"Sonde suchen", None))
#if QT_CONFIG(tooltip)
        self.action_sonde_suchen.setToolTip(QCoreApplication.translate("Form", u"Sucht nach einer Sonde", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Konfiguration KAYE-Sonde", None))
        self.btn_sonde_suchen.setText(QCoreApplication.translate("Form", u"Sonde suchen", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:400;\">Aktuell wird nur eine KAYE-Sonde unterst\u00fctzt. Die erste Adresse die gefunden wird, wird verwendet.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:400;\">Das Schreiben von Kalibrierdatum und Koeffizienten wird sp\u00e4ter implementiert.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Serielle Schnittstelle", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"BaudRate", None))
        self.combo_baud.setItemText(0, QCoreApplication.translate("Form", u"9600", None))
        self.combo_baud.setItemText(1, QCoreApplication.translate("Form", u"4800", None))
        self.combo_baud.setItemText(2, QCoreApplication.translate("Form", u"2400", None))
        self.combo_baud.setItemText(3, QCoreApplication.translate("Form", u"1200", None))
        self.combo_baud.setItemText(4, QCoreApplication.translate("Form", u"600", None))
        self.combo_baud.setItemText(5, QCoreApplication.translate("Form", u"300", None))

        self.label_18.setText(QCoreApplication.translate("Form", u"letzte ID", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Suche Sonde...", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"ID:", None))
        self.lbl_search_id.setText(QCoreApplication.translate("Form", u"00", None))
        self.btn_sonde_suchen_2.setText(QCoreApplication.translate("Form", u"Sonde suchen", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Gefundene Sonden", None))
        self.radio_sonde_0.setText(QCoreApplication.translate("Form", u"ID: 0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Adresse", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Label", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"User Label", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Kalibrierung", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Temperatur-Skala", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"R0", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Alpha", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Delta", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"A4", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"C4", None))
        self.btn_save_parameter.setText(QCoreApplication.translate("Form", u"Parameter speichern", None))
        self.btn_start.setText(QCoreApplication.translate("Form", u"Schliessen und Messung starten", None))
    # retranslateUi

