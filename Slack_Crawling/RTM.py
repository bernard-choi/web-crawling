

from slackclient import SlackClient
import time

slack_token = 'xoxp-432198335607-433979124469-437877501313-e48aaa1cbdc7bd8d0127ae624b07a672'
sc = SlackClient(slack_token)
if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        print(receive_data)
        time.sleep(1)
else:
    print("Connection Failed")
