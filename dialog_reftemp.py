# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_reftemp.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)
import ressource_rc

class Ui_dlg_referenz(object):
    def setupUi(self, dlg_referenz):
        if not dlg_referenz.objectName():
            dlg_referenz.setObjectName(u"dlg_referenz")
        dlg_referenz.resize(400, 206)
        icon = QIcon()
        icon.addFile(u":/icons/IRTD", QSize(), QIcon.Normal, QIcon.Off)
        dlg_referenz.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(dlg_referenz)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(dlg_referenz)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.edit_ref_temp = QLineEdit(dlg_referenz)
        self.edit_ref_temp.setObjectName(u"edit_ref_temp")
        self.edit_ref_temp.setToolTipDuration(-1)
        self.edit_ref_temp.setAlignment(Qt.AlignCenter)
        self.edit_ref_temp.setDragEnabled(False)
        self.edit_ref_temp.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.edit_ref_temp)

        self.group_type = QGroupBox(dlg_referenz)
        self.group_type.setObjectName(u"group_type")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_type.sizePolicy().hasHeightForWidth())
        self.group_type.setSizePolicy(sizePolicy)
        self.group_type.setMaximumSize(QSize(16777215, 92))
        self.verticalLayout_2 = QVBoxLayout(self.group_type)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radio_act = QRadioButton(self.group_type)
        self.radio_act.setObjectName(u"radio_act")
        self.radio_act.setChecked(True)

        self.verticalLayout_2.addWidget(self.radio_act)

        self.radio_stat = QRadioButton(self.group_type)
        self.radio_stat.setObjectName(u"radio_stat")

        self.verticalLayout_2.addWidget(self.radio_stat)


        self.verticalLayout.addWidget(self.group_type)

        self.buttonBox = QDialogButtonBox(dlg_referenz)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(dlg_referenz)
        self.buttonBox.accepted.connect(dlg_referenz.accept)
        self.buttonBox.rejected.connect(dlg_referenz.reject)

        QMetaObject.connectSlotsByName(dlg_referenz)
    # setupUi

    def retranslateUi(self, dlg_referenz):
        dlg_referenz.setWindowTitle(QCoreApplication.translate("dlg_referenz", u"Referenztemperatur", None))
        self.label.setText(QCoreApplication.translate("dlg_referenz", u"Referenztemperatur eingeben", None))
#if QT_CONFIG(tooltip)
        self.edit_ref_temp.setToolTip(QCoreApplication.translate("dlg_referenz", u"Temperatur in \u00b0C", None))
#endif // QT_CONFIG(tooltip)
        self.group_type.setTitle(QCoreApplication.translate("dlg_referenz", u"Art der Aufzeichnung", None))
        self.radio_act.setText(QCoreApplication.translate("dlg_referenz", u"Aktueller Wert", None))
        self.radio_stat.setText(QCoreApplication.translate("dlg_referenz", u"Maximum / Minimum und Mittelwert der Auswahl", None))
    # retranslateUi

