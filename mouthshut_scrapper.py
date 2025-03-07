import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

url = "https://www.mouthshut.com/Insurance-Companies-ProID-925860?cid=925860&srchKeyword=insurance"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")
products = soup.find_all("div", class_= "listing-prod-title")
links_list = []
for product in products:
    link = product.find("a")
    links_list.append(link)
# print(links_list[:-5])
url_list = []
for link in links_list[:-5]:
    url = link['href']
    url_list.append(url)

# print(url_list)

for url in url_list:
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    driver = webdriver.Chrome("E:\\hackrx3\\chromedriver.exe",options=option)
    driver.get(url)
    divs =  driver.find_elements(By.CLASS_NAME, 'review-article')
    review_list = []
    for div in divs:
        reviewdiv = div.find_element(By.CLASS_NAME, "profile")
        user = div.find_element(By.CLASS_NAME, "user-ms-name")
        profile = user.find_element(By.TAG_NAME, "a")
        # print(profile.get_attribute("innerHTML"))
        paragraph = div.find_element(By.TAG_NAME, "p")
        # print(paragraph.text)
        item  ={}
        item["username"]  = profile.get_attribute("innerHTML")
        item["text"] = paragraph.get_attribute("innerHTML"),
        item['link'] = profile.get_attribute("href")
        review_list.append(item)
    print(review_list)
    driver.quit()