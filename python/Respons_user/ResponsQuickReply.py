
import requests
import json

from python.Util import Util

class ResponsQuickReply:
    
    def __init__(self,devicetoken,text):
   
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {

            "replyToken": str(devicetoken),
            "messages": [
            
               {
                    "type": "text",
                    "text": text,
                    "quickReply": {
                        "items": [

                
                            {
                                "type": "action",
                                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_member.JPG",
                                "action": {
                                    "type": "uri",
                                    "label": Util().intent_profile_sys,
                                    "uri": Util().liff_url_profile_detail
                                },
                            },
                           
                            {
                                "type": "action",
                                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_meet.png",
                                "action": {
                                    "type": "uri",
                                    "label": Util().intent_time_att,
                                    "uri": Util().liff_url_time_stamp
                                },
                            },
                          
                            

                            {
                                "type": "action",
                                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_meet.png",
                                "action": {
                                    "type": "message",
                                    "label": Util().intent_time_work,
                                    "text": Util().intent_time_work
                                }
                            },
                            {
                                "type": "action",
                                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_menu.png",
                                "action": {
                                    "type": "message",
                                    "label": Util().intent_menu,
                                    "text": Util().intent_menu
                                }
                            }
                        
                           
                        ]
                    }
                }
            ]
        }


        # body = {

        #     "to": str(devicetoken),
        #     "messages": [
            
        #        {
        #             "type": "text",
        #             "text": "Hello Quick Reply!",
        #             "quickReply": {
        #                 "items": [
        #                     {
        #                         "type": "action",
        #                         "action": {
        #                         "type": "cameraRoll",
        #                         "label": "Camera Roll"
        #                         }
        #                     },
        #                     {
        #                         "type": "action",
        #                         "action": {
        #                         "type": "camera",
        #                         "label": "Camera"
        #                         }
        #                     },
        #                     {
        #                         "type": "action",
        #                         "action": {
        #                         "type": "location",
        #                         "label": "Location"
        #                         }
        #                     },
        #                     {
        #                         "type": "action",
        #                         "imageUrl": "https://cdn1.iconfinder.com/data/icons/mix-color-3/502/Untitled-1-512.png",
        #                         "action": {
        #                         "type": "message",
        #                         "label": "Message",
        #                         "text": "Hello World!"
        #                         }
        #                         },
        #                     {
        #                         "type": "action",
        #                         "action": {
        #                         "type": "postback",
        #                         "label": "Postback",
        #                         "data": "action=buy&itemid=123",
        #                         "displayText": "Buy"
        #                         }
        #                         },
        #                     {
        #                         "type": "action",
        #                         "imageUrl": "https://icla.org/wp-content/uploads/2018/02/blue-calendar-icon.png",
        #                         "action": {
        #                         "type": "datetimepicker",
        #                         "label": "Datetime Picker",
        #                         "data": "storeId=12345",
        #                         "mode": "datetime",
        #                         "initial": "2018-08-10t00:00",
        #                         "max": "2018-12-31t23:59",
        #                         "min": "2018-08-01t00:00"
        #                         }
        #                     }
        #                 ]
        #             }
        #         }
        #     ]
        # }





        #========================================================================================
        # body = {

        #     "to": str(devicetoken),
        #     "messages": [
            
        #          {
        #             "type": "text",
        #             "text": text,
        #             "quickReply": {
        #                 "items": [
        #                     {
        #                         "type": "action",
        #                         "action": {
        #                             "type": "datetimepicker",
        #                             "label": "Select date",
        #                             "data": "storeId=12345",
        #                             "mode": "datetime",
        #                             "initial": "2017-12-25t00:00",
        #                             "max": "2018-01-24t23:59",
        #                             "min": "2017-12-25t00:00"
        #                         }
        #                     },
        #                     {
        #                         "type": "action",
        #                         "action": {
        #                             "type": "location",
        #                             "label": "Location"
        #                         }
        #                     }
        #                 ]
        #             }
        #         }
        #     ]
        # }
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

# ResponsQuickReply("Uc1e2655638774e42ab8cf38043744cdb")