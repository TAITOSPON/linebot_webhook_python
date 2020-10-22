
import requests
import json

from python.Util import Util

class ResponsListItem:
    
    def __init__(self,devicetoken):

        headers = {
                'Content-Type': 'application/json',
                'Authorization': Util().Bearer + Util().serverToken
            }

        body = {

            "to": str(devicetoken),
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
        response = requests.post(Util().line_api_push,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())
