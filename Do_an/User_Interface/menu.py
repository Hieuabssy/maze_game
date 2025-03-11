from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from User_Interface.music import Sound
class MenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        # background
        self.background = QLabel(self)
        self.background.setGeometry(QRect(0, 0, 1000, 800))

        # Label
        self.label = QLabel(self)
        self.label.setGeometry(200, 100, 600, 100)
        self.label.setStyleSheet(
            "font: 32pt \"Segoe Print\";\n"
            "border-radius:0px")
        self.label.setText("MAZE GAME")
        self.label.setAlignment(Qt.AlignCenter)
        self.play_button, self.load_button,self.help_button,self.about_button,self.log_out_button,self.quit_button = self.button()
        #volume button
        self.Vol_on_icon = QIcon()
        self.Vol_on_icon.addFile("Do_an/image/Icon/volume_on.png")
        self.Vol_off_icon = QIcon()
        self.Vol_off_icon.addFile("Do_an/image/Icon/volume_off.webp")
        self.volume_button = QPushButton(self)
        self.volume_button.setGeometry(QRect(960,0,40,40))
        self.volume_button.setIcon(self.Vol_on_icon)
        self.Volume = False
        self.volume_button.clicked.connect(self.change_Vol)
        self.sound = Sound()
        self.sound.setUp()
        

    def button(self):
        play_button = QPushButton(self)
        load_button = QPushButton(self)
        help_button = QPushButton(self)
        about_button = QPushButton(self)
        quit_button = QPushButton(self)
        log_out_button = QPushButton(self)
        Button = [play_button,load_button,help_button,about_button,quit_button,log_out_button]
        Rect = [QRect(400, 280+i*70, 200, 50) for i in range(6)]
        Text = ["PLAY", "LOAD", "HELP", "ABOUT", "LOG OUT","QUIT"]
        for i in range(6):
            Button[i].setText(Text[i])
            Button[i].setGeometry(Rect[i])
            Button[i].setStyleSheet(u"QPushButton{\n"
    "border: 3px  solid green;border-radius:25px;\n"
    "background-color:rgb(82,204, 206);\n"
    "text-align:Center;\n"
    "color:White;\n"
    "font: bold 10pt \"MS Shell Dlg 2\";\n"
    "}\n"
    "QPushButton:hover{\n"
    "border: 3px  solid black;\n"
    "border-radius:25px;\n"
    "background-color: rgb(3, 57, 108);\n"
    "\n"
    "color:White;\n"
    "font: bold 10pt \"MS Shell Dlg 2\";text-align: Center;\n"
    "	\n"
    "}\n"
    "")
        return Button
    def change_Vol(self):
        if(self.Volume):
            self.volume_button.setIcon(self.Vol_off_icon)
            self.sound.pause_bgSound()
            self.Volume = False
        else:
            self.volume_button.setIcon(self.Vol_on_icon)
            self.sound.bgSound()
            self.Volume = True
    def off_volume(self):
        if(self.Volume):
            self.volume_button.setIcon(self.Vol_off_icon)
            self.sound.pause_bgSound()
            self.Volume = False

