import pyautogui
import time	

time.sleep(10)
f = open('spam.txt', 'r')

for i in f:
	pyautogui.typewrite(i)
	pyautogui.press('enter')