from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from win10toast import ToastNotifier


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

def join_meet(email, password, link):
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
    time.sleep(5)
    #Goes to chat tab
    driver.find_element_by_css_selector('div.HKarue').click()
    time.sleep(10)  

def check_message(old_message, i, f):
    #Finds message
    i = i
    f = f
    try:
        message = driver.find_element_by_xpath(f"//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[{f}]/div[2]/div[{i}]").get_attribute("innerHTML").splitlines()[0]
        return message
    except:
        message = old_message
        return message

def get_name(old_name, e):
    e = e
    try:
        name = driver.find_element_by_xpath(f"//*[@id=\"ow3\"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[{e}]/div[1]/div[1]").get_attribute("innerHTML").splitlines()[0]
        return name
    except:
        name = old_name
        return name 
def check_attendance(attendance_list):
    try:
        driver.find_element_by_css_selector("div.sUgV6e").click()
        time.sleep(1)
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

if __name__ == "__main__":
    toast = ToastNotifier()
    link = ""
    email = ""
    password = ""
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver.exe') 
    join_meet(email, password, link)
    #missing = check_attendance(["Arha Gatram", "Sreeram Rave", "Nermal Skywalker"])
    #print (missing)
    i = 1
    e = 1
    f = 1
    old_message = ""
    old_name = ""
    while True:
        new_name = get_name(old_name, e)
        if(old_name != new_name):
            if(old_name == ""):
                f = 1
            else:
                f +=1
                i = 1
            old_name = new_name
            e += 1
            new_message = check_message(old_message, i, f)
            old_message = new_message
            print(f"{new_name} - {new_message}")
            toast.show_toast(f"{new_name}", f"{new_message}", duration = 5, icon_path = "meetlogo.ico")
            i += 1
        elif(old_name == new_name):
            new_message = check_message(old_message, i, f)
            if(old_message != new_message):
                old_message = new_message
                print(f"{new_name} - {new_message}")
                toast.show_toast(f"{new_name}", f"{new_message}", duration = 5, icon_path = "meetlogo.ico")
                i+=1            
        time.sleep(3)
    

