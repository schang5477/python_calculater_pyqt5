import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("cal.ui")[0]

#화면을 띄우는데 사용되는 Class 선언

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.number = 0
        #버튼에 기능을 연결하는 코드
        self.pb_add.clicked.connect(self.printAdd)
        self.pb_subtract.clicked.connect(self.printSubtract)
        self.pb_multiply.clicked.connect(self.printMultiply)
        self.pb_divide.clicked.connect(self.printDivide)
        self.pb_reset.clicked.connect(self.printReset)
        self.pb_1.clicked.connect(self.print1)
        self.pb_2.clicked.connect(self.print2)
        self.pb_3.clicked.connect(self.print3)
        self.pb_4.clicked.connect(self.print4)
        self.pb_5.clicked.connect(self.print5)
        self.pb_6.clicked.connect(self.print6)
        self.pb_7.clicked.connect(self.print7)
        self.pb_8.clicked.connect(self.print8)
        self.pb_9.clicked.connect(self.print9)
        self.pb_enter.clicked.connect(self.printEnter)
        self.list = []

    def printAdd(self):
        self.list.append("+")
        self.label_2.setText(str(self.list))
    def printSubtract(self):
        self.list.append("-")
        self.label_2.setText(str(self.list))
    def printMultiply(self):
        self.list.append("*")
        self.label_2.setText(str(self.list))
    def printDivide(self):
        self.list.append("%")
        self.label_2.setText(str(self.list))
    def printReset(self):

        self.list.clear()
        self.list.append("0")
        self.label_2.setText(str(self.list))
    def print1(self):
        self.list.append("1")
        self.label_2.setText(str(self.list))
    def print2(self):
        self.list.append("2")
        self.label_2.setText(str(self.list))
    def print3(self):
        self.list.append("3")
        self.label_2.setText(str(self.list))
    def print4(self):
        self.list.append("4")
        self.label_2.setText(str(self.list))
    def print5(self):
        self.list.append("5")
        self.label_2.setText(str(self.list))
    def print6(self):
        self.list.append("6")
        self.label_2.setText(str(self.list))
    def print7(self):
        self.list.append("7")
        self.label_2.setText(str(self.list))
    def print8(self):
        self.list.append("8")
        self.label_2.setText(str(self.list))
    def print9(self):
        self.list.append("9")
        self.label_2.setText(str(self.list))
    def printEnter(self):
        self.label_2.setText(str(self.list))


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()