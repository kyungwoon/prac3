from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

driver = webdriver.Chrome('./chromedriver')  # 드라이버를 실행합니다.


url = "https://www.korearank.com/tour/tour_list.php?type=28&category=A03021700"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)

driver.get(url)  # 드라이버에 해당 url의 웹페이지를 띄웁니다.
sleep(5)  # 페이지가 로딩되는 동안 5초 간 기다립니다.

req = driver.page_source  # html 정보를 가져옵니다.
driver.quit()  # 정보를 가져왔으므로 드라이버는 꺼줍니다.

# soup = BeautifulSoup(data.text, 'html.parser')
soup = BeautifulSoup(req, 'html.parser')  # 가져온 정보를 beautifulsoup으로 파싱해줍니다.

songs = soup.select("#frm > div > table > tbody > tr")
print(len(songs))


trs = soup.select('#body_main > table')

for tr in trs:
    a_tag = tr.select_one('tbody > tr:nth-child(1) > td:nth-child(2) > a > b').text
    if a_tag is not None:
        title = a_tag
        address = tr.select_one('tbody > tr:nth-child(3) > td').text
        description = tr.select_one('tbody > tr:nth-child(5) > td > span').text
        image = tr.select_one('tbody > tr:nth-child(1) > td:nth-child(1) > a > img')['src']
        url = tr.select_one('tbody > tr:nth-child(1) > td:nth-child(1) > a')

        doc = {
            'title':title,
            'address':address,
            'description':description,
            'image':image,
            'url':url
        }
        db.prac.insert_one(doc)
