from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import infoLogin


browser = webdriver.Chrome()

browser.get("https://www.instagram.com/")

username = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
password = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
loginButton = browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')

username.send_keys(infoLogin.username)
password.send_keys(infoLogin.password)
loginButton.click()
time.sleep(7)

profile = browser.find_element(By.XPATH,'//*[@id="mount_0_0_d0"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div')
profile.click()
time.sleep(3)

followersProfile = browser.find_element(By.XPATH,'//*[@id="mount_0_0_d0"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followersProfile.click()
time.sleep(3)

jscommand = """

followers = document.querySelector("._aano");
followers.scrollTo(0,followers.scrollHeight):
var lenOfPage = followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount== lenOfPage:
        match= True
time.sleep(5) 

followersList= []
followersCount = 1

elements = browser.find_elements(By.CSS_SELECTOR,'a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd')
for element in elements:
    followersList.append(elements.text)


with open ("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(str(followersCount) + ".followers\n" + followersList +"\n" )
        file.write("********************\n")
        followersCount +=1
time.sleep(4)


browser.close()