import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from DangNhap import *
from DangKy import *
from trangchu import *
from GuiHopDong import *
from GiaiMaHopDong import *
from NhanHopDong import *
from xulykey import RSA
import docx2txt
# from client import *


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DangNhapWindow()
        self.ui.setupUi(self)

        self.trangChuWin = QMainWindow()
        self.trangChuUI = Ui_TrangChuWindow()
        self.trangChuUI.setupUi(self.trangChuWin)

        self.HopDongWin = QMainWindow()
        self.HopDongUi = Ui_HopDongWindow()
        self.HopDongUi.setupUi(self.HopDongWin)

        self.DangKyWin = QMainWindow()
        self.DangKyUi = Ui_DangKyWindow()
        self.DangKyUi.setupUi(self.DangKyWin)

        self.GiaiMaWin = QMainWindow()
        self.GiaiMaUi = Ui_GiaiMaWindow()
        self.GiaiMaUi.setupUi(self.GiaiMaWin)

        self.NhanHopDongWin = QMainWindow()
        self.NhanHopDongUi = Ui_NhanHopDongWindow()
        self.NhanHopDongUi.setupUi(self.NhanHopDongWin)

        # nút ở đang đăng nhập
        self.ui.pushButton_login.clicked.connect(self.dangNhap)
        self.ui.pushButton_register.clicked.connect(self.dangky)
        # nút ở trang chủ
        self.DangKyUi.pushButton_Back.clicked.connect(self.Trovetrangchu3)

        # nút ở trang chủ
        self.trangChuUI.dangXuatButton.clicked.connect(self.dangXuat)
        self.trangChuUI.pushButton_GuiHopDong.clicked.connect(self.TaoHopDong)
        self.trangChuUI.pushButton_GiaiMa.clicked.connect(self.GiaiMa)
        self.trangChuUI.pushButton_NhanHopDong.clicked.connect(
            self.NhanHopDong)

        # nút ở gửi hợp đồng
        self.HopDongUi.pushButton_file.clicked.connect(self.linkto)
        self.HopDongUi.pushButton_gui.clicked.connect(self.HopDong_result)
        self.HopDongUi.pushButton_back.clicked.connect(self.Trovetrangchu)

        # nút ở giải mã
        self.GiaiMaUi.pushButton_back.clicked.connect(self.Trovetrangchu1)

        # nút ở nhận hợp đồng
        self.NhanHopDongUi.pushButton_Back.clicked.connect(self.Trovetrangchu2)

    # nút ở đang đăng nhập
    def dangNhap(self):
        email = self.ui.Text_email.text()
        pass_email = self.ui.Text_pass.text()
        if email == "user" and pass_email == "123":
            self.trangChuWin.show()
            self.hide()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("This is a message box")
            msg.setInformativeText("This is additional information")
            msg.setWindowTitle("MessageBox demo")
            msg.setDetailedText("The details are as follows:")
            msg.exec_()

    def dangky(self):
        self.trangChuWin.close()
        self.DangKyWin.show()
    # nút ở đăng ký

    def Trovetrangchu3(self):
        self.DangKyWin.close()
        self.show()
    # nút ở trang chủ

    def dangXuat(self):
        self.trangChuWin.close()
        self.show()

    def TaoHopDong(self):
        self.trangChuWin.close()
        self.HopDongWin.show()

    def GiaiMa(self):
        self.trangChuWin.close()
        self.GiaiMaWin.show()

    def NhanHopDong(self):
        self.trangChuWin.close()
        self.NhanHopDongWin.show()

    # nút ở gửi hợp đồng

    def HopDong_result(self):
        self.rsa = RSA(keysize=32)

        msg = docx2txt.process(self.Text_3.text())
        email = self.Text.text()
        tieude = self.Text_2.text()

        enc = self.rsa.encrypt(msg)

        f = open("tieude.txt", "w")
        f.write(tieude)
        f.close()

        f = open("email.txt", "w")
        f.write(email)
        f.close()

        f = open("data/data.txt", "w")
        f.write(enc)
        f.close()
        print("ok")

        f = open("data/data.txt.txt", "a")
        f.write(" " + str(self.rsa.d))
        f.write(" " + str(self.rsa.N))
        f.close()

        # main_client()
        print("ok")

    def linkto(self):
        link = QFileDialog.getOpenFileName(filter='*.doc *.docx')
        self.Text_3.setText(link[0])

    def Trovetrangchu(self):
        self.HopDongWin.close()
        self.trangChuWin.show()

    # nút ở giải mã
    def Trovetrangchu1(self):
        self.GiaiMaWin.close()
        self.trangChuWin.show()

    # nút ở nhận hợp đồng
    def Trovetrangchu2(self):
        self.NhanHopDongWin.close()
        self.trangChuWin.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = Main()
    m.show()

    sys.exit(app.exec_())
