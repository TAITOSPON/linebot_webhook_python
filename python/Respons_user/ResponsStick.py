import requests
import json

from python.Util import Util


class ResponsStick:

    def __init__(self,devicetoken):

        LINE_API = Util().line_api_reply
        Authorization = Util().Bearer + Util().serverToken
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Authorization':Authorization
        }
        data = json.dumps({"replyToken":devicetoken, "messages":[{ "type":"sticker","packageId":"11537","stickerId":"52002758"}]})
        response = requests.post(LINE_API, headers=headers, data=data) 
        print(response.status_code)
        print(response.json())