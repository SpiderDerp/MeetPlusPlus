from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
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

def join_meet(link):
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(4)
    #Enters Email
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("meetplusplus@gmail.com")
    time.sleep(2)
    #Clicks next
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
    #Enters password
    driver.find_element_by_xpath("//input[@name='password']").send_keys("GoogleMeet++")
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
    time.sleep(5)
    #Goes to chat tab
    driver.find_element_by_css_selector('div.HKarue').click()
    time.sleep(10)  
    messages = driver.find_elements_by_css_selector('div.oIy2qc')
    for message in messages[1:]:
        print(message.text)
    print(messages)


if __name__ == "__main__":
    link = "https://meet.google.com/pbo-ynqq-kjz"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver.exe') 
    join_meet(link)
    

