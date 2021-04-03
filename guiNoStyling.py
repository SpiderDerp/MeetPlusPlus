import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from PySide2.QtGui import QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(450, 600))

        self.setWindowTitle("Meet++")

        self.titleLine = QLabel(self)
        self.titleLine.setText('Meet++')
        self.titleLine.move(20,0)

        self.meetLink = QLabel(self)
        self.meetLink.setText('Meet Link: ')
        self.meetLine = QLineEdit(self)

        self.meetLine.move(100, 40)
        self.meetLine.resize(300, 32)
        self.meetLink.move(20, 40)

        self.emailAd = QLabel(self)
        self.emailAd.setText('Email: ')
        self.emailLine = QLineEdit(self)

        self.emailLine.move(100, 80)
        self.emailLine.resize(300, 32)
        self.emailAd.move(20,80)

        self.passwordIn = QLabel(self)
        self.passwordIn.setText('Password: ')
        self.passLine = QLineEdit(self)

        self.passLine.move(100, 120)
        self.passLine.resize(300, 32)
        self.passwordIn.move(20, 120)


        pybutton = QPushButton('Enter', self)
        pybutton.clicked.connect(self.meetReg)
        pybutton.resize(200,32)
        pybutton.move(100, 160)

        self.insLine = QLabel(self)
        self.insLine.setText('Instructions: ')
        self.insLine.move(20, 200)

        self.insLine1 = QLabel(self)
        self.insLine1.resize(400,50)
        self.insLine1.setText('1. Go to \'Focus Assist Settings\' and turn off \n \' When I\'m using an app in fullscreen mode\' ')
        self.insLine1.move(30, 240)

        self.insLine2 = QLabel(self)
        self.insLine2.resize(400, 50)
        self.insLine2.setText('2. Enter all the above information and press enter ')
        self.insLine2.move(30, 280)


    def meetReg(self): #where u manipulate inputs
        print('Link: ' + self.meetLine.text())
        print('Email: ' + self.emailLine.text())
        print('Password: ' + self.passLine.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_())