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

pages=5
for i in range(pages):
    followers=driver.find_elements(By.XPATH,'//*[@id="page-follows"]/div/div[2]/div[2]/div[2]/ul[1]/li/a')
    Signs=driver.find_elements(By.XPATH,'//*[@id="page-follows"]/div/div[2]/div[2]/div[2]/ul[1]/li/div[2]/p')

    for j in range(len(followers)):
        follower=followers[j]
        Sign=Signs[j]
        name=follower.accessible_name
        herf=follower.get_attribute('href')
        uid=re.sub(r'\D','',herf)
        sign=Sign.accessible_name
        print(i*20+j+1,': ',name.ljust(20),'签名：'+sign.ljust(20),'uid: '+uid.ljust(20))
    print('number %d page done'%(i+1))

    next_page=driver.find_element(By.XPATH,'//*[@id="page-follows"]/div/div[2]/div[2]/div[2]/ul[2]/li[@title="下一页"]/a')
    next_page.click()

# //*[@id="page-follows"]/div/div[6]/div[2]/div/div[3]/a/span
# //*[@id="page-follows"]/div/div[6]/div[2]/div/div[3]/a/span
    # try:
    #     banned=driver.find_elements(By.XPATH,'//*[@id="page-follows"]/div/div[6]/div[2]/div/div[1]/div[@class="modal-title"')
    #     if banned:
    #         print('被ban了')
    #         break
    # except:
    #     print('没被ban')
    time.sleep(1)




print('done')
