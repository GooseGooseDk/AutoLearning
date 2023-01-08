from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import re

edge_drive_path=r'D:\Program Files\Python\Python310\msedgedriver.exe'
s=Service(executable_path=edge_drive_path)
driver=webdriver.Edge(service=s)
# driver.set_window_size(800,600)

url='https://space.bilibili.com/33605910/fans/fans'
driver.get(url=url)
driver.refresh()
time.sleep(1)

followers=driver.find_elements(By.XPATH,'//*[@id="page-follows"]/div/div[2]/div[2]/div[2]/ul[1]/li/a')
Signs=driver.find_elements(By.XPATH,'//*[@id="page-follows"]/div/div[2]/div[2]/div[2]/ul[1]/li/div[2]/p')

for i in range(len(followers)):
    follower=followers[i]
    Sign=Signs[i]
    name=follower.accessible_name
    herf=follower.get_attribute('href')
    uid=re.sub(r'\D','',herf)
    sign=Sign.accessible_name
    print(name.ljust(20),'签名：'+sign.ljust(20),'uid: '+uid.ljust(20))
# descs=driver.find_elements(By.CLASS_NAME,'desc')

# for i in range(len(names)):
#     print(i+1,names[i].text,descs[i].text)

print('done')
