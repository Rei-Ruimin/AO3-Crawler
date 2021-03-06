# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress_bar.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(355, 264)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/download.svg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
" QScrollBar:vertical {\n"
"     background:rgb(65, 59, 68);\n"
"     width: 15px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {\n"
"     background: rgb(128, 116, 139);\n"
"    border: 2px solid rgb(65, 59, 68);\n"
"alignment: bottom;\n"
" }\n"
"\n"
"\n"
"    QScrollBar::add-line:vertical {\n"
"        height: 0px;\n"
"        subcontrol-position: bottom;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"    QScrollBar::sub-line:vertical {\n"
"        height: 0 px;\n"
"        subcontrol-position: top;\n"
"        subcontrol-origin: margin;\n"
"    }\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 4, 0, 8)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.msg_l = QtWidgets.QLabel(Form)
        self.msg_l.setMinimumSize(QtCore.QSize(0, 20))
        self.msg_l.setStyleSheet("font: 7pt \"Verdana\";")
        self.msg_l.setObjectName("msg_l")
        self.verticalLayout.addWidget(self.msg_l, 0, QtCore.Qt.AlignHCenter)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 0))
        self.textBrowser.setStyleSheet("QTextEdit{\n"
"    background-color: rgb(54, 48, 68);\n"
"color: white;\n"
"border: 0.5pt lightgray;\n"
"    \n"
"    font: 7pt \"微软雅黑\";\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.open_folder_btn = QtWidgets.QPushButton(Form)
        self.open_folder_btn.setEnabled(False)
        self.open_folder_btn.setMinimumSize(QtCore.QSize(100, 20))
        self.open_folder_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.open_folder_btn.setStyleSheet("QPushButton:enabled{\n"
"    \n"
"    background-color: rgb(85, 0, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    font: 7pt \"Verdana\";\n"
"    border-style:none;\n"
"    padding:3px;\n"
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
"}\n"
"\n"
"QPushButton:disabled{\n"
"        background-color: gray;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    font: 7pt \"Verdana\";\n"
"    border-style:none;\n"
"    padding:3px;\n"
"    border-radius:8px;\n"
"}")
        self.open_folder_btn.setFlat(False)
        self.open_folder_btn.setObjectName("open_folder_btn")
        self.verticalLayout.addWidget(self.open_folder_btn, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 20)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.msg_l.raise_()
        self.open_folder_btn.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        self.open_folder_btn.clicked.connect(Form.open_folder)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "A03 Crawler"))
        self.msg_l.setText(_translate("Form", "Loading..."))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:7pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.open_folder_btn.setText(_translate("Form", "Open the folder"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
