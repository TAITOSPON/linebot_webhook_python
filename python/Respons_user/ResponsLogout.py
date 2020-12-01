
import requests
import json

from python.Util import Util

class ResponsLogout:
    
    def __init__(self,devicetoken,text):
   
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {

            "replyToken": str(devicetoken),
            "messages": [
            
               {
                    "type": "text",
                    "text": text,
                    "quickReply": {
                        "items": [
                            
                            {
                                "type": "action",
                                "action": {
                                    "type": "postback",
                                    "label" : str(Util().intent_login)+"อีกครั้ง",
                                    "data": str('{ "key":"'+str(Util().User_logout)+'"}')
                                },
                            }
                        ]
                    }
                }
            ]
        }

        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

