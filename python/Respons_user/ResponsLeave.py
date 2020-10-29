import requests
import json

from python.Util import Util

class ResponsLeave:
    
    def __init__(self,devicetoken):
     
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
        }

        data =  '{ "key":"'+str(Util().Leave_info)+'", "year":""}'

        body = {    
            "to": str(devicetoken),
            "messages": [
                  {
                    "type": "flex",
                    "altText": "ข้อมูลการขาด - ลา",
                    "contents":
                    {
                        "type": "bubble",
                        "size": "kilo",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "xs",
                 
                            
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "ข้อมูลการขาด - ลา",
                                    "weight": "bold",
                                    "align": "center",
                                    "gravity": "bottom",
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
                                    "label": "ข้อมูลการขาด - ลา",
                                    "data": str(data)
                                },
                                "color": "#D39D2B",
                                "style": "primary"
                            },
                            {
                                "type": "button",
                                "margin": "xs",
                                "action": {
                                    "type": "postback",
                                    "label": "บันทึกใบลา",
                                    "data": "Developing"
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
        # body = {    
        #     "to": str(devicetoken),
        #     "messages": [
        #           {
        #             "type": "flex",
        #             "altText": "ข้อมูลการขาด - ลา",
        #             "contents":
        #             {
        #                 "type": "bubble",
        #                 "size": "kilo",
        #                 "direction": "ltr",
        #                 "body": {
        #                     "type": "box",
        #                     "layout": "vertical",
        #                     "spacing": "xs",
                 
                            
        #                     "contents": [
        #                         {
        #                             "type": "text",
        #                             "text": "ข้อมูลการขาด - ลา",
        #                             "weight": "bold",
        #                             "align": "center",
        #                             "gravity": "bottom",
        #                             "contents": []
        #                         }
        #                     ]
        #                 },
        #                 "footer": {
        #                     "type": "box",
        #                     "layout": "vertical",
        #                     "contents": [
                       
        #                     {
        #                         "type": "button",
        #                         "action": {
        #                             "type": "uri",
        #                             "label": "ข้อมูลการขาด - ลา",
        #                             "uri": "https://liff.line.me/1655109480-VOMzYnqm"
        #                         },
        #                         "color": "#D39D2B",
        #                         "style": "primary"
        #                     },
        #                     {
        #                         "type": "button",
        #                         "margin": "xs",
        #                         "action": {
        #                             "type": "postback",
        #                             "label": "บันทึกใบลา",
        #                             "data": "Developing"
        #                         },
        #                         "color": "#D39D2B",
        #                         "style": "primary"
                             
        #                     }
                            
                            
                           
        #                     ]
        #                 }
        #             }
        #         }
                    
        #     ]
        
        # }
        response = requests.post(Util().line_api_push,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

