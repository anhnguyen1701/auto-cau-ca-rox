import pyautogui

# iml = pyautogui.screenshot(region=(740,370,115,105))
# Box(left=746/1.02, top=387/1.06, width=77*1.5, height=55*2)
# iml = pyautogui.screenshot(region=(746, 387, 115, 110))
iml = pyautogui.screenshot(region=(731, 365, 115, 110))
iml.save(r"C:\Users\anhnguyen\Desktop\autopy\test2.png")
