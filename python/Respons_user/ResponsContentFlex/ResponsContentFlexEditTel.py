
import json
from python.Util import Util


from python.Api_backend.PostUserDetailWithAd import PostUserDetailWithAd

class ResponsContentFlexEditTel:

    def __new__(self,user_ad_code):

        try:
   

      
            user_detail = PostUserDetailWithAd(user_ad_code)
                
            
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
                                    "text": Util().edit_tel,
                                    "weight": "bold",
                                    "size": "lg",
                                    "margin": "none",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": user_detail["result"]["personal"]["PersonalName"],
                                    "size": "sm",
                                    "color": "#d3af04",
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
                                            "text": "ชื่อเล่น : "+user_detail["result"]["personal"]["PersonalNickName"],
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
                                            "text": "เบอร์โทรภายใน : "+user_detail["result"]["personal"]["TelOffice"],
                                    
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
                                            "text": "เบอร์โทรศัพท์  : "+user_detail["result"]["personal"]["TelMobile"],
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
                                "label": "ปรับปรุงเบอร์โทร",
                                "uri": Util().liff_url_profile_detail_lineoaformsettingtelephonenumber,
                                "altUri": {
                                    "desktop" : Util().profile_detail_lineoaformsettingtelephonenumber
                                }
                            },
                            
                            "color": "#d3af04",
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