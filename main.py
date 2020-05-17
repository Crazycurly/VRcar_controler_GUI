import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from  Ui_main import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.but)
    def but(self):
        print("test")
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())