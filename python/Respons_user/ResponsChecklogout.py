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
            "to": str(devicetoken),
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
                                "type": "uri",
                                "label": "ตกลง",
                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
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
        response = requests.post(Util().line_api_push,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

