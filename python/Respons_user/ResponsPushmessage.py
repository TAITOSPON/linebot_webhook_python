
import requests
import json

from python.Util import Util

class ResponsPushmessage:
    
    def __init__(self,devicetoken,text):
        
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {
            
            "to": devicetoken,
            "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
        }

        response = requests.post(Util().line_api_push,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())