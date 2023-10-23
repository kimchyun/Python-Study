import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import secrets
from random import random

form_class = uic.loadUiType("myqt03.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)

    def myclick(self):
        arr = [
            1,2,3,4,5,   6,7,8,9,10,
            11,12,13,14,15,   16,17,18,19,20,
            21,22,23,24,25,   26,27,28,29,30,
            31,32,33,34,35,   36,37,38,39,40,
            41,42,43,44,45
        ]

        for i in range(1000):
            r = int(random()*45)
            a = arr[0]
            arr[0] = arr[r]
            arr[r] = a

        print(arr)
        
        self.lbl1.setText(str(arr[0]))
        self.lbl2.setText(str(arr[1]))
        self.lbl3.setText(str(arr[2]))
        self.lbl4.setText(str(arr[3]))
        self.lbl5.setText(str(arr[4]))
        self.lbl6.setText(str(arr[5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
