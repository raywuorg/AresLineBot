from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import requests

app = Flask(__name__)
#line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
#handler = WebhookHandler('YOUR_CHANNEL_SECRET')
line_bot_api = LineBotApi('UQr71PlWAcmC0tBB8F6nIqxTX5gaXK85TWeDBYeUbP8a9+t6+8dVFCCr9yL0npVaM5ADS3Kcxv2gwkp1FHKM2XdxNdWCaYzQbgQxxwF1C+oJZkqVongg/ttfW4RtcqUfLlipSNuRR+tCGI0v0bK8rwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('dc2b3a87b8a2f091d58b464b156014cd')
#ngrok token: 2J73TEfW8q4edfSNqHOxBdhGTdK_hm9gnx8F8Hqk5oRZUuZS

@app.route("/callback", methods=['POST'])

#def lineNotifyMessage(msg):
#    headers = {
#        "Authorization": "Bearer " + 'muVJwaFTAYjAg9X15rTUOwieyV6ahZcJXE6hiq8J4gu', 
#        "Content-Type" : "application/x-www-form-urlencoded"
#    }
#
#    payload = {'message': msg}
#    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
#    return r.status_code

def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    #line_bot_api.reply_message(
    #    event.reply_token,
    #    TextSendMessage(text=event.message.text))
    #lineNotifyMessage(' said:: '+event.message.text)

    headers = {
        "Authorization": "Bearer " + 'muVJwaFTAYjAg9X15rTUOwieyV6ahZcJXE6hiq8J4gu', 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': event.message.text}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

if __name__ == "__main__":
    app.run()