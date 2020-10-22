
import requests
import json

from python.Util import Util

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

# ResponsQuickReply("Uc1e2655638774e42ab8cf38043744cdb")