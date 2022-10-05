try:
    from pyautogui import *
    import pyautogui
    import time
    import keyboard
    import random
    import win32api, win32con

    print("nhan ctrl C de thoat")
    print("keo man hinh gia lap to hoac be cho den khi xuat hien chu: I can see it")

    while 1:
        if pyautogui.locateOnScreen('quangcan2.png', confidence=0.8) != None:
            print("I can see it")
            time.sleep(0.5)
        else:
            print("I am unable to see it")
            time.sleep(0.5)

    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
except Exception as e:
    print(e)

input()