import requests
import json

from python.Util import Util

class ResponsChecklogout:
    
    def __init__(self,devicetoken):
     
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }
        body = {    
            "replyToken": str(devicetoken),
            "messages": [
                  {
                    "type": "flex",
                    "altText": "ออกจากระบบใช่หรือไม่?",
                    "contents":
                    {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xs",
                            "action": {
                            "type": "uri",
                            "label": "Action",
                            "uri": "https://linecorp.com"
                            },
                            "contents": [
                            {
                                "type": "text",
                                "text": "ยืนยันการออกจากระบบ",
                                "weight": "bold",
                                "align": "center",
                                "gravity": "bottom",
                                "contents": []
                            },
                            {
                                "type": "text",
                                "text": "กรุณายืนยันการออกจากระบบ",
                                "size": "xxs",
                                "color": "#AAAAAA",
                                "align": "center",
                               
                                "contents": []
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                       
                            {
                                "type": "button",
                                "action": {
                                    "type": "postback",
                                    "label" : "ยืนยัน",
                                    "data": str('{ "key":"'+str(Util().User_logout)+'"}')
                                },
                                "color": "#D39D2B",
                                "style": "primary"
                            }
                            
                           
                            ]
                        }
                    }
                }
                    
            ]
        
        }
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

