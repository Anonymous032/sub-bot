from selenium import webdriver
import random
import string
import time

while True:
                driver=webdriver.Chrome()
                driver.get('https://mail.protonmail.com/create/new?language=en')
                time.sleep(4)
                usrnm = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
                passwd = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

                emailaddr=driver.find_element_by_xpath('//*[@id="username"]')
                emailaddr.send_keys(usrnm)
                pwd=driver.find_element_by_xpath('//*[@id="password"]')
                confpwd=driver.find_element_by_xpath('//*[@id="passwordc"]')
                pwd.send_keys(passwd)
                confpwd.send_keys(passwd)
                cracc=driver.find_element_by_xpath('//*[@id="app"]/div/footer/button')
                cracc.click()
                print(usrnm, '@protonmail.com, password is ', passwd)
                email=usrnm+'@protonmail.com'
                driver.get('https://www.youtube.com/user/Alozerk?sub_confirmation=1')
                sub=driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/paper-button')
                sub.click()
                time.sleep(1)
                loggm=driver.find_element_by_xpath('//*[@id="identifierId"]')
                loggm.send_keys(email)
                nexttopass=driver.find_element_by_xpath('//*[@id="identifierNext"]')
                nexttopass.click()
                passlog=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
                passlog.send_keys(passwd)
                nexttolog=driver.find_element_by_xpath('//*[@id="passwordNext"]')
                nexttolog.click()
                time.sleep(2)
                sub.click()
                time.sleep(1)
                driver.quit()
                

