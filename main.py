import sys
import cv2
import requests

from Ui_main import *
from xinput import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.Qt import Qt


base_url = 'http://192.168.137.37'
angle = [90, 90]
move = 0
scale = 50.0

class MyWindow(Ui_Dialog, QtWidgets.QLabel):
    reSize = QtCore.pyqtSignal(QtCore.QSize)

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        global base_url
        self.setupUi(self)
        self.btn_start.clicked.connect(self.start)
        self.btn_stop.clicked.connect(self.stop)
        self.btn_gamepad.clicked.connect(self.gamepad)
        self.th = Thread(self)
        self.th.changePixmap.connect(self.setImage)
        self.reSize.connect(self.th.scaled)
        self.th.scaled(self.size())

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.mjpeg_label.setPixmap(QPixmap.fromImage(image))

    def start(self):
        self.th.start()

    def stop(self):
        self.th.stop()

    def resizeEvent(self, event):
        print(self.size())
        self.reSize.emit(self.size())

    def send_control(self, angle, d):
        print(angle, d)

    def keyPressEvent(self, e):
        global angle, move ,scale
        def clamp(n, minn, maxn): return max(min(maxn, n), minn)
        print(e.key())
        if e.key() == Qt.Key_W:
            print('W')
            if move != 1:
                move = 1
        elif e.key() == Qt.Key_S:
            print('S')
            if move != 3:
                move = 3
        elif e.key() == Qt.Key_A:
            print('A')
            if move != 4:
                move = 4
        elif e.key() == Qt.Key_D:
            print('D')
            if move != 2:
                move = 2
        elif e.key() == Qt.Key_I:
            angle[0] = clamp(angle[0]-1, 10, 180)
            print('I')
        elif e.key() == Qt.Key_K:
            angle[0] = clamp(angle[0]+1, 10, 180)
            print('K')
        elif e.key() == Qt.Key_J:
            angle[1] = clamp(angle[1]+1, 0, 180)
            print('J')
        elif e.key() == Qt.Key_L:
            angle[1] = clamp(angle[1]-1, 0, 180)
            print('L')
        elif e.key() == Qt.Key_R:
            angle = [90, 90]
        elif e.key() == Qt.Key_F:
            scale = clamp(scale + 1, 1, 50)
        elif e.key() == Qt.Key_H:
            scale = clamp(scale - 1, 1, 50)
        elif e.key() == Qt.Key_G:
            scale = 50
            

    def keyReleaseEvent(self, e):
        global move
        if e.key() in [Qt.Key_W, Qt.Key_S, Qt.Key_A, Qt.Key_D]:
            move = 0

    def gamepad(self):
        self.gpth = gmaepadThread()
        self.gpth.start()


class Thread(QThread):
    changePixmap = pyqtSignal(QImage)
    scaled_size = QtCore.QSize(640, 480)
    base_url = QtCore.pyqtSignal(str)
    state = False

    def run(self):
        global base_url
        cap = cv2.VideoCapture(base_url+':8080/?action=stream')
        # cap = cv2.VideoCapture(0)
        global scale
        self.th = requestSender()
        self.state = True
        self.th.start()
        while self.state:
            ret, frame = cap.read()
            if ret:
                height, width, channels = frame.shape
                print(height,width,scale)
                centerX,centerY=int(height/2),int(width/2)
                radiusX,radiusY= int(int(scale)*height/100),int(int(scale)*width/100)

                minX,maxX=centerX-radiusX,centerX+radiusX
                minY,maxY=centerY-radiusY,centerY+radiusY

                cropped = frame[minX:maxX, minY:maxY]
                self.setImage(cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB))
        cap.release()
        self.th.stop()
        self.setImage(cv2.imread('tank.png'))

    def setImage(self, rgbImage):
        convertToQtFormat = QtGui.QImage(
            rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QtGui.QImage.Format_RGB888)
        p = convertToQtFormat.scaled(
            self.scaled_size, QtCore.Qt.KeepAspectRatio)
        self.changePixmap.emit(p)

    def scaled(self, scaled_size):
        self.scaled_size = scaled_size
        if self.state == False:
            self.setImage(cv2.imread('tank.png'))

    def stop(self):
        self.state = False


