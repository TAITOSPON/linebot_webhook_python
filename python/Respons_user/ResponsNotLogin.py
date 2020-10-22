
import requests
import json

from python.Util import Util

class ResponsNotLogin:
    
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
                    "altText": "กรุณาเข้าสู่ระบบก่อน",
                    "contents": {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "hero": {
                            "type": "image",
                            "url": "https://www.thaitobacco.or.th/th/wp-content/uploads/2015/09/logo-ttm-admin.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xs",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "คุณยังไม่ได้เข้าสู่ระบบ",
                                    "weight": "bold",
                                    "align": "center",
                                    "gravity": "bottom",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "กรุณาเข้าสู่ระบบก่อน",
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
                                    "type": "spacer",
                                    "size": "xxl"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "เข้าสู่ระบบ",
                                        "uri": "https://liff.line.me/1655109480-NdbD97GK"
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

