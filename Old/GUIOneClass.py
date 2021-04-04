import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QObject, QThread, pyqtSignal, QThreadPool, QRunnable
from PySide2.QtGui import QPalette
from PyQt5 import QtGui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from win10toast import ToastNotifier

class Runnable(QRunnable):
    def __init__(self):
        super().__init__()

    def run(self):
        """Long-running task."""
        toast = ToastNotifier()
        i = 1
        e = 1
        f = 1
        old_message = ""
        old_name = ""
        while True:
            new_name = MainWindow().get_name(old_name, e)
            if(old_name != new_name):
                if(old_name == ""):
                    f = 1
                else:
                    f +=1
                    i = 1
                old_name = new_name
                e += 1
                new_message = MainWindow().check_message(old_message, i, f)
                old_message = new_message
                toast.show_toast(f"{new_name}", f"{new_message}", icon_path = "meetlogo.ico", duration = 5)
                i += 1
            elif(old_name == new_name):
                new_message = MainWindow().check_message(old_message, i, f)
                if(old_message != new_message):
                    old_message = new_message
                    toast.show_toast(f"{new_name}", f"{new_message}", icon_path = "meetlogo.ico", duration = 5)
                    i+=1            
            time.sleep(3) 

class MainWindow(QMainWindow):
    global opt
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
    })
    global driver 
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver.exe') 
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(470, 600))

        self.setWindowTitle("Meet++")
        self.setWindowIcon(QtGui.QIcon('meetlogo.ico'))
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

    def join_meet(self, email, password, link):
        driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
        time.sleep(4)
        #Enters Email
        driver.find_element_by_xpath("//input[@name='identifier']").send_keys(email)
        time.sleep(2)
        #Clicks next
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
        time.sleep(5)
        #Enters password
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        time.sleep(2)
        #Clicks next
        driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
        time.sleep(5)
        driver.get(link)
        driver.refresh()
        time.sleep(5)
        #Turning off mic and video
        camandmic = driver.find_elements_by_css_selector('div.U26fgb.JRY2Pb.mUbCce.kpROve')
        for i in camandmic:
            i.click()
        #Joins meeting
        driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
        time.sleep(7)
        #Goes to chat tab
        driver.find_element_by_css_selector('div.HKarue').click()
        time.sleep(10)  

    def check_message(self, old_message, i, f):
        #Finds message
        i = i
        f = f
        try:
            message = driver.find_element_by_xpath(f"//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[{f}]/div[2]/div[{i}]").get_attribute("innerHTML").splitlines()[0]
            return message
        except:
            message = old_message
            return message

    def get_name(self, old_name, e):
        e = e
        try:
            name = driver.find_element_by_xpath(f"//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[{e}]/div[1]/div[1]").get_attribute("innerHTML").splitlines()[0]
            return name
        except:
            name = old_name
            return name

    def check_attendance(self, attendance_list):
        try:
            driver.find_element_by_css_selector("div.sUgV6e").click()
            time.sleep(2)
            attendance_present = driver.find_elements_by_class_name("ZjFb7c")
            attendance_present_str = []
            attendance_missing = []

            for i in range(len(attendance_present)):
                attendance_present_str.append(attendance_present[i].get_attribute("innerHTML")) 

            for i in range(len(attendance_list)):
                if (attendance_list[i] not in attendance_present_str):
                    attendance_missing.append(attendance_list[i])

            driver.find_element_by_css_selector("div.zCU1Sc").click()

            if (len(attendance_missing) == 0):
                return ["Everyone is present"]
            else:
                return attendance_missing
        except:
            return ["Failed to check attendance"]


    def meetLog(self):
        email = self.emailLine.text()
        password = self.passLine.text()
        link = self.meetLine.text()
        self.join_meet(email, password, link)
        

    def overlay(self):
        pool = QThreadPool.globalInstance()
        runnable = Runnable()
        # 3. Call start()
        pool.start(runnable)

    def attendance(self):
        attendancelist = self.rosterLine.text()
        attendancelist = attendancelist.split(",")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())