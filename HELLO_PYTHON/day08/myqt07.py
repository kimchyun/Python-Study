import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import secrets

form_class = uic.loadUiType("myqt07.ui")[0]

class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        
    def getStar(self,cnt):
        ret = "";
        for i in range(cnt):
            ret+="★"
        ret += "\n"
        return ret
        
    def myclick(self) :
        f = self.le_first.text()
        l = self.le_last.text()
        ff = int(f)
        ll = int(l)
        
        txt = ""
        for i in range(ff,ll+1):
            txt += self.getStar(i)
        
        self.te.setText(txt)    
            
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()