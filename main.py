from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



#REDDIT

#Récpère la page
browser = webdriver.Chrome()
browser.get("https://old.reddit.com/r/globaloffensive")
titles = []


posts = browser.find_elements(By.CLASS_NAME,("thing"))
for p in posts:
    if "promoted" not in p.get_attribute("class"):
        title = p.find_element(By.CLASS_NAME,"top-matter")
        title = title.find_element(By.CLASS_NAME,"may-blank")
        titles.append(title.text)

print(titles)
