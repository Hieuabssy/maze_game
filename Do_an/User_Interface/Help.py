from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QSizePolicy, QMessageBox,
                             QFrame)
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import *
import sys
class HelpWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        #help label
        self.Help_label = QLabel(self)
        self.Help_label.setGeometry(400,100,200,60)
        self.Help_label.setText("HELP")
        self.Help_label.setAlignment(Qt.AlignCenter)
        self.Help_label.setStyleSheet("font: bold 40pt \"Freestyle Script\"")

        # Label1
        self.Label1 = QLabel(self)
        self.Label1.setGeometry(QRect(180,200,700, 120))
        self.Label1.setText("<html><head/><body><p align=\"center\">Hãy giúp chú mèo Tom của chúng ta lấy lại </p></body></html>")
        self.Label1.setStyleSheet("font: bold 16pt \"Constantia\"")

        # Label1
        self.Label2 = QLabel(self)
        self.Label2.setGeometry(QRect(180,260,700, 120))
        self.Label2.setText("<html><head/><body><p align=\"center\"> những chiếc phô mai bị Gia Huy cướp mất nhé! </p></body></html>")
        self.Label2.setStyleSheet("font: bold 16pt \"Constantia\"")
        
        #Label 2
        self.Label2 = QLabel(self)
        self.Label2.setGeometry(QRect(180, 340, 700, 120))
        self.Label2.setText("<html><head/><body><p align=\"center\">Sử dụng các phím W-A-S-D hoặc</p></body></html>")
        self.Label2.setStyleSheet("font: bold 16pt \"Constantia\"")

        #Label 3
        self.Label3 = QLabel(self)
        self.Label3.setGeometry(QRect(180, 400, 700, 120))
        self.Label3.setText("<html><head/><body><p align=\"center\">phím mũi tên để điều khiển nhân vật</p></body></html>")
        self.Label3.setStyleSheet("font: bold 16pt \"Constantia\"")


        #Label 4
        self.Label4 = QLabel(self)
        self.Label4.setGeometry(QRect(180, 480, 700, 120))
        self.Label4.setText("<html><head/><body><p align=\"center\">Nhấn H để hiển thị đường đi đến đích</p></body></html>")
        self.Label4.setStyleSheet("font: bold 16pt \"Constantia\"")

        #Label 5
        self.Label5 = QLabel(self)
        self.Label5.setGeometry(QRect(180, 540, 700, 120))
        self.Label5.setText("<html><head/><body><p align=\"center\">Nhấn SPACE để tạm dừng trò chơi</p></body></html>")
        self.Label5.setStyleSheet("font: bold 16pt \"Constantia\"")


        #Back_Button
        Icon = QIcon()
        Icon.addFile('Do_an/Image/Icon/Back.webp')
        self.Back_Button = QPushButton(self)
        self.Back_Button.setGeometry(QRect(0, 0,100, 40))
        self.Back_Button.setIcon(Icon)
        self.Back_Button.setText("Back")



