from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class AboutWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        # ABOUT LABEL
        self.About_Label = QLabel(self)
        self.About_Label.setGeometry(400,100,200,60)
        self.About_Label.setText("ABOUT")
        self.About_Label.setAlignment(Qt.AlignCenter)
        self.About_Label.setStyleSheet("font: bold 40pt \"Freestyle Script\"")
        # Label1
        self.Label1 = QLabel(self)
        self.Label1.setGeometry(QRect(270,200,460,60))
        self.Label1.setText("<html><head/><body><p align=\"center\">Đoàn Quang Thắng: 23122051</p></body></html>")
        self.Label1.setStyleSheet("font: bold 16pt \"Constantia\"")
        #Label 2
        self.Label2 = QLabel(self)
        self.Label2.setGeometry(QRect(270, 280, 460, 60))
        self.Label2.setText("<html><head/><body><p align=\"center\">Phan Ngọc Quân: 23122046</p></body></html>")
        self.Label2.setStyleSheet("font: bold 16pt \"Constantia\"")
        #Label 3
        self.Label3 = QLabel(self)
        self.Label3.setGeometry(QRect(270, 360, 460, 60))
        self.Label3.setText("<html><head/><body><p align=\"center\">Châu Văn Minh Khoa: 23122035</p></body></html>")
        self.Label3.setStyleSheet("font: bold 16pt \"Constantia\"")
        #Label 4
        self.Label4 = QLabel(self)
        self.Label4.setGeometry(QRect(270, 440, 480, 60))
        self.Label4.setText("<html><head/><body><p align=\"center\">Vũ Nguyễn Trung Hiếu: 23122028</p></body></html>")
        self.Label4.setStyleSheet("font: bold 16pt \"Constantia\"")
        #Label 5
        self.Label5 = QLabel(self)
        self.Label5.setGeometry(QRect(270, 520, 480, 60))
        self.Label5.setText("<html><head/><body><p align=\"center\">GVHD: Tùng Lê - Minh Nguyễn</p></body></html>")
        self.Label5.setStyleSheet("font: bold 16pt \"Constantia\"")
        #Back_Button
        Icon = QIcon()
        Icon.addFile('Do_an/Image/Icon/Back.webp')
        self.Back_Button = QPushButton(self)
        self.Back_Button.setGeometry(QRect(0, 0,100, 40))
        self.Back_Button.setIcon(Icon)
        self.Back_Button.setText("Back")
