# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cont_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(236, 96)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/download.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("font: 7pt \"Verdana\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    font: 7pt \"Verdana\";\n"
"    border-style:none;\n"
"    padding:3px;\n"
"    min-height:20px;\n"
"    min-width:40px;\n"
"    border-radius:8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 85, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgb(68, 0, 206);\n"
"}")
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.ok_btn.clicked.connect(Dialog.cont_info_ok_btn_c)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AO3 Crawler"))
        self.label.setText(_translate("Dialog", "Data from last running is found, the program will continue!"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())