import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

def getCuriousUsers(keyword):
    question_list = []
    url = "https://www.quora.com/search?q="+keyword+"&time=day&type=question"
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome("E:\\hackrx3\\chromedriver.exe",options=option)
    driver.get(url)
    questionbox = driver.find_element(By.ID, "mainContent")
    # print(questionbox.get_attribute("innerHTML"))
    body = BeautifulSoup(questionbox.get_attribute("innerHTML"), "html.parser")
    innerdiv = body.find("div", class_="q-box")
    questiondiv = innerdiv.find("div")
    questionlinks = questiondiv.find_all("a", class_="q-box")
    for question in questionlinks: 
        link = question["href"]
        if "profile" not in link and "/answer/" not in link:
            print(link)
            question_list.append(link)
    driver.quit()
    return question_list[1:]

def getCuriousProfiles():
    question_list = getCuriousUsers("insurance")
    for question in question_list:
        option = webdriver.ChromeOptions()
        driver = webdriver.Chrome("E:\\hackrx3\\chromedriver.exe",options=option)
        driver.get(question+"/log")
        counter = 2000
        while True:
            # Scroll down to bottom
            driver.execute_script(f"window.scrollTo(0, {counter});")

            # Wait to load page
            time.sleep(2)
            last_height = 0
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            maindiv = driver.find_element(By.ID, "mainContent")
            divs = maindiv.find_elements(By.CLASS_NAME,"q-box")
            soup = BeautifulSoup(maindiv.get_attribute("innerHTML"), "html.parser")
            innerdiv = soup.find_all("div", class_="qu-borderBottom")[-1]
            questiondiv = innerdiv.next_sibling
            questiondiv.find("div", class_="q-box")
            print(questiondiv.get("innerHTML"))
            last_height = new_height
            counter+=2000

getCuriousProfiles()