
import json
from python.Util import Util


from python.Api_backend.PostUserDetailWithAd import PostUserDetailWithAd

class ResponsContentFlexEditTaxt:

    def __new__(self,user_ad_code):

        try:
   

      
            user_detail = PostUserDetailWithAd(user_ad_code)
                
            
            content = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://memberapp.toat.co.th/memberttm/Content/assets/media/logos/toat-logo-red-full-2.png",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "2:3",
                        "gravity": "top"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "เปิดระบบแก้ไข ข้อมูลค่าลดหย่อนภาษี ประจำปีภาษี 2565 รอบที่ 1",
                                "size": "xl",
                                "color": "#ffffff",
                                "weight": "bold",
                                "wrap": True
                            }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "text",
                                "text": "**ตั้งแต่วันที่ 15 ธันวาคม 2564  ถึงวันที่ 7 มกราคม 2565",
                                "color": "#ebebeb",
                                "size": "sm",
                                "flex": 0,
                                "wrap": True
                            }
                            ],
                            "spacing": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "filler"
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "filler"
                                },
                                {
                                    "type": "text",
                                    "text": "แก้ไข",
                                    "color": "#ffffff",
                                    "flex": 0,
                                    "offsetTop": "-2px"
                                },
                                {
                                    "type": "filler"
                                }
                                ],
                                "spacing": "sm"
                            },
                            {
                                "type": "filler"
                            }
                            ],
                            "borderWidth": "1px",
                            "cornerRadius": "4px",
                            "spacing": "sm",
                            "borderColor": "#ffffff",
                            "margin": "xxl",
                            "height": "40px",
                            "action": {
                            "type": "uri",
                            "label": "action",
                                "uri": Util().liff_url_profile_detail_taxt,
                                "altUri": {
                                    "desktop" : Util().url_member_tax
                                }
                            }
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#d02030CC",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "ประกาศ",
                            "color": "#ffffff",
                            "align": "center",
                            "size": "sm",
                            "offsetTop": "3px"
                        }
                        ],
                        "position": "absolute",
                        "cornerRadius": "20px",
                        "offsetTop": "18px",
                        "backgroundColor": "#ff334b",
                        "offsetStart": "18px",
                        "height": "25px",
                        "width": "53px"
                    }
                    ],
                    "paddingAll": "0px"
                }
                }

            status = "normal"
        except:
            content = {}
            status = "except"

      
 
        return status,content