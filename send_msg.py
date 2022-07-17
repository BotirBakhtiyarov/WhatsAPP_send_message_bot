import webbrowser
import pyautogui as pt
import time


reciver_contact = input("Enter Contact number or Name: ")
message = input("Enter your message: ")
limit = input("How many times: ")
webbrowser.open("https://web.whatsapp.com/")
time.sleep(15)
#print(pt.position())

#search on bar
pt.click(120,170)
pt.typewrite(reciver_contact)

#enter personal
time.sleep(2)
pt.click(207,305)
i = 1

while i <= int(limit):
    time.sleep(1)
    pt.click(593,836)
    pt.typewrite(message)

    time.sleep(1)
    pt.click(1404,838)
    i+=1