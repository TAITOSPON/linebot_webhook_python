
import requests
import json

from python.Util import Util

class ResponsTimeAt:
    
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
                                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_meet.png",
                                "action": {
                                    "type": "postback",
                                    "label" : "ดูรายละเอียด",
                                    "data": str('{ "key":"'+str(Util().intent_time_work)+'", "detail":"detail"}')
                                }

                                
                            },
                        
                           
                        ]
                    }
                }
            ]
        }


        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

# ResponsQuickReply("Uc1e2655638774e42ab8cf38043744cdb")