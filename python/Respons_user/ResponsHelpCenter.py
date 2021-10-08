
import requests
import json

from python.Util import Util

class ResponsHelpCenter:
    
    def __init__(self,devicetoken):

        headers = {
                'Content-Type': 'application/json',
                'Authorization': Util().Bearer + Util().serverToken
            }

        body = {    
            "replyToken": str(devicetoken),
            "messages": [
                {
                    "type": "flex",
                    "altText": Util().help_center,
                    "contents": {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "none",
                            "contents": [
                            
                                {
                                    "type": "text",
                                    "text": Util().help_center,
                                    "weight": "bold",
                                    "size": "lg",
                                  
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
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": 'https://webhook.toat.co.th/linebot/web/src/%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD_LINE_FULL.pdf',
                                                        "altUri": {
                                                            "desktop" : 'https://webhook.toat.co.th/linebot/web/src/%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD_LINE_FULL.pdf'
                                                        }
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                              
                                                                {
                                                                    "type": "text",
                                                                    "text": "คู่มือการใช้",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]

                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "xs",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",

                                                     "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": Util().liff_url_help_center
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                              
                                                                {
                                                                    "type": "text",
                                                                    "text": "รายงานปัญหาในการใช้งาน",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                   
                                                }
                                            ]
                                        }
                                    ]
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

