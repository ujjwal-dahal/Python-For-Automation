import pyautogui 
import time


def Message(number):
    message = f"Boksi Number {number} "
    return message

time.sleep(5)

for num in range(1,6):
    getMessage = Message(num)
    time.sleep(2)
    pyautogui.write(getMessage)
    pyautogui.press("enter")
    

