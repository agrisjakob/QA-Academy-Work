# This file includes the practice code I used to understand Selenium better and the while loop that continuously checks for a free
# delivery slot and alerts me if one is availalb. However, I've not been able to find an avialable slot yet, so I've not been able to
# test if this actually works.
import time
import winsound
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.tesco.com/groceries/en-GB/slots/delivery/2020-05-02?slotGroup=4')

username = driver.find_element_by_id("username")
username.click()
username.send_keys('')
password = driver.find_element_by_id("password")
password.send_keys('')
from selenium.webdriver.common.keys import Keys
password.send_keys((Keys.ENTER))


#Creates a random number to be used to set a random time interval in miliseconds
def randomTime():
    listOfSeconds = list(range(29765,42874))
    randomInterval = random.choice(listOfSeconds)
    return randomInterval/1000

noSlot = True

while noSlot == True:
    driver.get('https://www.tesco.com/groceries/en-GB/slots/delivery/2020-05-05?slotGroup=4')
    availability = driver.find_element_by_class_name("book-a-slot--info-message")
    freeslot = availability.text
    if freeslot != 'No slots available! Try another day':
        noSlot = False
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)
    time.sleep(randomTime())
