
import requests
import json

from python.Util import Util

class ResponsMemberFlex:
    
    def __init__(self,devicetoken,body,titlename,liff):
       
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {

            "replyToken": str(devicetoken),
            "messages": [
            
               {
                    "type": "text",
                    "text": "คุณหมายถึง"+titlename+"ใช่ไหม?",
                    "quickReply": {
                        "items": [

                
                            {
                                "type": "action",
                                "imageUrl": "",
                                "action": {
                                    "type": "uri",
                                    "label": titlename,
                                    "uri": liff
                                },
                            }
                        
                           
                        ]
                    }
                }
            ]
        }
        # body = {    
        #         "replyToken": str(devicetoken),
        #         "messages": [
        #             {
        #                 "type": "flex",
        #                 "altText": Util().intent_time_work,
        #                 "contents": 


        #             {
        #                 "type": "bubble",
        #                 # "size": "giga",
        #                 "direction": "ltr",
        #                 "body": {
        #                     "type": "box",
        #                     "layout": "vertical",
        #                     "contents": [
        #                         {
        #                             "type": "box",
        #                             "layout": "vertical",
        #                             "contents": [
                        
        #                             {
        #                                 "type": "text",
        #                                 "text": titlename,
        #                                 "weight": "bold",
        #                                 "size": "lg",
        #                                 "margin": "none",
        #                                 "contents": []
        #                             },
        #                             {
        #                                 "type": "text",
        #                                 "text": " ",
        #                                 "size": "sm",
        #                                 "color": "#d3af04",
        #                                 "contents": []
        #                             },
                                
        #                             ]
        #                         }
        #                     ]
        #                 },
        #                 "footer": {
        #                     "type": "box",
        #                     "layout": "horizontal",
        #                     "contents": [
        #                         {
        #                             "type": "button",
        #                             "action": {
        #                             "type": "uri",
        #                             "label": "คลิก",
        #                             "uri": liff
        #                             },
        #                             "color": "#d3af04",
        #                             "style": "primary"
        #                         }
        #                     ]
        #                 }
        #                 }  


        #             }     
        #         ]
        
        #     }
    
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())


# ResponsMenu("Uc1e2655638774e42ab8cf38043744cdb")