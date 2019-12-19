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
        self.result = ""
        self.list = []
        self.quest = 1
        self.answer = 0

    def printAdd(self):
        if self.quest == 0:
            self.list.append("+")
            self.addtoresult()
    def printSubtract(self):
        if self.quest == 0:
            self.list.append("-")
            self.addtoresult()
    def printMultiply(self):
        if self.quest == 0:
            self.list.append("*")
            self.addtoresult()
    def printDivide(self):
        if self.quest == 0:
            self.list.append("%")
            self.addtoresult()
    def printReset(self):

        self.result = ""
        self.label_2.setText(self.result)
    def print1(self):
        self.list.append("1")
        self.addtoresult()
        self.quest = 0
    def print2(self):
        self.list.append("2")
        self.addtoresult()
        self.quest = 0
    def print3(self):
        self.list.append("3")
        self.addtoresult()
        self.quest = 0
    def print4(self):
        self.list.append("4")
        self.addtoresult()
        self.quest = 0
    def print5(self):
        self.list.append("5")
        self.addtoresult()
        self.quest = 0
    def print6(self):
        self.list.append("6")
        self.addtoresult()
        self.quest = 0
    def print7(self):
        self.list.append("7")
        self.addtoresult()
        self.quest = 0
    def print8(self):
        self.list.append("8")
        self.addtoresult()
        self.quest = 0
    def print9(self):
        self.list.append("9")
        self.addtoresult()
        self.quest = 0
    def printEnter(self):

        li = self.list
        number = "0123456789"
        calculation = "+-*/"
        numli = []
        calli = []
        yes = 0
        stop = 0
        num1 = 0
        num2 = 0
        calculated = 0
        for a in range(len(li)):
            for b in range(10):
                if li[a] == number[b]:
                    numli.append(li[a])
                    yes += 1
            if yes == 0:
                for c in range(4):
                    if li[a] == calculation[c]:
                        calli.append(li[a])
                        stop += 1
            if stop != 0:
                num1 = int(numli.pop(len(numli) - 1))
                num2 = int(numli.pop(len(numli) - 1))
                cal = calli.pop(len(calli) - 1)
                if cal == "+":
                    calculated = num1 + num2
                if cal == "-":
                    calculated = num1 - num2
                if cal == "*":
                    calculated = num1 * num2
                if cal == "/":
                    calculated = num1 % num2
            yes = 0
            if stop != 0:
                numli.append(calculated)
            stop = 0


        temp = calculated

        self.label_2.setText(str(temp))
        self.result = ""
    def addtoresult(self):
        self.result += str(self.list[len(self.list) - 1])
        self.label_2.setText(self.result)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()