
import requests
import json

from python.Util import Util

class ResponsWorkSystem:
    
    def __init__(self,devicetoken,contents):

        headers = {
                'Content-Type': 'application/json',
                'Authorization': Util().Bearer + Util().serverToken
            }

        body = {    
            "replyToken": str(devicetoken),
            "messages": [
                {
                    "type": "flex",
                    "altText": Util().work_system,
                    "contents": {
                        "type": "bubble",
                        "size": "mega",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "none",
                            "contents": [
                            
                                {
                                    "type": "text",
                                    "text": Util().work_system,
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
                                            "contents": contents
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

