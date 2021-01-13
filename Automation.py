from selenium import webdriver
from time import sleep

chrome_path=r"C:\Users\USER\Desktop\VSCODE\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get('http://192.168.2.2:57778/')
driver.implicitly_wait(3)

sleep(5) ; stream = driver.execute_script('return document.getElementById("stream").srcObject.active')
print("Playing..") if stream else print("Eror")
while True:
    frame = driver.execute_script('return document.getElementById("stream").webkitDecodedFrameCount')
    print("Frame:",frame)
    sleep(0.4)
