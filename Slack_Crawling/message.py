
## Slackclient를 이용한 메시지보내기

from slackclient import SlackClient
def notification(message):
    slack_token = 'xoxp-432198335607-433979124469-437877501313-e48aaa1cbdc7bd8d0127ae624b07a672'
    sc = SlackClient(slack_token)
    sc.api_call(
    "chat.postMessage",
    channel = "#yunsikpractice",
    text = message
    )
notification("Hi my name is Yunsik")