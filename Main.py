import pyautogui
import time
import pytesseract
x=["No Scan Results","No Scan Results\n","No Scan Results:\n","No Scan Results:"]
while True:

    time.sleep(3)
    pyautogui.keyDown("v")
    time.sleep(0.05)
    pyautogui.keyUp("v")
    im = pyautogui.screenshot(region=(534, 911, 200, 50))
    text = pytesseract.image_to_string(im)
    time.sleep(1)
    print(str(text))
    e=str(text)
    e.strip()
    if e not in x:
        print(e)
        pyautogui.click(1101, 1031)
        time.sleep(0.1)
        pyautogui.click()
        print("e")
        time.sleep(0.1)
        pyautogui.click(1670, 141)
        time.sleep(0.1)
        pyautogui.click()
        im.save("e.png")
        break
    if pyautogui.pixelMatchesColor(1787, 846, (65, 91, 100), tolerance=10):
        print("e")
        pyautogui.click(1670, 141)
        time.sleep(0.1)
        pyautogui.click()
        break
