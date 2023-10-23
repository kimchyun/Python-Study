import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("myqt04.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self) :
        a = self.le.text()
        aa = int(a)
        
        txt = ""
        txt += "{}*{}={}\n".format(aa,1,aa*1)
        txt += "{}*{}={}\n".format(aa,2,aa*2)
        txt += "{}*{}={}\n".format(aa,3,aa*3)
        txt += "{}*{}={}\n".format(aa,4,aa*4)
        txt += "{}*{}={}\n".format(aa,5,aa*5)
        txt += "{}*{}={}\n".format(aa,6,aa*6)
        txt += "{}*{}={}\n".format(aa,7,aa*7)
        txt += "{}*{}={}\n".format(aa,8,aa*8)
        txt += "{}*{}={}\n".format(aa,9,aa*9)
        
        self.te.setText(txt)
           
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()