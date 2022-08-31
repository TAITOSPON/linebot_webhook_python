import json
from python.Util import Util

from python.Api_backend.PostLeaveYearSelect import PostLeaveYearSelect
from python.Api_backend.PostLeaveyear import PostLeaveyear

class ResponsContentFlexLeave:

    def __new__(self,body):

        try:
            user_uid = str(body["events"][0]['source']['userId'])
            user = str(body["events"][0]['replyToken'])

            LeaveYearSelect = PostLeaveYearSelect(user_uid)
            Leaveyear = PostLeaveyear(user_uid,LeaveYearSelect[0]["Value"])
            
                
            
            content = {
                "type": "bubble",
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
                                    "color": "#cf0a2c",
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
                                        "layout": "vertical",
                                        "margin": "md",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว : "+str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                            "size": "sm",
                                            "contents": []
                                        },
                                        
                                        ]
                                    },

                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },

                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  : "+str(Leaveyear['result']['leave_head']['TotalLeave']),
                                    
                                            "size": "sm",
                                            "contents": []
                                        },
                                        
                                        ]
                                    },

                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },

                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "วันลาพักผ่อนคงเหลือ  : "+str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                            "size": "sm",
                                            "contents": []
                                        },
                                        
                                        ]
                                    }
                                    ]
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                
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
                                "uri": Util().liff_url_profile_detail_leave,
                                "altUri": {
                                    "desktop" : Util().profile_detail_leaveyear
                                }
                            },
                            
                            "color": "#cf0a2c",
                            "style": "primary"
                        }
                    ]
                }
            } 

            status = "normal"
        except:
            content = {}
            status = "except"

      
 
        return status,content