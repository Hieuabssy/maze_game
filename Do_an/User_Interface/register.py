from PyQt5 import QtGui
from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
import sys
class RegisterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        # background
        self.background = QLabel(self)
        self.background.setGeometry(QRect(0, 0, 1000, 800))
        self.background.setPixmap(QtGui.QPixmap("Do_an/Image/blue1.png"))

        # Label
        self.label = QLabel(self)
        self.label.setGeometry(200, 50, 600, 100)
        self.label.setStyleSheet(
            "font: 32pt \"Segoe Print\";\n"
            "border-radius:0px")
        self.label.setText("REGISTER")
        self.label.setAlignment(Qt.AlignCenter)
        # Icon
        # pass_icon = QIcon()
        # user_icon = QIcon()
        # pass_icon.addFile('icon/password.jpg')
        # user_icon.addFile('icon/username.jpg')
        # self.pass_icon_button = QPushButton(self)
        # self.user_icon_button = QPushButton(self)
        # self.user_icon_button.setGeometry(QRect(50, 310, 40, 40))
        # self.pass_icon_button.setGeometry(QRect(50, 380, 40, 40))
        # self.user_icon_button.setIcon(user_icon)
        # self.pass_icon_button.setIcon(pass_icon)
        # login button
        self.sign_up_button = QPushButton(self)
        self.sign_up_button.setGeometry(QRect(380, 450, 240, 40))
        self.sign_up_button.setStyleSheet(
            u"background-color:rgb(82,204, 206);\n"
            "border-radius:10px;column-gap: 5px;\n"
            "border :2px solid yellow;\n"
            "font: bold 8pt \"Segoe Print\";"
        )
        #qradialgradient(cx: 0.1, cy: 0.2, radius: 1, fx: 1, fy: 1, stop: 0 rgba(97, 186, 255, 255), stop: 0.901 rgba(166, 239, 253, 255))
        self.sign_up_button.setText("SIGN UP")
        # LOG IN Button
        self.login_button = QPushButton(self)
        self.login_button.setObjectName(u"pushButton_3")
        self.login_button.setGeometry(QRect(460 + 100, 510, 80, 40))
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        style = 0
        self.login_button.setStyleSheet("font: 75 10pt \"Segoe Print\";text-decoration: underline;border: 0px")
        self.login_button.setText("Login")
        # create "Dont have an account ?"
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(260 + 100, 510, 200, 40))
        self.label_2.setStyleSheet("font: 9pt \"Segoe Print\";border :0px solid black")
        self.label_2.setText("Already have an account?")
        # User_name
        self.User_name = QLineEdit(self)
        self.User_name.setObjectName(u"lineEdit")
        self.User_name.setGeometry(QRect(290 + 100, 260, 220, 40))
        self.User_name.setStyleSheet(u"border:1px solid black;\n"
                                     "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                     "background-color:rgba(39, 89, 245, 0.13);font: 10pt \"Segoe Script\";")
        self.User_name.setPlaceholderText("username")
        # password
        self.Password = QLineEdit(self)
        self.Password.setObjectName(u"lineEdit_2")
        self.Password.setGeometry(QRect(290 + 100, 340, 220, 40))
        self.Password.setStyleSheet(u"border:1px solid black;\n"
                                    "border-bottom:2px solid rgba(105, 118, 132, 255);\n"
                                    "background-color:rgba(39, 89, 245, 0.13);font: 10pt \"Segoe Script\";")
        self.Password.setPlaceholderText("password")
        self.Password.setEchoMode(QLineEdit.Password)

        self.acc_icon = QIcon("Do_an/Image/Icon/username.jpg")
        self.pass_icon = QIcon("Do_an/Image/Icon/password.jpg")
        #
        self.accButton = QPushButton(self)
        self.accButton.setGeometry(QRect(350,260,40,40))
        self.accButton.setIcon(self.acc_icon)
        #
        self.PassButton = QPushButton(self)
        self.PassButton.setGeometry(QRect(350,340,40,40))
        self.PassButton.setIcon(self.pass_icon)
