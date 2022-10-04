from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

run = True
quangcan_x = 0
quangcan_y = 0
quangcan_height = 10
quangcan_width = 10
print("Nhap diem the luc: ")
diemtheluc = int(input())
checkquangcan = False
checkrutcan = False


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# Box(left=755, top=454, width=95, height=20)
# o day cao gap 5 height -> height*5
# width* 1.5
# toa do y = top-4*heghit
# toa do x = left- 0.2*width
def getlocation(quangcanlocation):
    quangcan_x = quangcanlocation.left - 0.1*quangcanlocation.width
    quangcan_y = quangcanlocation.top - 4.2*quangcanlocation.height
    quangcan_height = quangcanlocation.height*5.4
    quangcan_width = quangcanlocation.width*1.2
    return quangcan_x, quangcan_y, quangcan_height, quangcan_width
# region: ((740,370,115,105))


while keyboard.is_pressed("q") == False:
    if (run):
        print("run")
        locatequangcan = pyautogui.locateOnScreen(
            'quangcan3.png', confidence=0.8)
        if (locatequangcan != None):
            quangcan_x, quangcan_y, quangcan_height, quangcan_width = getlocation(
                locatequangcan)
            run = False
        else:
            print("khong xac dinh dc quang can")

    postitonquangcan = pyautogui.locateOnScreen('quangcan3.png', region=(int(quangcan_x), int(
        quangcan_y), int(quangcan_width), int(quangcan_height)), confidence=0.8)
    postionkeocan = pyautogui.locateOnScreen('keocan2.png', region=(int(quangcan_x), int(
        quangcan_y), int(quangcan_width), int(quangcan_height)), confidence=0.8)

    # quang can
    # 749 451 20 95
    # y = top - height*4/2
    # x = left + width/2

    # keo can
    # 761 387 59 68
    # y = top + height/2
    # s = left + width/2
    if (postitonquangcan != None) & (checkquangcan != True):
        print("quang can")
        x = int(postitonquangcan.left + postitonquangcan.width/2)
        y = int(postitonquangcan.top - postitonquangcan.height*4/2)

        time.sleep(0.2)
        click(x, y)
        diemtheluc -= 10
        print("diem the luc ", diemtheluc)
        postitonquangcan = None
        checkquangcan = True
        checkrutcan = False

    elif (postionkeocan != None) & (checkrutcan != True):
        print("keo can")
        x = int(postionkeocan.left + postionkeocan.width/2)
        y = int(postionkeocan.top + postionkeocan.height/2)

        click(x, y)
        checkquangcan = False
        checkrutcan = True
        postionkeocan = None
    else:
        if diemtheluc <= 10:
            break
        else:
            time.sleep(0.2)
            # print("ko thay gi")