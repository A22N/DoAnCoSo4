# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GiaiMaHopDong.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GiaiMaWindow(object):
    def setupUi(self, GiaiMaWindow):
        GiaiMaWindow.setObjectName("GiaiMaWindow")
        GiaiMaWindow.resize(600, 300)
        self.centralwidget = QtWidgets.QWidget(GiaiMaWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 47, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/HAMATASURIMA/Desktop/HYde (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_GiaiMa = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GiaiMa.setGeometry(QtCore.QRect(250, 170, 75, 31))
        self.pushButton_GiaiMa.setObjectName("pushButton_GiaiMa")
        self.Text_File = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_File.setGeometry(QtCore.QRect(140, 100, 311, 31))
        self.Text_File.setObjectName("Text_File")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 51, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(490, 100, 75, 31))
        self.pushButton_file.setObjectName("pushButton_file")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(510, 240, 75, 31))
        self.pushButton_back.setObjectName("pushButton_back")
        GiaiMaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GiaiMaWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        GiaiMaWindow.setMenuBar(self.menubar)

        self.retranslateUi(GiaiMaWindow)
        QtCore.QMetaObject.connectSlotsByName(GiaiMaWindow)

    def retranslateUi(self, GiaiMaWindow):
        _translate = QtCore.QCoreApplication.translate
        GiaiMaWindow.setWindowTitle(_translate("GiaiMaWindow", "MainWindow"))
        self.label.setText(_translate("GiaiMaWindow", "HỢP ĐỒNG ĐIỆN TỬ"))
        self.pushButton_GiaiMa.setText(_translate("GiaiMaWindow", "Giải mã"))
        self.label_4.setText(_translate("GiaiMaWindow", "File giải mã"))
        self.pushButton_file.setText(_translate("GiaiMaWindow", "Chọn file"))
        self.pushButton_back.setText(_translate("GiaiMaWindow", "TRỞ VỀ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GiaiMaWindow = QtWidgets.QMainWindow()
    ui = Ui_GiaiMaWindow()
    ui.setupUi(GiaiMaWindow)
    GiaiMaWindow.show()
    sys.exit(app.exec_())
