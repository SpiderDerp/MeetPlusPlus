from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from win10toast import ToastNotifier


import re

#Enter login info 
#gmail_user = input("Enter your email: ")
#gmail_password = input("Enter your password: ")
#meet_link = input("Paste Google Meet Link here: ")

gmail_user = ""
gmail_password = ""
meet_link = "https://meet.google.com/pbo-ynqq-kjz"
#Makes the window suitable for the program
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--disable-web-security")
opt.add_argument("--allow-running-insecure-content")
opt.add_argument('--disable-blink-features=AutomationControlled')


opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

#Signs in
chromedriver = webdriver.Chrome(options=opt, executable_path="chromedriver.exe") 

#chromedriver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')  #uses stack overflow to login through google
#sleep(5)
#chromedriver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()  #signing in with google
#chromedriver.find_element_by_xpath('//input[@type="email"]').send_keys(gmail_user)  #Entering the email
#chromedriver.find_element_by_xpath('//*[@id="identifierNext"]').click()
#sleep(5)
#chromedriver.find_element_by_xpath('//input[@type="password"]').send_keys(gmail_password)  #entering the password
#chromedriver.find_element_by_xpath('//*[@id="passwordNext"]').click()

resume = ""
while(resume != "continue"):
    resume = input("Type \"continue\" here when you log into Google: ")

#Joins the meeting
chromedriver.get(meet_link)
sleep(15)
chromedriver.find_element_by_css_selector('button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.ksBjEc.lKxP2d.cjtUbb').click()
sleep(5)
camandmic = chromedriver.find_elements_by_css_selector('div.U26fgb.JRY2Pb.mUbCce.kpROve')
for i in camandmic:
    i.click()
chromedriver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click() 
sleep(5)

#Goes to chat tab
chromedriver.find_element_by_css_selector('div.uArJ5e.UQuaGc.kCyAyd.QU4Gid.foXzLb.M9Bg4d').click()
sleep(5)

#Gets the messages
names = chromedriver.find_elements_by_css_selector('div.z38b6.CnDs7d.hPqowe')
print(names)

toaster = ToastNotifier()
#toaster.show_toast(f"Cum",
                   #{article},
                   #duration=10)