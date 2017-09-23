import os
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

app = Flask(__name__)

line_bot_api = LineBotApi('k9DcRI/iAbR0Ul5WEO5lolDw6n6aOrOV/e9OHVbHZnzuzV2LwMiWIb5IdL9VNMm2sULDnOohz7Rnbs0K7x71XjRvaj/oP+mY2qhNaqP0HqRpidv6aB1yrartjb4Um95JsCWw5YV+QhCKlYCTLRd8uwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('058536e5ac1427ab3e6d1238742ead5e')

@app.route("/callback", methods=['POST'])
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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)