from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import os


#REDDIT

#initialisation
url = input("Please enter an URL: ")



browser = webdriver.Chrome()

browser.get(url)
titles = []

nextPage = 0

while nextPage<5:
    sleep(0.5)
    currentPage = browser.current_url
    browser.get(currentPage)
    try:
        posts = browser.find_elements(By.CLASS_NAME,("thing"))
        for p in posts:
            #Filters ads posts
            if "promoted" not in p.get_attribute("class"):
                title = p.find_element(By.CLASS_NAME,"top-matter")
                title = title.find_element(By.CLASS_NAME,"may-blank")
                titles.append(title.text)
        nextButton = browser.find_element(By.CLASS_NAME,("next-button"))
        nextPage += 1
        nextButton.click()
    except:
        break


location = os.path.join(os.path.dirname(__file__),'results.csv')
with open(location,'w',newline='',encoding="utf-8") as file:
    wr = csv.writer(file)
    for t in titles:
        wr.writerow(t)
    file.close()