# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaoHopDong.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaoHopDongWindow(object):
    def setupUi(self, TaoHopDongWindow):
        TaoHopDongWindow.setObjectName("TaoHopDongWindow")
        TaoHopDongWindow.resize(800, 703)
        TaoHopDongWindow.setStyleSheet("\n"
"QMainWindow{\n"
" border-image: url(:/background/image/Nen-xanh-duong-pastel.ng.jpg);\n"
"background-color: rgb(0, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(TaoHopDongWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_FileHopDong = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FileHopDong.setGeometry(QtCore.QRect(680, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_FileHopDong.setFont(font)
        self.pushButton_FileHopDong.setObjectName("pushButton_FileHopDong")
        self.pushButton_trove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_trove.setGeometry(QtCore.QRect(690, 630, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_trove.setFont(font)
        self.pushButton_trove.setObjectName("pushButton_trove")
        self.label_ManHinh = QtWidgets.QLabel(self.centralwidget)
        self.label_ManHinh.setGeometry(QtCore.QRect(10, 60, 641, 571))
        self.label_ManHinh.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ManHinh.setText("")
        self.label_ManHinh.setScaledContents(True)
        self.label_ManHinh.setObjectName("label_ManHinh")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(10, 640, 311, 31))
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(340, 640, 311, 31))
        self.pushButton_next.setObjectName("pushButton_next")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 47, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("image/HYde (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 111, 31))
        self.label.setObjectName("label")
        self.pushButton_GuHopDong = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GuHopDong.setGeometry(QtCore.QRect(680, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_GuHopDong.setFont(font)
        self.pushButton_GuHopDong.setObjectName("pushButton_GuHopDong")
        TaoHopDongWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TaoHopDongWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        TaoHopDongWindow.setMenuBar(self.menubar)

        self.retranslateUi(TaoHopDongWindow)
        QtCore.QMetaObject.connectSlotsByName(TaoHopDongWindow)

    def retranslateUi(self, TaoHopDongWindow):
        _translate = QtCore.QCoreApplication.translate
        TaoHopDongWindow.setWindowTitle(_translate("TaoHopDongWindow", "MainWindow"))
        self.pushButton_FileHopDong.setText(_translate("TaoHopDongWindow", "FILE HỢP ĐỒNG"))
        self.pushButton_trove.setText(_translate("TaoHopDongWindow", "TRỞ VỀ"))
        self.pushButton_back.setText(_translate("TaoHopDongWindow", "<"))
        self.pushButton_next.setText(_translate("TaoHopDongWindow", ">"))
        self.label.setText(_translate("TaoHopDongWindow", "HỢP ĐỒNG ĐIỆN TỬ"))
        self.pushButton_GuHopDong.setText(_translate("TaoHopDongWindow", "BƯỚC 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaoHopDongWindow = QtWidgets.QMainWindow()
    ui = Ui_TaoHopDongWindow()
    ui.setupUi(TaoHopDongWindow)
    TaoHopDongWindow.show()
    sys.exit(app.exec_())
