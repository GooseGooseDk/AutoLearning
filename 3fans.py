from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

edge_drive_path=r'D:\Program Files\Python\Python310\msedgedriver.exe'
s=Service(executable_path=edge_drive_path)
driver=webdriver.Edge(service=s)
# driver.set_window_size(800,600)

url='https://space.bilibili.com/33605910/fans/fans'
driver.get(url=url)
driver.refresh()
time.sleep(2)

names=driver.find_elements(By.CLASS_NAME,'fans-name')
descs=driver.find_elements(By.CLASS_NAME,'desc')

for i in range(len(names)):
    print(i+1,names[i].text,descs[i].text)

print('done')