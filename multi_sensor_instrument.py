# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multi_sensor_instrument.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_SetupForm(object):
    def setupUi(self, SetupForm):
        if not SetupForm.objectName():
            SetupForm.setObjectName(u"SetupForm")
        SetupForm.resize(781, 238)
        SetupForm.setMinimumSize(QSize(781, 238))
        SetupForm.setMaximumSize(QSize(781, 238))
        self.verticalLayout = QVBoxLayout(SetupForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SetupForm)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(SetupForm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.spin_probes_count = QSpinBox(self.frame)
        self.spin_probes_count.setObjectName(u"spin_probes_count")
        self.spin_probes_count.setMinimum(1)
        self.spin_probes_count.setMaximum(25)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spin_probes_count)

        self.spin_interval = QSpinBox(self.frame)
        self.spin_interval.setObjectName(u"spin_interval")
        self.spin_interval.setMinimum(1)
        self.spin_interval.setMaximum(30)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spin_interval)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.check_common = QCheckBox(self.frame)
        self.check_common.setObjectName(u"check_common")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.check_common)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_start = QPushButton(SetupForm)
        self.btn_start.setObjectName(u"btn_start")

        self.verticalLayout.addWidget(self.btn_start)


        self.retranslateUi(SetupForm)

        QMetaObject.connectSlotsByName(SetupForm)
    # setupUi

    def retranslateUi(self, SetupForm):
        SetupForm.setWindowTitle(QCoreApplication.translate("SetupForm", u"Dummy-Messger\u00e4t", None))
        self.label.setText(QCoreApplication.translate("SetupForm", u"Dummy-Messger\u00e4t mit mehreren F\u00fchlern", None))
        self.label_2.setText(QCoreApplication.translate("SetupForm", u"Anzahl F\u00fchler", None))
        self.spin_interval.setSuffix(QCoreApplication.translate("SetupForm", u" Sekunde(n)", None))
        self.label_3.setText(QCoreApplication.translate("SetupForm", u"Abtastintervall", None))
        self.label_4.setText(QCoreApplication.translate("SetupForm", u"F\u00fchler gleichzeitig messen", None))
        self.check_common.setText("")
        self.btn_start.setText(QCoreApplication.translate("SetupForm", u"Messger\u00e4t starten", None))
    # retranslateUi

