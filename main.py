import sys
import cv2

from  Ui_main import *
from PyQt5.QtWidgets import  QWidget, QLabel, QApplication,QMainWindow
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.but_start.clicked.connect(self.start)
        self.but_stop.clicked.connect(self.stop)

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.mjpeg_label.setPixmap(QPixmap.fromImage(image))

    def start(self):
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.th.start()

    def stop(self):
        self.th.stop()
        
class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    state = True
    def run(self):
        cap = cv2.VideoCapture(0)
        while self.state:
            ret, frame = cap.read()
            if ret:
                self.set_image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        cap.release()
        self.set_image(cv2.imread('test.jpg'))
        
    def set_image(self,img):
        h, w, ch = img.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)

    def stop(self):
        self.state = False


if __name__=="__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())