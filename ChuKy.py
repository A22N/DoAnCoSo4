# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChuKy.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChuKyWin(object):
    def setupUi(self, ChuKyWin):
        ChuKyWin.setObjectName("ChuKyWin")
        ChuKyWin.resize(599, 460)
        self.centralwidget = QtWidgets.QWidget(ChuKyWin)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(490, 340, 75, 31))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_ChuKy = QtWidgets.QLabel(self.centralwidget)
        self.label_ChuKy.setGeometry(QtCore.QRect(140, 180, 311, 191))
        self.label_ChuKy.setFrameShape(QtWidgets.QFrame.Box)
        self.label_ChuKy.setLineWidth(2)
        self.label_ChuKy.setText("")
        self.label_ChuKy.setScaledContents(True)
        self.label_ChuKy.setObjectName("label_ChuKy")
        self.Text_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_2.setGeometry(QtCore.QRect(140, 120, 311, 31))
        self.Text_2.setObjectName("Text_2")
        self.pushButton_gui = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gui.setGeometry(QtCore.QRect(240, 390, 75, 31))
        self.pushButton_gui.setObjectName("pushButton_gui")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 51, 21))
        self.label_3.setObjectName("label_3")
        self.Text = QtWidgets.QLineEdit(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(140, 60, 311, 31))
        self.Text.setObjectName("Text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 250, 41, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 47, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("image/HYde (1).png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_back_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back_2.setGeometry(QtCore.QRect(520, 400, 75, 31))
        self.pushButton_back_2.setObjectName("pushButton_back_2")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(490, 260, 75, 31))
        self.pushButton_file.setObjectName("pushButton_file")
        ChuKyWin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChuKyWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 21))
        self.menubar.setObjectName("menubar")
        ChuKyWin.setMenuBar(self.menubar)

        self.retranslateUi(ChuKyWin)
        QtCore.QMetaObject.connectSlotsByName(ChuKyWin)

    def retranslateUi(self, ChuKyWin):
        _translate = QtCore.QCoreApplication.translate
        ChuKyWin.setWindowTitle(_translate("ChuKyWin", "MainWindow"))
        self.pushButton_back.setText(_translate("ChuKyWin", "TR??? V???"))
        self.pushButton_gui.setText(_translate("ChuKyWin", "G???I"))
        self.label_3.setText(_translate("ChuKyWin", "Ti??u ?????"))
        self.label.setText(_translate("ChuKyWin", "H???P ?????NG ??I???N T???"))
        self.label_2.setText(_translate("ChuKyWin", "G???i ?????n"))
        self.label_4.setText(_translate("ChuKyWin", "Ch??? K??"))
        self.pushButton_back_2.setText(_translate("ChuKyWin", "THO??T"))
        self.pushButton_file.setText(_translate("ChuKyWin", "Ch???n file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChuKyWin = QtWidgets.QMainWindow()
    ui = Ui_ChuKyWin()
    ui.setupUi(ChuKyWin)
    ChuKyWin.show()
    sys.exit(app.exec_())
