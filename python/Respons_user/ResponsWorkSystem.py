
import requests
import json

from python.Util import Util

class ResponsWorkSystem:
    
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
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": Util().liff_url_work_system_report_sale,
                                                      
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
                                                                    "text": "รายงานการขาย",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                },
                                                                # {
                                                                #     "type": "icon",
                                                                #     "url": "https://webhook.toat.co.th/linebot/web/src/800px.png",
                                                                #     "size" : "xxl"
                                                                    
                                                                # }, 
                                                                # {
                                                                #     "type": "icon",
                                                                #     "url": "https://webhook.toat.co.th/linebot/web/src/trans.png",
                                                                #     "size" : "sm"
                                                                # }, 
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]

                                                },
                                              
                                                # {
                                                #     "type": "box",
                                                #     "layout": "vertical",
                                                #     "margin": "xs",
                                                #     "backgroundColor": "#D39D2B",
                                                #     "cornerRadius": "5px",

                                                #      "action": {
                                                #         "type": "uri",
                                                #         "label": "Action",
                                                #         "uri": Util().liff_url_help_center
                                                #     },
                                                #     "contents": [
                                                #         {
                                                #             "type": "spacer",
                                                #             "size": "xl"
                                                #         },
                                                #         {
                                                #             "type": "box",
                                                #             "layout": "baseline",
                                                #             "contents": [
                                                #                 {
                                                #                     "type": "spacer"
                                                #                 },
                                                              
                                                #                 {
                                                #                     "type": "text",
                                                #                     "text": "ระบบจุ๊กกรู๊",
                                                #                     "color": "#FFFFFFFF",
                                                #                     "align": "start",
                                                #                     "gravity": "center",
                                                #                     "offsetBottom": "2px",
                                                #                     "offsetStart": "2px",
                                                #                     "contents": []
                                                #                 }
                                                #             ]
                                                #         },
                                                #         {
                                                #             "type": "spacer",
                                                #             "size": "xl"
                                                #         }
                                                #     ]
                                                   
                                                # },
                                              
                                                # {
                                                #     "type": "box",
                                                #     "layout": "vertical",
                                                #     "margin": "xs",
                                                #     "backgroundColor": "#D39D2B",
                                                #     "cornerRadius": "5px",

                                                #      "action": {
                                                #         "type": "uri",
                                                #         "label": "Action",
                                                #         "uri": Util().liff_url_help_center
                                                #     },
                                                #     "contents": [
                                                #         {
                                                #             "type": "spacer",
                                                #             "size": "xl"
                                                #         },
                                                #         {
                                                #             "type": "box",
                                                #             "layout": "baseline",
                                                #             "contents": [
                                                #                 {
                                                #                     "type": "spacer"
                                                #                 },
                                                              
                                                #                 {
                                                #                     "type": "text",
                                                #                     "text": "ระบบจุ๊กกกกกกกกกกกกก",
                                                #                     "color": "#FFFFFFFF",
                                                #                     "align": "start",
                                                #                     "gravity": "center",
                                                #                     "offsetBottom": "2px",
                                                #                     "offsetStart": "2px",
                                                #                     "contents": []
                                                #                 }
                                                #             ]
                                                #         },
                                                #         {
                                                #             "type": "spacer",
                                                #             "size": "xl"
                                                #         }
                                                #     ]
                                                   
                                                # },
                                           
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

