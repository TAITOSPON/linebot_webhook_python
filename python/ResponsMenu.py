
import requests
import json

class ResponsMenu:
    
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
                    "altText": "MENU",
                    "contents": {
                        "type": "bubble",
                        "size": "giga",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "md",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "icon",
                                                    "url": "https://www.thaitobacco.or.th/th/wp-content/uploads/2015/09/logo-ttm-admin.png",
                                                    "size": "5xl"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "align": "end",
                                                    "text": "MENU",
                                                    "weight": "bold",
                                                    "margin": "sm",
                                                    "size": "3xl",
                                                    "contents": []
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "Tobacco Authority of Thailand",
                                    "size": "xxs",
                                    "color": "#AAAAAA",
                                    "contents": []
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "News",
                                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
                                            },
                                            "color": "#D39D2B",
                                            "style": "primary",
                                            "gravity": "center"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "Time & Attendance",
                                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
                                            },
                                            "color": "#D39D2B",
                                            "margin": "xs",
                                            "style": "primary",
                                            "gravity": "center"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "margin": "xs",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "Doctor Table",
                                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
                                            },
                                            "color": "#D39D2B",
                                            "style": "primary",
                                            "gravity": "center"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "Tobacco Club",
                                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
                                            },
                                            "color": "#D39D2B",
                                            "margin": "xs",
                                            "style": "primary",
                                            "gravity": "center"
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "margin": "xs",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "Tobacco Cooperative",
                                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
                                            },
                                            "color": "#D39D2B",
                                            "style": "primary",
                                            "gravity": "center"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "Log Out",
                                                "uri": "https://liff.line.me/1654967329-5AMQZKN1"
                                            },
                                            "color": "#D39D2B",
                                            "margin": "xs",
                                            "style": "primary",
                                            "gravity": "center"
                                        }
                                    ]
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

# ResponsMenu("Uc1e2655638774e42ab8cf38043744cdb")