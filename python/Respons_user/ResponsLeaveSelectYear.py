
import requests
import json

from python.Util import Util
from python.Api_backend.PostLeaveYearSelect import PostLeaveYearSelect

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util
# from Api_backend.PostLeaveYearSelect import PostLeaveYearSelect

class ResponsLeaveSelectYear:
    
    def __init__(self,body,text):
        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])

        result = PostLeaveYearSelect(user_uid)
        items = []
        
        # data =  '{ "key":"Leave_info", "year":"2564"}'

        # in_item = {
        #     "type": "action",
        #     "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_leave.png",
        #     "action": {
        #         "type": "postback",
        #         "label" : "aaa",
        #         "data": data
        #     }
        # }


        for i in range(len(result)):

            in_item = {
                "type": "action",
                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_leave.png",
                "action": {
                    "type": "postback",
                    "label" : str(result[i]["Value"]),
                    "data": str('{ "key":"'+str(Util().Leave_info)+'", "year":"'+str(result[i]["Value"])+'"}')
                }
            }

            items.append(in_item) 

        # items.append(in_item) 
        print(items)


        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {

            "replyToken": str(user),
            "messages": [
            
               {
                    "type": "text",
                    "text": text,
                    "quickReply": {
                        "items": items
                    }
                }
            ]
        }


   
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

# ResponsLeaveSelectYear("U4f34652f4e163d5492b3fbe573a50d0a")