from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://billboard.co.kr/chart/week/")

x = datetime.now()

songslist = []
i = 1

while i<100:
    for song in driver.find_elements(By.TAG_NAME, value="li"):
        print(song.text)
        for tag in song.find_elements(By.TAG_NAME, value="div"):
            for img in tag.find_elements(By.TAG_NAME, value="img"):
                print(img.get_attribute("src"))
                urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
                i = i+1
                songslist.append(
                    {"Rangking": song.text.split("\n")[0],
                    "Title": song.text.split("\n")[1],
                    "Artist": song.text.split("\n")[2],
                    "Scraping Time": x.strftime("%Y-%m-%d pukul %H:%M:%S"),
                    "Image": img.get_attribute("src")
                    }
                )
     
hasil_scraping = open("scraping2.json", "w")
json.dump(songslist, hasil_scraping, indent = 3)
hasil_scraping.close()

driver.quit()