from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread
import json
import time
import keyboard
import os

url ="https://www.hentaiheroes.com/"
user = "gioste.rule32@virgilio.it"
password = "Nemomilla1"

## Opening JSON file
#with open('Data.json', 'r') as openfile:
#
#    # Reading from json file
#    json_object = json.load(openfile)
#



os.system("cls")

def PanicButton():
    while True:
        if keyboard.is_pressed("q"):
            driver.quit()
            print("The panic button has been pressed")
            quit()



#new test for yk

def Next(STR):
    time.sleep(0.5) 
    os.system("cls")
    print(STR)

def WaitUntillVisible_CSS_AND_CLICK(Path):
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, Path))
    )
    driver.find_element(By.CSS_SELECTOR, Path).click()


def WaitUntillVisible_XPATH_AND_CLICK(Path):
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, Path)))
    driver.find_element(By.XPATH, Path).click()

def main():
    global driver

    #driver informations
    s = Service('c:\chromedriver\chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=s, chrome_options=chrome_options)


    Next("Opening browser") # opens the browser
    driver.get(url)
    Iframe_main = driver.find_element(By.XPATH, "/html/body/iframe") #main iframe
    driver.switch_to.frame(Iframe_main)

    Next("Now running the login script") 
    WaitUntillVisible_XPATH_AND_CLICK("/html/body/div[7]/div/div/div[1]/button[1]") #age verification button
    WaitUntillVisible_XPATH_AND_CLICK("/html/body/div[2]/header/div/a[1]/div/img") #login button
    Iframe_registration = driver.find_element(By.XPATH, "/html/body/div[8]/iframe") 
    driver.switch_to.frame(Iframe_registration)
    WaitUntillVisible_XPATH_AND_CLICK("/html/body/div/form[2]/div/div[1]/input") #user field
    driver.find_element(By.XPATH, "/html/body/div/form[2]/div/div[1]/input").send_keys(user) #user field
    driver.find_element(By.XPATH, "/html/body/div/form[2]/div/div[2]/input").send_keys(password) #password field
    driver.find_element(By.XPATH, "/html/body/div/form[2]/div/button").click() #login button
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/iframe")) #main iframe
    )
    Iframe_main = driver.find_element(By.XPATH, "/html/body/iframe") #main iframe
    driver.switch_to.frame(Iframe_main)
    Next("Now in the main page")
    print("now checking for any popups...")

    def SpecialOffertsCloser():
        while True:
            try:
                SpecialOffertsIsDisplayed = driver.find_element(By.XPATH, "/html/body/div/form[2]/div/button").is_displayed() #popup div
                if SpecialOffertsIsDisplayed == True:
                    Next("Special Offerts is displayed, i'll be closing it now")
                    driver.find_element(By.CSS_SELECTOR, "img[src='https://hh2.hh-content.com/clubs/ic_xCross.png']").click() # X button
            except:
                None
    
    def NotificationRequest():
        while True:
            try:
                SpecialOffertsIsDisplayed = driver.find_element(By.CSS_SELECTOR, "#confirmation_popup").is_displayed() #popup div
                if SpecialOffertsIsDisplayed == True:
                    Next("Notification popup is displated, now closing it")
                    driver.find_element(By.XPATH, "/html/body/iframe").send_keys(Keys.ESCAPE) #exit buttonw
            except:
                None    

    def ESC():
        while True:
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    SpecialOffertsCloser_thread = Thread(target= SpecialOffertsCloser)
    NotificationRequest_thread = Thread(target= NotificationRequest)
    ESC_thread = Thread(target= ESC)
    SpecialOffertsCloser_thread.start()
    NotificationRequest_thread.start()
    ESC_thread.start()

    time.sleep(5)

    Next("Claiming the daily login reward") #Claim Daily Reward 
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/header/div[5]/plus"))) #daily login icon
    try:
        DailyLoginReward = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[5]/plus/img").is_displayed() #daily login reward icon
    except:
        Next("no dayly login rewards to be claimed")
        DailyLoginReward = False

    if DailyLoginReward == True:
        Next("Now claiming the dailiy login claim")
        driver.find_element(By.XPATH, "/html/body/div[2]/header/div[5]/plus").click() #clicks the daily reward icon
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "/html/body/div[8]/div[1]/div[1]/div/div[5]/div/div"))) #daily grid div
        try:
            driver.find_element(By.XPATH, "(//button[contains(text(),'Richiesta')])[1]").click() #click to claim
        except:
            None
        driver.find_element(By.CSS_SELECTOR, "img[src='https://hh2.hh-content.com/clubs/ic_xCross.png']").click() # X button

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/section/div[1]/div[1]/div[1]/a[2]/div/span"))) #activity menu
    MissionTask = driver.find_element(By.XPATH, "(//div[contains(@class,'daily-goals-objective-status')])[1]").text() #mission text
    print(MissionTask)
    
    




PanicButton_thread = Thread(target= PanicButton)
PanicButton_thread.start()

main = Thread(target= main)
main.daemon = True
main.start()