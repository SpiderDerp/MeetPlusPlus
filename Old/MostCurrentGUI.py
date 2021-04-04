import sys
import sqlite3
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
import asyncio
from PySide2.QtGui import QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.setFixedSize(QSize(470, 600))

        self.setWindowTitle("Meet++")
        self.setWindowIcon(QtGui.QIcon("meetlogo.ico"))

        self.titleLine = QLabel(self)
        self.titleLine.setText('Meet++')
        self.titleLine.move(20,0)

        self.meetLink = QLabel(self)
        self.meetLink.setText('Meet Link: ')
        self.meetLine = QLineEdit(self)

        self.meetLine.move(120, 40)
        self.meetLine.resize(300, 32)
        self.meetLink.move(20, 40)

        self.emailAd = QLabel(self)
        self.emailAd.setText('Email: ')
        self.emailLine = QLineEdit(self)

        self.emailLine.move(120, 80)
        self.emailLine.resize(300, 32)
        self.emailAd.move(20,80)

        self.passwordIn = QLabel(self)
        self.passwordIn.setText('Password: ')
        self.passLine = QLineEdit(self)

        self.passLine.move(120, 120)
        self.passLine.resize(300, 32)
        self.passwordIn.move(20, 120)

        self.classRoster = QLabel(self)
        self.classRoster.setText('Class Roster: ')
        self.rosterLine = QLineEdit(self)

        self.rosterLine.move(120, 160)
        self.rosterLine.resize(300, 32)
        self.classRoster.move(20, 160)

        chatBut = QPushButton('Log Into Meet', self)
        chatBut.clicked.connect(self.meetLog)
        chatBut.resize(200, 32)
        chatBut.move(120, 240)

        chatBut = QPushButton('Run Chat Overlay', self)
        chatBut.clicked.connect(self.overlay)
        chatBut.resize(200, 32)
        chatBut.move(20, 200)

        attBut = QPushButton('Run Attendance', self)
        attBut.clicked.connect(self.attendance)
        attBut.resize(200, 32)
        attBut.move(220, 200)

        self.insLine = QLabel(self)
        self.insLine.setText('Instructions: ')
        self.insLine.move(20, 280)

        self.insLine1 = QLabel(self)
        self.insLine1.resize(400,50)
        self.insLine1.setText('- Go to \'Focus Assist Settings\' and turn off \n \' When I\'m using an app in fullscreen mode\' ')
        self.insLine1.move(30, 320)

        self.insLine2 = QLabel(self)
        self.insLine2.resize(400, 80)
        self.insLine2.setText('- Enter all information necessary. Seperate \n  the names in the class roster by commas \n  Ex: FirstName1 LastName1,FirstName2 LastName2')
        self.insLine2.move(30, 380)

        self.insLine2 = QLabel(self)
        self.insLine2.resize(400, 80)
        self.insLine2.setText('- Press \'Log into Meet\' to enter the meeting. \n  Press \' Run Chat Overlay\' to run the chat overlay. \n  Press \'Run Attendance\' to run the auto-attendance')
        self.insLine2.move(30, 480)


    def meetLog(self):
        print("pie")

    def overlay(self):
        print("dej")

    def attendance(self):
        print("kik")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    stylesheet = open("Darkeum.qss")
    app.setStyleSheet(stylesheet.read())
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_())