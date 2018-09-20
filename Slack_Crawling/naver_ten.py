from slackclient import SlackClient
import requests
from bs4 import BeautifulSoup
import time
import json

slack_token = 'xoxp-432198335607-433979124469-437877501313-e48aaa1cbdc7bd8d0127ae624b07a672'
sc = SlackClient(slack_token)

def notification(message,sc):

    sc.api_call(
    "chat.postMessage",
    channel = "#yunsikpractice",
    text = message
    )

 #유저가 보낸 메시지 인지 파이썬이 응답한 메세지인지 검사
def is_user(k):
    return 'type' in k and 'text' in k and 'user' in k

def is_receive(data):
    return len(data)

def crawler():
    url = "https://www.naver.com"
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'lxml')
    naverLst = soup.select("span.ah_k")
    final = [x.string for x in naverLst][:10]
    return final

#RTM
if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        if is_receive(receive_data):
            keys = list(receive_data[0].keys())
            if is_user(keys):
                message = receive_data[0]['text']
                print(message)
                if message == '네이버':
                    d = crawler()
                    for i in range(len(d)):
                         notification(d[i],sc)
        time.sleep(1)
else:
    print("Connection Failed")

