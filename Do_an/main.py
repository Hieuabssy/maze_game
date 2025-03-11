from User_Interface.mainWindow import *
from game import *
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = MainWindow()
    login.show()
    sys.exit(app.exec_())
