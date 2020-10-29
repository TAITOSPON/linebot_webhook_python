
import requests
import json

from python.Util import Util

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util

class ResponsText:
    
    def __init__(self,devicetoken,text):
 
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {

            "to": str(devicetoken),
            "messages": [
                {
                    "type": "text",
                    "text": str(text)
                }
            ]

        
        }
        response = requests.post(Util().line_api_push,headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

# ResponsText("U4f34652f4e163d5492b3fbe573a50d0a","hi")