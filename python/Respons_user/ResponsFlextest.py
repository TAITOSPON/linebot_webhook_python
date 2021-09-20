import requests
import json

from python.Util import Util
from python.Api_backend.PostLeaveYearSelect import PostLeaveYearSelect
from python.Api_backend.PostLeaveyear import PostLeaveyear


class ResponsFlextest:
    
    def __init__(self,devicetoken,body):

        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])
       
        LeaveYearSelect = PostLeaveYearSelect(user_uid)
        Leaveyear = PostLeaveyear(user_uid,LeaveYearSelect[0]["Value"])
     
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

     
        body = {    
                "replyToken": str(devicetoken),
                "messages": [
                    {
                        "type": "flex",
                        "altText": Util().intent_leave,
                        "contents": 


                        {
                            "type": "bubble",
                            "size": "giga",
                            "direction": "ltr",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                        
                                            {
                                                "type": "text",
                                                "text": Util().intent_leave,
                                                "weight": "bold",
                                                "size": "lg",
                                                "margin": "none",
                                                "contents": []
                                            },
                                            {
                                                "type": "text",
                                                "text": "ปีงบประมาณ : "+str(LeaveYearSelect[0]["Value"]),
                                                "size": "sm",
                                                "color": "#D39D2B",
                                                "contents": []
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "md"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "spacing": "sm",
                                                "margin": "xs",
                                                "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "margin": "md",
                                                    "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว :",
                                                        "size": "sm",
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                                        "align": "end",
                                                        "size": "sm",
                                                        "contents": []
                                                    }
                                                    ]
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  :",
                                                
                                                        "size": "sm",
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": str(Leaveyear['result']['leave_head']['TotalLeave']),
                                                        "size": "sm",
                                                        "align": "end",
                                                        "contents": []
                                                    }
                                                    ]
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "horizontal",
                                                    "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "วันลาพักผ่อนคงเหลือ  :",
                                                        "size": "sm",
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                                        "size": "sm",
                                                        "align": "end",
                                                        "wrap": True,
                                                        "contents": []
                                                    }
                                                    ]
                                                }
                                                ]
                                            },
                                            {
                                                "type": "separator",
                                                "margin": "md"
                                            },
                                            # {
                                            #     "type": "box",
                                            #     "spacing": "sm",
                                            #     "layout": "vertical",
                                            #     "margin": "xs",
                                            #     "contents": [
                                            #     {
                                            #         "type": "box",
                                            #         "layout": "horizontal",
                                            #         "margin": "md",
                                            #         "contents": [
                                            #         {
                                            #             "type": "text",
                                            #             "text": "เวลาออกงาน  :",
                                            #             "size": "sm",
                                            #             "contents": []
                                            #         },
                                            #         {
                                            #             "type": "text",
                                            #             "text": "out_time",
                                            #             "size": "sm",
                                            #             "align": "start",
                                            #             "contents": []
                                            #         }
                                            #         ]
                                            #     },
                                            #     {
                                            #         "type": "box",
                                            #         "layout": "horizontal",
                                            #         "contents": [
                                            #         {
                                            #             "type": "text",
                                            #             "text": "ด้วย  :",
                                            #             "size": "sm",
                                            #             "contents": []
                                            #         },
                                            #         {
                                            #             "type": "text",
                                            #             "text": "out_type",
                                            #             "size": "sm",
                                            #             "align": "start",
                                            #             "contents": []
                                            #         }
                                            #         ]
                                            #     },
                                            #     {
                                            #         "type": "box",
                                            #         "layout": "horizontal",
                                            #         "contents": [
                                            #         {
                                            #             "type": "text",
                                            #             "text": "สถานที่  :",
                                            #             "size": "sm",
                                            #             "contents": []
                                            #         },
                                            #         {
                                            #             "type": "text",
                                            #             "text": "out_place",
                                            #             "size": "sm",
                                            #             "align": "start",
                                            #             "wrap": True,
                                            #             "contents": []
                                            #         }
                                            #         ]
                                            #     }
                                            #     ]
                                            # },
                                            # {
                                            #     "type": "separator",
                                            #     "margin": "md"
                                            # }
                                        ]
                                    }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "รายละเอียด",
                                            "uri": Util().liff_url_profile_detail_askinout,
                                            "altUri": {
                                                "desktop" : Util().url_timeat
                                            }
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

        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

