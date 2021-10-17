from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import sys

sys.path.append('\\Python39\\Lib\\site-packages\\win32')
sys.path.append('\\Python39\\Lib\\site-packages\\win32\\lib')

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(584, 422, 751, 526))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if b == 195 and r == 255 and g == 219:
                flag = 1
                click(x+584, y+422)
                time.sleep(0.05)
                break

        if flag == 1:
            break
