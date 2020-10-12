
import requests
import json

class ResponsNotLogin:
    
    def __init__(self,devicetoken):
        serverToken = '4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU='


        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + serverToken,
            }

        body = {    
            "to": devicetoken,
            "messages": [
                  {
                    "type": "flex",
                    "altText": "You are not logged in.",
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
                                    "text": "You are not logged in.",
                                    "weight": "bold",
                                    "align": "center",
                                    "gravity": "bottom",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": "Please login before.",
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
                                        "label": "Log In",
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
        response = requests.post("https://api.line.me/v2/bot/message/push",headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

