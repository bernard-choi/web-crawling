from slackclient import SlackClient
import time
slack_token = 'xoxp-432198335607-433979124469-437877501313-e48aaa1cbdc7bd8d0127ae624b07a672'
sc = SlackClient(slack_token)

# 메시지 전달
def notification(message,sc):
    sc.api_call(
        "chat.postMessage",
        channel = "#yunsikpractice",
        text=message
    )
#RTM
# 내가 보낸 메시지에 ' response'를 받아서 다시 보내준다
if sc.rtm_connect():
    while True:
        receive_data = sc.rtm_read()
        if len(receive_data):
            keys = list(receive_data[0].keys())
            if 'type' in keys and 'text' in keys and 'user' in keys:
                message = receive_data[0]['text']
                print(receive_data)
                notification(message + ' response', sc)
        time.sleep(1)
else:
    print("Connection Failed")