class gmaepadThread(QThread):

    def run(self):
        self.j = self.connect()
        self.dir = 0
        self.s = [0, 0]
        self.s2 = [0, 0]
        self.tri = 0
        global angle, move,scale
        def clamp(n, minn, maxn): return max(min(maxn, n), minn)

        @self.j.event
        def on_button(button, pressed):
            global angle,scale
            print('button', button, pressed)
            if button == 13:
                angle = [90, 90]
                self.dir = 0
            elif button == 9:
                scale = 50
            elif button == 10:
                scale = 10

        @self.j.event
        def on_axis(axis, value):
            print('axis', axis, value)
            global angle, move
            mtmp = 0
            atmp = angle
            if axis == 'l_thumb_y' or axis == 'l_thumb_x':
                mtmp = move
                if axis == 'l_thumb_y':
                    if value >= 0.48:
                        mtmp = 1
                        self.s[0] = 1
                    elif value <= -0.48:
                        mtmp = 3
                        self.s[0] = 1
                    else:
                        self.s[0] = 0
                elif axis == 'l_thumb_x':
                    if value >= 0.48:
                        mtmp = 2
                        self.s[1] = 1
                    elif value <= -0.48:
                        mtmp = 4
                        self.s[1] = 1
                    else:
                        self.s[1] = 0
                if move != mtmp:
                    move = mtmp
                if self.s == [0, 0]:
                    move = 0
            elif axis == 'r_thumb_y' or axis == 'r_thumb_x':
                tmp = self.dir
                if axis == 'r_thumb_y':
                    if value >= 0.48:
                        tmp = 1
                        self.s2[0] = 1
                    elif value <= -0.48:
                        tmp = 2
                        self.s2[0] = 1
                    else:
                        self.s2[0] = 0
                elif axis == 'r_thumb_x':
                    if value >= 0.48:
                        tmp = 3
                        self.s2[1] = 1
                    elif value <= -0.48:
                        tmp = 4
                        self.s2[1] = 1
                    else:
                        self.s2[1] = 0
                if self.s2 == [0, 0]:
                    self.dir = 0
                else:
                    self.dir = tmp
            elif axis == 'left_trigger' or axis == 'right_trigger':
                if axis == 'left_trigger':
                    if value >=0.9:
                        self.tri = 1
                    else:
                        self.tri = 0
                elif axis == 'right_trigger':
                    if value >=0.9:
                        self.tri = 2
                    else:
                        self.tri = 0
            
        while True:
            self.j.dispatch_events()
            if self.dir == 1:
                angle[0] = clamp(angle[0]-1, 10, 180)
            elif self.dir == 2:
                angle[0] = clamp(angle[0]+1, 10, 180)
            elif self.dir == 3:
                angle[1] = clamp(angle[1]-1, 0, 180)
            elif self.dir == 4:
                angle[1] = clamp(angle[1]+1, 0, 180)

            if self.tri == 1:
                scale = clamp(scale + 0.5, 1, 50)
            elif self.tri == 2:
                scale = clamp(scale - 0.5, 1, 50)
                
            time.sleep(.01)

    def connect(self):
        joysticks = XInputJoystick.enumerate_devices()
        device_numbers = list(map(attrgetter('device_number'), joysticks))
        print('found %d devices: %s' % (len(joysticks), device_numbers))

        if not joysticks:
            print('quit')
            self.exec()
        j = joysticks[0]

        print('using %d' % j.device_number)

        battery = j.get_battery_information()
        print(battery)
        return j


class requestSender(QThread):
    state = False

    def run(self):
        global base_url, angle, move
        self.state = True
        while self.state:
            # print(angle, move)
            requests.get(base_url+':3000/pmove/' +
                         str(angle[0])+'/'+str(angle[1])+'/'+str(move))
            time.sleep(.07)

    def stop(self):
        self.state = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
