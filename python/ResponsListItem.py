
import requests
import json

class ResponsListItem:
    
    def __init__(self,serverToken,devicetoken):
        # serverToken = '4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU='
        # deviceToken = 'device token here'

        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + serverToken,
            }

        body = {

            "to": devicetoken,
            "messages": [
            
                {
                    "type": "template",
                    "altText": "this is a carousel template",
                    "template": {
                        "type": "carousel",
                        "columns": [
                            {
                                "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
                                "imageBackgroundColor": "#FFFFFF",
                                "title": "this is menu",
                                "text": "description",
                                "defaultAction": {
                                    "type": "uri",
                                    "label": "View detail",
                                    "uri": "http://example.com/page/123"
                                },
                                "actions": [
                                    {
                                        "type": "postback",
                                        "label": "Buy",
                                        "data": "action=buy&itemid=111"
                                    },
                                    {
                                        "type": "postback",
                                        "label": "Add to cart",
                                        "data": "action=add&itemid=111"
                                    },
                                    {
                                        "type": "uri",
                                        "label": "View detail",
                                        "uri": "http://example.com/page/111"
                                    }
                                ]
                            },
                            {
                                "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
                                "imageBackgroundColor": "#000000",
                                "title": "this is menu",
                                "text": "description",
                                "defaultAction": {
                                    "type": "uri",
                                    "label": "View detail",
                                    "uri": "http://example.com/page/222"
                                },
                                "actions": [
                                    {
                                        "type": "postback",
                                        "label": "Buy",
                                        "data": "action=buy&itemid=222"
                                    },
                                    {
                                        "type": "postback",
                                        "label": "Add to cart",
                                        "data": "action=add&itemid=222"
                                    },
                                    {
                                        "type": "uri",
                                        "label": "View detail",
                                        "uri": "http://example.com/page/222"
                                    }
                                ]
                            }
                        ],
                        "imageAspectRatio": "rectangle",
                        "imageSize": "cover"
                    }
                }
            ]

        
        }
        response = requests.post("https://api.line.me/v2/bot/message/push",headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

