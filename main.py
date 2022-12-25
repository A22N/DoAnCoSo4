import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from DangNhap import *
from DangKy import *
from trangchu import *
from GuiHopDong import *
from GiaiMaHopDong import *
from NhanHopDong import *
from TaoHopDong import *
from xulykey import RSA
import socket
import pyodbc
import random
import aspose.words as aw
from PIL import Image
import base64


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DangNhapWindow()
        self.ui.setupUi(self)
        self.conx = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};\
        SERVER=LAPTOP-46CK9SKG; Database=hopdong_Account;\
            UID=nguyenan123; PWD=123;')

        self.trangChuWin = QMainWindow()
        self.trangChuUI = Ui_TrangChuWindow()
        self.trangChuUI.setupUi(self.trangChuWin)

        self.TaoHopDongWin = QMainWindow()
        self.TaoHopDongUI = Ui_TaoHopDongWindow()
        self.TaoHopDongUI.setupUi(self.TaoHopDongWin)

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

        # nút tạo hợp đồng
        self.TaoHopDongUI.pushButton_trove.clicked.connect(self.Trovetrangchu4)
        self.TaoHopDongUI.pushButton_FileHopDong.clicked.connect(
            self.linkto_pic)
        self.TaoHopDongUI.pushButton_back.clicked.connect(self.back_pic)
        self.TaoHopDongUI.pushButton_next.clicked.connect(self.next_pic)
        self.i = 0
        self.a = None
        self.TaoHopDongUI.pushButton_GuHopDong.clicked.connect(self.GuiHopDong)

        # nút ở đang đăng nhập
        self.ui.pushButton_login.clicked.connect(self.dangNhap)
        self.ui.pushButton_register.clicked.connect(self.dangky)

        # nút ở đăng ký
        self.DangKyUi.pushButton_Back.clicked.connect(self.Trovetrangchu3)
        self.DangKyUi.pushButton_dangky.clicked.connect(self.dangkytaikhoan)

        # nút ở trang chủ
        self.trangChuUI.dangXuatButton.clicked.connect(self.dangXuat)
        self.trangChuUI.pushButton_GuiHopDong.clicked.connect(self.TaoHopDong)
        self.trangChuUI.pushButton_GiaiMa.clicked.connect(self.GiaiMa)
        self.trangChuUI.pushButton_NhanHopDong.clicked.connect(
            self.NhanHopDong)

        # nút ở gửi hợp đồng
        self.HopDongUi.pushButton_file.clicked.connect(self.linkto_pic1)
        self.HopDongUi.pushButton_gui.clicked.connect(self.HopDong_result)
        self.HopDongUi.pushButton_back.clicked.connect(self.Trovetrangchu)

        # nút ở giải mã
        self.GiaiMaUi.pushButton_back.clicked.connect(self.Trovetrangchu1)

        # nút ở nhận hợp đồng
        self.NhanHopDongUi.pushButton_Back.clicked.connect(self.Trovetrangchu2)
        self.NhanHopDongUi.pushButton.clicked.connect(self.chayserver)

    # nút ở đang đăng nhập
    def dangNhap(self):
        email = self.ui.Text_email.text()
        pass_email = self.ui.Text_pass.text()
        cursor = self.conx.cursor()
        die = 1
        for row in cursor.execute("select * from Account where email = ? and pass = ?", email, pass_email):
            self.trangChuWin.show()
            self.hide()
            die = 0
        if die == 1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Tài khoản không hợp lệ!!!")
            msg.exec_()

    def dangky(self):
        self.trangChuWin.close()
        self.DangKyWin.show()
    # nút ở đăng ký

    def Trovetrangchu3(self):
        self.DangKyWin.close()
        self.show()

    def dangkytaikhoan(self):
        doanh_nghiep = self.DangKyUi.Text_doanhnghiep.text()
        ma_so_thue = self.DangKyUi.Text_masothue.text()
        ho_ten = self.DangKyUi.Text_hoten.text()
        sdt = self.DangKyUi.Text_sdt.text()
        email = self.DangKyUi.Text_email.text()
        pass_email = self.DangKyUi.Text_pass.text()
        port1 = random.randint(30000, 99999)
        cursor = self.conx.cursor()
        die = 1
        for row in cursor.execute("select * from Account where doanh_nghiep = ? and ma_so_thue = ? and ho_va_ten = ? and sdt = ? and email = ? and pass = ?", doanh_nghiep, ma_so_thue, ho_ten, sdt, email, pass_email):
            die = 2
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Tài khoản không hợp lệ!!!")
            msg.exec_()
        if die == 1:
            cursor.execute("insert Account values (?,?,?,?,?,?,?)",
                           doanh_nghiep, ma_so_thue, ho_ten, sdt, email, pass_email, port1)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Tài khoản đăng ký thành công !!!")
            msg.exec_()
        self.conx.commit()

    # nut o tao hop dong
    def Trovetrangchu4(self):
        self.TaoHopDongWin.close()
        self.trangChuWin.show()

    def linkto_pic(self):

        link = QFileDialog.getOpenFileName(filter='*.doc *.docx')
        print(link[0])
        x = link[0].split("/// ", 1)
        print(x[0])
        doc = aw.Document(x[0])
        self.dem = 0
        chuoi1 = ''
        for page in range(0, doc.page_count):
            extractedPage = doc.extract_pages(page, 1)
            extractedPage.save(f"{page + 1}.png")
            self.dem = self.dem + 1
            chuoi = str('D:/Ki_1_nam_3/DoAn4/') + str(self.dem) + '.png'
            chuoi1 += chuoi + " "
        print(chuoi1.split())
        files = chuoi1.split()
        print(files)
        self.a = files
        print(len(self.a))
        self.show_pic(i=0)

    def show_pic(self, i):
        self.TaoHopDongUI.label_ManHinh.setPixmap(
            QtGui.QPixmap(self.a[i]))

    def back_pic(self):
        if self.i > 0:
            self.i -= 1
            self.show_pic(self.i)

    def next_pic(self):
        if self.i < len(self.a)-1:
            self.i += 1
            self.show_pic(self.i)

    def GuiHopDong(self):
        self.TaoHopDongWin.close()
        self.HopDongWin.show()

    # nút ở trang chủ

    def dangXuat(self):
        self.trangChuWin.close()
        self.show()

    def TaoHopDong(self):
        self.trangChuWin.close()
        self.TaoHopDongWin.show()

    def GiaiMa(self):
        self.trangChuWin.close()
        self.GiaiMaWin.show()

    def NhanHopDong(self):
        self.trangChuWin.close()
        self.NhanHopDongWin.show()

    # nút ở gửi hợp đồng

    def linkto_pic1(self):
        link = QFileDialog.getOpenFileName(filter='*.png')
        self.HopDongUi.label_ChuKy.setPixmap(QtGui.QPixmap(link[0]))

    def HopDong_result(self):
        for i in range(self.dem):
            tieude = self.HopDongUi.Text_2.text()
            with open("{self.dem}.png", "rb") as image2string:
                converted_string = base64.b64encode(image2string.read())
            with open('{self.dem}+ "_data".txt', "wb") as file:
                file.write(converted_string)

            f = open("tieude.txt", "w")
            f.write(tieude)
            f.close()

            print("ok")
            # ----------------client---------------
            cursor = self.conx.cursor()
            email = self.DangKyUi.Text_email.text()
            chay = 0
            for row in cursor.execute("select * from Account where email = ?", email):
                PORT = row.port
                chay = 1
            if chay == 1:
                IP = socket.gethostbyname(socket.gethostname())
                ADDR = (IP, PORT)
                FORMAT = "utf-8"
                SIZE = 1024

                # Chạy TCP socket
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Kết nối đến server
                client.connect(ADDR)

                # Mở đọc dữ liệu
                file = open("data/data.txt", "r")
                data = file.read()

                # Gửi file đến server
                client.send("data/data.txt".encode(FORMAT))
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER]: {msg}")

                # Truyền data đến server
                client.send(data.encode(FORMAT))
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER]: {msg}")

                file.close()

                print("ok")

    def linkto(self):
        link = QFileDialog.getOpenFileName(filter='*.doc *.docx')
        self.HopDongUi.Text_3.setText(link[0])

    def Trovetrangchu(self):
        self.HopDongWin.close()
        self.TaoHopDongWin.show()

    # nút ở giải mã
    def Trovetrangchu1(self):
        self.GiaiMaWin.close()
        self.trangChuWin.show()

    # nút ở nhận hợp đồng
    def Trovetrangchu2(self):
        self.NhanHopDongWin.close()
        self.trangChuWin.show()

    def chayserver(self):
        chay = 0
        cursor = self.conx.cursor()
        email = self.NhanHopDongUi.Text_Port.text()
        for row in cursor.execute("select * from Account where email = ?", email):
            PORT = row.port
            chay = 1
        if chay == 1:
            IP = socket.gethostbyname(socket.gethostname())
            ADDR = (IP, PORT)
            SIZE = 1024
            FORMAT = "utf-8"
            self.NhanHopDongUi.label_xacnhan = "Đang đợi..."

            print("[STARTING] Server is starting.")
            """ Staring a TCP socket. """
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            """ Bind the IP and PORT to the server. """
            server.bind(ADDR)

            """ Server is listening, i.e., server is now waiting for the client to connected. """
            server.listen()
            print("[LISTENING] Server is listening.")

            while True:
                """ Server has accepted the connection from the client. """
                conn, addr = server.accept()
                print(f"[NEW CONNECTION] {addr} connected.")

                """ Receiving the filename from the client. """
                filename = conn.recv(SIZE).decode(FORMAT)
                print(f"[RECV] Receiving the filename.")
                file = open(filename, "w")
                conn.send("Filename received.".encode(FORMAT))

                """ Receiving the file data from the client. """
                data = conn.recv(SIZE).decode(FORMAT)
                print(f"[RECV] Receiving the file data.")
                conn.send("File data received".encode(FORMAT))
                f = open("server_data/server_data.txt", "w")
                f.write(data)
                """ Closing the file. """
                f.close()

                """ Closing the connection from the client. """

                conn.close()
                print(f"[DISCONNECTED] {addr} disconnected.")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Đã nhận được hợp đồng!!!")
                msg.setWindowTitle("Thông báo")
                msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = Main()
    m.show()

    sys.exit(app.exec_())
