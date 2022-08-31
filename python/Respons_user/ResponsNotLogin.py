
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
            
            "replyToken": str(devicetoken),
            "messages": [
                  {
                    "type": "flex",
                    "altText": "กรุณาเข้าสู่ระบบก่อน",
                    "contents": {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 0,
                            "contents": [
                                {
                                    "type": "spacer"
                                }
                            ]
                        },
                        "hero": {
                            "type": "image",
                            "url": "https://webhook.toat.co.th/linebot/web/src/800px_logo_full.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                        },
                        # "body": {
                        #     "type": "box",
                        #     "layout": "vertical",
                        #     "spacing": "xs",
                        #     "contents": [
                        #         {
                        #             "type": "text",
                        #             "text": "คุณยังไม่ได้เข้าสู่ระบบ",
                        #             "weight": "bold",
                        #             "align": "center",
                        #             "gravity": "bottom",
                        #             "contents": []
                        #         },
                        #         {
                        #             "type": "text",
                        #             "text": "กรุณาเข้าสู่ระบบก่อน",
                        #             "size": "xxs",
                        #             "color": "#AAAAAA",
                        #             "align": "center",
                        #             "contents": []
                        #         }
                        #     ]
                        # },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                             
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "เข้าสู่ระบบ",
                                        "uri": Util().liff_url_login,
                                        "altUri": {
                                            "desktop" : Util().liff_url_login
                                        }
                                    },
                                    
                                    "color": "#cf0a2c",
                                    "style": "primary"
                                },
                               
                                
                            ]
                        }
                    }
                }
                    
            ]
        
        }
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

