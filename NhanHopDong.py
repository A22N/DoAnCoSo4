# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NhanHopDong.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NhanHopDongWindow(object):
    def setupUi(self, NhanHopDongWindow):
        NhanHopDongWindow.setObjectName("NhanHopDongWindow")
        NhanHopDongWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(NhanHopDongWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 47, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("image/HYde (1).png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Back.setGeometry(QtCore.QRect(320, 140, 75, 31))
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 70, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_xacnhan = QtWidgets.QLabel(self.centralwidget)
        self.label_xacnhan.setGeometry(QtCore.QRect(50, 132, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_xacnhan.setFont(font)
        self.label_xacnhan.setText("")
        self.label_xacnhan.setObjectName("label_xacnhan")
        self.Text_Port = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_Port.setGeometry(QtCore.QRect(100, 70, 211, 31))
        self.Text_Port.setObjectName("Text_Port")
        NhanHopDongWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NhanHopDongWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        NhanHopDongWindow.setMenuBar(self.menubar)

        self.retranslateUi(NhanHopDongWindow)
        QtCore.QMetaObject.connectSlotsByName(NhanHopDongWindow)

    def retranslateUi(self, NhanHopDongWindow):
        _translate = QtCore.QCoreApplication.translate
        NhanHopDongWindow.setWindowTitle(_translate("NhanHopDongWindow", "MainWindow"))
        self.label_5.setText(_translate("NhanHopDongWindow", "MOON.eContract"))
        self.pushButton_Back.setText(_translate("NhanHopDongWindow", "TRỞ VỀ"))
        self.label.setText(_translate("NhanHopDongWindow", "Địa Chỉ"))
        self.pushButton.setText(_translate("NhanHopDongWindow", "Nhận"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NhanHopDongWindow = QtWidgets.QMainWindow()
    ui = Ui_NhanHopDongWindow()
    ui.setupUi(NhanHopDongWindow)
    NhanHopDongWindow.show()
    sys.exit(app.exec_())
