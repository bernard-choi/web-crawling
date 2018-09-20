import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient
import pandas as pd


## 메시지 전달
def notification(message):
    slack_token = 'xoxp-432198335607-433979124469-437877501313-e48aaa1cbdc7bd8d0127ae624b07a672'
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel = "#yunsikpractice",
        text = message
    )

##로또사이트 크롤링

url  ="http://nlotto.co.kr/gameResult.do?method=byWin&drwNo="
sales = []
games = []
for i in range(1, 825):
    finalurl = url + str(i)  ## url 이 뒤에 숫자만 바뀌는 형태로 되어있다.
    sss = requests.get(finalurl)
    html = sss.text
    soup = BeautifulSoup(html, 'lxml')

    yunsik = soup.select_one("span.f_blue")
    sales.append(yunsik.string)

    yunsik2 = soup.select("td.rt")
    aa = []
    bb = [x.string for x in yunsik2]
    for j in range(5):
        aa.append(bb[4 * j + 1])

    games.append(aa)

##데이터프레임으로 만들어준다
first = [x[0] for x in games]
second = [x[1] for x in games]
third = [x[2] for x in games]
fourth = [x[3] for x in games]
fifth =  [x[4] for x in games]
x = list(range(1,825))

dongwook = pd.DataFrame({'x':x,'sales':sales,'first':first,'second':second,'third':third,'fourth':fourth,'fifth':fifth}) ##데이터프레임으로 정랼
dongwook.to_csv("dw.csv",encoding='utf-8',index=False)

notification('크롤링완료')
