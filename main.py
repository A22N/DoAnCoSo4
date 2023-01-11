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
from TraHopDong import *
from xulykey import RSA
import socket
import os
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

        self.TraHopDongWin = QMainWindow()
        self.TraHopDongUi = Ui_TraHopDongWin()
        self.TraHopDongUi.setupUi(self.TraHopDongWin)

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

        # nut o tra hop dong
        self.TraHopDongUi.pushButton_ImageHopDong.clicked.connect(
            self.hopdong)
        self.TraHopDongUi.pushButton_back.clicked.connect(self.back_pic1)
        self.TraHopDongUi.pushButton_next.clicked.connect(self.next_pic1)
        self.j = 0
        self.b = None
        self.TraHopDongUi.pushButton_trove.clicked.connect(self.Trovetrangchu8)

        # nút ở đăng ký
        self.DangKyUi.pushButton_Back.clicked.connect(self.Trovetrangchu3)
        self.DangKyUi.pushButton_dangky.clicked.connect(self.dangkytaikhoan)

        # nút ở trang chủ
        self.trangChuUI.dangXuatButton.clicked.connect(self.dangXuat)
        self.trangChuUI.pushButton_GuiHopDong.clicked.connect(self.TaoHopDong)
        # self.trangChuUI.pushButton_GiaiMa.clicked.connect(self.GiaiMa)
        self.trangChuUI.pushButton_NhanHopDong.clicked.connect(
            self.NhanHopDong)
        self.trangChuUI.pushButton_ShowHopDong.clicked.connect(
            self.ShowHopDong)

        # nút ở gửi hợp đồng
        self.HopDongUi.pushButton_file.clicked.connect(self.linkto_pic1)
        self.HopDongUi.pushButton_gui.clicked.connect(self.HopDong_result)
        self.HopDongUi.pushButton_back.clicked.connect(self.Trovetrangchu)
        self.HopDongUi.pushButton_back_2.clicked.connect(self.Trovetrangchu5)

        # nút ở giải mã
        self.GiaiMaUi.pushButton_back.clicked.connect(self.Trovetrangchu1)

        # nút ở nhận hợp đồng
        self.NhanHopDongUi.pushButton_Back.clicked.connect(self.Trovetrangchu2)
        self.NhanHopDongUi.pushButton.clicked.connect(self.chayserver)

    # nut o tra hop dong
    def ShowHopDong(self):
        self.trangChuWin.close()
        self.TraHopDongWin.show()

    def hopdong(self):
        files = QFileDialog.getOpenFileName(
            None, "", "", "Python Files (*.png), Text Files(*)")
        self.b = files[0]
        print(self.b)
        print(len(self.b))
        self.show_pic1(j=0)

    def show_pic1(self, j):
        self.TraHopDongUi.label_ManHinh.setPixmap(
            QtGui.QPixmap(self.b[j]))

    def back_pic1(self):
        if self.j > 0:
            self.j -= 1
            self.show_pic1(self.j)

    def next_pic1(self):
        if self.j < len(self.b)-1:
            self.j += 1
            self.show_pic1(self.j)

    def Trovetrangchu8(self):
        self.TraHopDongWin.close()
        self.trangChuWin.show()

    # nút ở đang đăng nhập
    def dangNhap(self):
        self.email = self.ui.Text_email.text()
        pass_email = self.ui.Text_pass.text()
        cursor = self.conx.cursor()
        die = 1
        for row in cursor.execute("select * from Account where email = ? and pass = ?", self.email, pass_email):
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
        dem = 0
        chuoi1 = ''
        for page in range(0, doc.page_count):
            extractedPage = doc.extract_pages(page, 1)
            extractedPage.save(f"{page + 1}.png")
            dem = dem + 1
            chuoi = str('D:/Ki_1_nam_3/DoAn4/') + str(dem) + '.png'
            chuoi1 += chuoi + " "
        files = chuoi1.split()
        print(files)
        self.a = files
        print(len(self.a))
        self.show_pic(i=0)
        self.dem2 = dem
        dem1 = dem
        for i in range(dem):
            chuoi2 = str('D:/Ki_1_nam_3/DoAn4/') + \
                str(dem1) + '.png'
            print(chuoi2)
            chuoi3 = str('D:/Ki_1_nam_3/DoAn4/data_nguoi_gui/files/data') + \
                str(dem1) + '.txt'
            print(chuoi3)
            with open(f"{chuoi2}", "rb") as image2string:
                converted_string = base64.b64encode(image2string.read())
            with open(f"{chuoi3}", "wb") as file:
                file.write(converted_string)
            dem1 = dem1 - 1

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

    # def GiaiMa(self):

    def NhanHopDong(self):
        self.trangChuWin.close()
        self.NhanHopDongWin.show()

    # nút ở gửi hợp đồng
    def Trovetrangchu5(self):
        self.HopDongWin.close()
        self.trangChuWin.show()

    def linkto_pic1(self):
        link = QFileDialog.getOpenFileName(filter='*.png')
        self.HopDongUi.label_ChuKy.setPixmap(QtGui.QPixmap(link[0]))
        with open("chuky.png", "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
        with open(r'D:\Ki_1_nam_3\DoAn4\data_nguoi_gui/files\chuky.txt', "wb") as file:
            file.write(converted_string)

    def HopDong_result(self):

        # ----------------client---------------
        cursor = self.conx.cursor()
        print(self.email)
        chay = 0
        for row in cursor.execute("select * from Account where email = ?", self.email):
            PORT = int(row.port)
            chay = 1
            print(PORT)
        if chay == 1:
            IP = "127.0.0.1"
            SIZE = 1024000
            FORMAT = "utf"
            CLIENT_FOLDER = "data_nguoi_gui"

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((IP, PORT))

            """ Folder path """
            path = os.path.join(CLIENT_FOLDER, "files")
            folder_name = path.split("/")[-1]

            """ Sending the folder name """
            msg = f"{folder_name}"
            print(f"[CLIENT] Sending folder name: {folder_name}")
            client.send(msg.encode(FORMAT))

            """ Receiving the reply from the server """
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}\n")

            """ Sending files """
            files = sorted(os.listdir(path))

            for file_name in files:
                """ Send the file name """
                msg = f"FILENAME:{file_name}"
                print(f"[CLIENT] Sending file name: {file_name}")
                client.send(msg.encode(FORMAT))

                """ Recv the reply from the server """
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")

                """ Send the data """
                file = open(os.path.join(path, file_name), "r")
                file_data = file.read()

                msg = f"DATA:{file_data}"
                client.send(msg.encode(FORMAT))
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")

                """ Sending the close command """
                msg = f"FINISH:Complete data send"
                client.send(msg.encode(FORMAT))
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")

            """ Closing the connection from the server """
            msg = f"CLOSE:File transfer is completed"
            client.send(msg.encode(FORMAT))

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Đã gửi được hợp đồng thành công!!!")
            msg.setWindowTitle("Thông báo")
            msg.exec_()
        dem1 = 3
        for i in range(3):
            chuoi2 = str('D:/Ki_1_nam_3/DoAn4/data_nguoi_nhan/data_nguoi_gui/files/data') + \
                str(dem1) + '.txt'
            print(chuoi2)
            chuoi3 = str('D:/Ki_1_nam_3/DoAn4/image_nguoi_nhan/') + \
                str(dem1) + '.png'

            file = open(f"{chuoi2}", "rb")
            byte = file.read()
            file.close()

            fh = open(f"{chuoi3}", "wb")
            fh.write(base64.b64decode((byte)))
            fh.close()
            dem1 = dem1 - 1
        dem3 = 3
        for i in range(3):
            chuoi4 = str('D:/Ki_1_nam_3/DoAn4/data_nguoi_gui/files/data') + \
                str(dem3) + '.txt'
            print(chuoi2)
            chuoi5 = str('D:/Ki_1_nam_3/DoAn4/image_nguoi_gui') + \
                str(dem3) + '.png'

            file = open(f"{chuoi4}", "rb")
            byte = file.read()
            file.close()

            fh = open(f"{chuoi5}", "wb")
            fh.write(base64.b64decode((byte)))
            fh.close()
            dem3 = dem3 - 1
        file = open(r'D:\Ki_1_nam_3\DoAn4\data_nguoi_gui\files\chuky.txt', "rb")
        byte = file.read()
        file.close()

        fh = open(r'D:\Ki_1_nam_3\DoAn4\image_nguoi_gui\chuky.png', "wb")
        fh.write(base64.b64decode((byte)))
        fh.close()

        file = open(
            r'D:\Ki_1_nam_3\DoAn4\data_nguoi_nhan\data_nguoi_gui\files\chuky.txt', "rb")
        byte = file.read()
        file.close()

        fh = open(r'D:\Ki_1_nam_3\DoAn4\image_nguoi_nhan\chuky.png', "wb")
        fh.write(base64.b64decode((byte)))
        fh.close()
        self.HopDongWin.hide()
        self.trangChuWin.show()

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
            port = int(row.port)
            chay = 1
            print(port)
        if chay == 1:
            IP = "127.0.0.1"
            PORT = int(port)
            SIZE = 1024000
            FORMAT = "utf"
            SERVER_FOLDER = "data_nguoi_nhan"
            print("[STARTING] Server is starting.\n")
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((IP, PORT))
            server.listen()
            print("[LISTENING] Server is waiting for clients.")

            while True:
                conn, addr = server.accept()
                print(f"[NEW CONNECTION] {addr} connected.\n")

                """ Receiving the folder_name """
                folder_name = conn.recv(SIZE).decode(FORMAT)

                """ Creating the folder """
                folder_path = os.path.join(SERVER_FOLDER, folder_name)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    conn.send(
                        f"Folder ({folder_name}) created.".encode(FORMAT))
                else:
                    conn.send(
                        f"Folder ({folder_name}) already exists.".encode(FORMAT))

                """ Receiving files """
                while True:
                    msg = conn.recv(SIZE).decode(FORMAT)
                    cmd, data = msg.split(":")

                    if cmd == "FILENAME":
                        """ Recv the file name """
                        print(f"[CLIENT] Received the filename: {data}.")

                        file_path = os.path.join(folder_path, data)
                        file = open(file_path, "w")
                        conn.send("Filename received.".encode(FORMAT))

                    elif cmd == "DATA":
                        """ Recv data from client """
                        print(f"[CLIENT] Receiving the file data.")
                        file.write(data)
                        conn.send("File data received".encode(FORMAT))

                    elif cmd == "FINISH":
                        file.close()
                        print(f"[CLIENT] {data}.\n")
                        conn.send("The data is saved.".encode(FORMAT))

                    elif cmd == "CLOSE":
                        print(f"[CLIENT] {data}")
                        break

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Đã nhận được hợp đồng!!!")
                msg.setWindowTitle("Thông báo")
                msg.exec_()
        dem1 = 3
        for i in range(3):
            chuoi2 = str('D:/Ki_1_nam_3/DoAn4/data_nguoi_nhan/data_nguoi_gui/files/data') + \
                str(dem1) + '.txt'
            print(chuoi2)
            chuoi3 = str('D:/Ki_1_nam_3/DoAn4/image_nguoi_nhan/') + \
                str(dem1) + '.png'

            file = open(f"{chuoi2}", "rb")
            byte = file.read()
            file.close()

            fh = open(f"{chuoi3}", "wb")
            fh.write(base64.b64decode((byte)))
            fh.close()
            dem1 = dem1 - 1
        dem3 = 3
        for i in range(3):
            chuoi4 = str('D:/Ki_1_nam_3/DoAn4/data_nguoi_gui/files/data') + \
                str(dem3) + '.txt'
            print(chuoi2)
            chuoi5 = str('D:/Ki_1_nam_3/DoAn4/image_nguoi_gui') + \
                str(dem3) + '.png'

            file = open(f"{chuoi4}", "rb")
            byte = file.read()
            file.close()

            fh = open(f"{chuoi5}", "wb")
            fh.write(base64.b64decode((byte)))
            fh.close()
            dem3 = dem3 - 1
        file = open(r'D:\Ki_1_nam_3\DoAn4\data_nguoi_gui\files\chuky.txt', "rb")
        byte = file.read()
        file.close()

        fh = open(r'D:\Ki_1_nam_3\DoAn4\image_nguoi_gui\chuky.png', "wb")
        fh.write(base64.b64decode((byte)))
        fh.close()

        file = open(
            r'D:\Ki_1_nam_3\DoAn4\data_nguoi_nhan\data_nguoi_gui\files\chuky.txt', "rb")
        byte = file.read()
        file.close()

        fh = open(r'D:\Ki_1_nam_3\DoAn4\image_nguoi_nhan\chuky.png', "wb")
        fh.write(base64.b64decode((byte)))
        fh.close()
        print("ok")
        cursor = self.conx.cursor()
        email = self.NhanHopDongUi.Text_Port.text()
        for row in cursor.execute("select * from Account where email = ?", email):
            port = int(row.port)
            chay = 1
            print(port)
        self.HopDongWin.close()
        self.HopDongWin.show()
        print("ok")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = Main()
    m.show()

    sys.exit(app.exec_())
