from PyQt5.QtWidgets import*
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class NewGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000,800)
        #Playbutton
        self.PlayButton = QPushButton(self)
        self.PlayButton.setGeometry(QRect(600,650,200,50))
        self.PlayButton.setStyleSheet("QPushButton{background-color:rgb(82,204, 206);border-radius:25px ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border-radius:25px ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.PlayButton.setText("PLAY")
        #Backbutton
        self.BackButton = QPushButton(self)
        self.BackButton.setGeometry(QRect(200, 650, 200, 50))
        self.BackButton.setText("Back")
        self.BackButton.setStyleSheet("QPushButton{background-color:rgb(82,204, 206);border-radius:25px ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border-radius:25px ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")

        self.mode_button =  QPushButton(self)
        self.mode_button.setGeometry(QRect(400,200,200,50))
        self.mode_button.setStyleSheet("QPushButton{background-color:rgb(82,204, 206) ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108) ;border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.mode_button.clicked.connect(self.change_mode)
        #difficult button
        self.difficult_button = QPushButton(self)
        self.difficult_button.setGeometry(QRect(400,300,200,50))
        self.difficult_button.setStyleSheet("QPushButton{background-color:rgb(82,204, 206) ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.difficult_button.clicked.connect(self.change_diff)
        #Option Button
        self.option_button = QPushButton(self)
        self.option_button.setGeometry(QRect(400,400,200,50))
        self.option_button.setStyleSheet("QPushButton{background-color:rgb(82,204, 206) ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.option_button.clicked.connect(self.change_option)
        #Custom
        self.Custom_button = QPushButton(self)
        self.Custom_button.setGeometry(QRect(400,500,200,50))
        self.Custom_button.setStyleSheet("QPushButton{background-color:rgb(82,204, 206) ;border: 3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}\n QPushButton:hover{background-color: rgb(3, 57, 108);border :3px solid green;color:white;font: bold 10pt \"MS Shell Dlg 2\"}")
        self.Custom_button.setText("Custom")
        self.Custom_button.clicked.connect(self.Custom_window)

        self.mode_list = ["Player","Bot"]
        self.mode_key_list = ["not_auto","auto"]
        self.mode_index = 0
        self.mode = self.mode_key_list[self.mode_index]
        self.mode_button.setText("Mode: Player")

        self.difficult_list = ["easy","medium","hard"]
        self.difficult_index = 0
        self.difficult = self.difficult_list[self.difficult_index]
        self.difficult_button.setText("Difficult: Easy")

        self.options_list = ["Random","Not Random"]
        self.option_index = 0
        self.optionKey = [False,True]
        self.option = self.optionKey[self.option_index]
        self.option_button.setText("Option: Random")




        self.prew_button1 = QPushButton(self)
        self.prew_button1.setGeometry(QRect(200-50,530,30,30))
        self.current_index = 0
        self.prew_button1.clicked.connect(self.change_Player_Prew)

        self.next_button1 = QPushButton(self)
        self.next_button1.setGeometry(QRect(370-50,530,30,30))
        self.next_button1.clicked.connect(self.change_Player_Next)

        self.list_image = []
        self.setList_image()
        # skin_list

        self.current_index = 0
        self.skin = self.list_image[self.current_index]["Player"]
        QIcon1 = QIcon()
        QIcon1.addFile("Do_an/Image/Image/prew.png")
        self.prew_button1.setIcon(QIcon1)
        #self.change_button1.hide()
        QIcon2 = QIcon()
        QIcon2.addFile("Do_an/Image/Image/next.png")
        self.next_button1.setIcon(QIcon2)
        self.next_button1.setStyleSheet("background-color:None;")
        #self.change_button2.hide()

        # display skin
        self.skin_display = QLabel(self)
        self.skin_display.setGeometry(QRect(100, 220, 300, 300))
        self.skin_display.setStyleSheet("border:2px solid black")
        self.skin_display.setPixmap(QPixmap(self.list_image[0]["path"]))
        #Player_Label
        self.Player_Label = QLabel(self)
        self.Player_Label.setGeometry(QRect(150,150,200,50))
        self.Player_Label.setStyleSheet("font: 16pt \"Segoe Print\"")
        self.Player_Label.setAlignment(Qt.AlignCenter)
        self.Player_Label.setText("Player")
        #skin name
        self.skin_name = QLabel(self)
        self.skin_name.setGeometry(QRect(220-30,530,120,30))
        self.skin_name.setText(self.skin)
        self.skin_name.setStyleSheet("font: 8pt \"Segoe Print\";")
        self.skin_name.setAlignment(Qt.AlignCenter)
        #Map Display
        self.Map_display = QLabel(self)
        self.Map_display.setGeometry(QRect(600, 220, 300, 300))
        self.Map_display.setStyleSheet("border:1px solid black")
        #Map Label
        self.Map_Label = QLabel(self)
        self.Map_Label.setGeometry(QRect(650,150,200,50))
        self.Map_Label.setStyleSheet("font: 16pt \"Segoe Print\"")
        self.Map_Label.setAlignment(Qt.AlignCenter)
        self.Map_Label.setText("Map")
        # Map_list
        self.Map_list = []
        self.MapIndex = 0
        self.setMap_List()
        self.Map = self.Map_list[self.MapIndex]["Map"]
        self.Map_display.setPixmap(QPixmap(self.Map_list[self.MapIndex]["path"]))
        #Map_name
        self.Map_name = QLabel(self)
        self.Map_name.setGeometry(QRect(620+50+20, 530, 120, 30))
        self.Map_name.setText(self.Map)
        self.Map_name.setStyleSheet(
            "font: 8pt \"Segoe Print\";")
        self.Map_name.setAlignment(Qt.AlignCenter)


        self.prew_button2 = QPushButton(self)
        self.prew_button2.setGeometry(QRect(600+50, 530, 30, 30))

        self.prew_button2.clicked.connect(self.change_Map_Prew)
        self.prew_button2.setIcon(QIcon1)

        self.next_button2 = QPushButton(self)
        self.next_button2.setGeometry(QRect(770+50, 530, 30, 30))
        self.next_button2.clicked.connect(self.change_Map_Next)
        self.next_button2.setIcon(QIcon2)
        



        self.Custom = False
        self.Off_Custom()
        #
    
    def set_skinList(self):
        skin1 = {"Name":"1","Path":"abc"}
        skin2 = {"Name":"2","Path":"abc"}
        skin3 = {"Name":"3","Path":"abc"}
        skin4 = {"Name":"4","Path":"abc"}
        self.skin_list = [skin1,skin2,skin3,skin4]

    def Off_Custom(self):
        self.skin_display.hide()
        self.Map_display.hide()
        self.prew_button1.hide()
        self.prew_button2.hide()
        self.next_button1.hide()
        self.next_button2.hide()
        self.Player_Label.hide()
        self.Map_name.hide()
        self.Map_Label.hide()
        self.skin_name.hide()
        self.mode_button.show()
        self.difficult_button.show()
        self.option_button.show()
        self.Custom_button.show()
    def setMap_List(self):
        a1 = 'Do_an/Image/Image/Map/green.png'
        a2 = 'Do_an/Image/Image/Map/grey.png'
        a3 = 'Do_an/Image/Image/Map/blue.png'
        a4 = 'Do_an/Image/Image/Map/brown.png'
        a5 = 'Do_an/Image/Image/Map/red.png'
        a6 = 'Do_an/Image/Image/Map/Yellow.png'
        A = [a1,a2,a3,a4,a5,a6]
        Map = ["green","grey","blue","brown","red","yellow"]

        self.Map_list = [{"path":A[i],"Map":Map[i]} for i in range(6)]
    def setList_image(self):
        a1 = "Do_an/Image/Image/Player/square.png"
        a2 = "Do_an/Image/Image/Player/MaskDude.png"
        a3 = "Do_an/Image/Image/Player/Tom.png"
        a4 = "Do_an/Image/Image/Player/Frog.png"
        a5 = "Do_an/Image/Image/Player/Blueman.png"
        A = [a1,a2,a3,a4,a5]
        name = ["Default","MaskDude","Tom","Frog","Blueman"]
        List1 = [{"path":A[i],"Player":name[i]} for i in range(5)]
        self.list_image = List1
    def change_Player_Next(self):
        self.current_index = (self.current_index+1)%5
        self.skin_display.setPixmap(QPixmap(self.list_image[self.current_index]["path"]))
        self.skin = self.list_image[self.current_index]["Player"]
        self.skin_name.setText(self.skin)
    def change_Player_Prew(self):
        self.current_index = (self.current_index-1)%5
        self.skin_display.setPixmap(QPixmap(self.list_image[self.current_index]["path"]))
        self.skin = self.list_image[self.current_index]["Player"]
        self.skin_name.setText(self.skin)
    def change_Map_Prew(self):
        self.MapIndex = (self.MapIndex-1)%6
        self.Map_display.setPixmap(QPixmap(self.Map_list[self.MapIndex]["path"]))
        self.Map = self.Map_list[self.MapIndex]["Map"]
        self.Map_name.setText(self.Map)


    def change_Map_Next(self):
        self.MapIndex = (self.MapIndex+1)%6
        self.Map_display.setPixmap(QPixmap(self.Map_list[self.MapIndex]["path"]))
        self.Map = self.Map_list[self.MapIndex]["Map"]
        self.Map_name.setText(self.Map)

    def change_mode(self):
        self.mode_index = (self.mode_index+1)%2
        self.mode_button.setText("Mode: "+self.mode_list[self.mode_index])
        self.mode = self.mode_key_list[self.mode_index]
        if(self.mode == "auto"):
            self.Custom_button.hide()
        else:
            self.Custom_button.show()
    def change_diff(self):
        self.difficult_index = (self.difficult_index+1)%3
        self.difficult_button.setText("Difficult: "+self.difficult_list[self.difficult_index])
        self.difficult = self.difficult_list[self.difficult_index]
    def change_option(self):
        self.option_index = (self.option_index+1)%2
        self.option_button.setText("Option: "+self.options_list[self.option_index])
        self.option = self.optionKey[self.option_index]
    def Custom_window(self):
        self.Custom = True
        self.mode_button.hide()
        self.difficult_button.hide()
        self.option_button.hide()
        self.Custom_button.hide()
        self.skin_display.show()
        self.Map_display.show()
        self.prew_button1.show()
        self.prew_button2.show()
        self.next_button1.show()
        self.next_button2.show()
        self.skin_name.show()
        self.Player_Label.show()
        self.Map_Label.show()
        self.Map_name.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = NewGame()
    login.show()
    sys.exit(app.exec_())