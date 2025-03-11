from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5 import QtMultimedia as M
from PyQt5.QtCore import QUrl

class Sound():
    def setUp(self):
        self.url_bg = QUrl.fromLocalFile("Do_an/sound/bg_music.mp3")
        self.content = M.QMediaContent(self.url_bg)
        self.background_sound = M.QMediaPlayer()
        self.background_sound.setMedia(self.content)
        self.background_sound.stateChanged.connect(self.handleStateChanged)

        self.url_click = QUrl.fromLocalFile("Do_an/sound/clickSound.mp3")
        self.content2 = M.QMediaContent(self.url_click)
        self.click_sound = M.QMediaPlayer()
        self.click_sound.setMedia(self.content2)

    def bgSound(self):
        self.background_sound.play()
    def pause_bgSound(self):
        self.background_sound.pause()

    #Hàm giúp lặp lại âm thanh nền
    def handleStateChanged(self, state):
        # Kiểm tra nếu âm thanh đã kết thúc
        if state == QMediaPlayer.StoppedState:
            # Phát lại âm thanh từ đầu
            self.background_sound.play()
    def clickSound(self):
        self.click_sound.play()

    

    