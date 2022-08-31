
import requests
import json

from python.Util import Util


from python.Api_backend.PostCheckLogin import PostCheckLogin
from python.Respons_user.ResponsContentFlex.ResponsContentFlexVaccine import ResponsContentFlexVaccine
from python.Respons_user.ResponsContentFlex.ResponsContentFlexDoctorAppointment import ResponsContentFlexDoctorAppointment

class ResponsItemHos:
    
    def __init__(self,devicetoken,body):

        user_uid = str(body["events"][0]['source']['userId'])
        response = PostCheckLogin(user_uid)
        if response["status"]:
            user_ad_code = response["data"][0]["user_ad_code"]

            status_flex_vaccine,content_vaccine = ResponsContentFlexVaccine(user_ad_code)
            status_flex_doctor_appointment,content_doctor_appointment = ResponsContentFlexDoctorAppointment(user_ad_code)

            if status_flex_vaccine == "normal":
                if status_flex_doctor_appointment == "normal":
                    contents = {
                        "type":"carousel",
                        "contents":[
                            
                            content_doctor_appointment,
                            content_vaccine,
                          

                            {
                                "type": "bubble",
                                "hero": {
                                    "type": "image",
                                    "url": "https://webhook.toat.co.th/linebot/web/src/hos_2.jpg",
                                    "size": "full",
                                    "aspectRatio": "20:13",
                                    "aspectMode": "fit",
                                    "action": {
                                        "type": "uri",
                                        "label": "Line",
                                        "uri": Util().facebook_hos_link
                                    }
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "โรงพยาบาลสวนเบญจกิติเฉลิมพระเกียรติ84พรรษา",
                                        "weight": "bold",
                                        "wrap": True,
                                        "size": "md",
                                        "contents": []
                                    },
                    
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "spacing": "sm",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "ที่อยู่ :",
                                                "size": "sm",
                                                "color": "#AAAAAA",
                                                "flex": 1,
                                                "contents": []
                                            },
                                            {
                                                "type": "text",
                                                "text": "184 ถนนพระรามที่ 4 แขวงคลองเตย เขตคลองเตย กรุงเทพมหานคร 10110",
                                                "size": "sm",
                                                "color": "#666666",
                                                "flex": 5,
                                                "wrap": True,
                                                "contents": []
                                            }
                                            ]
                                        }
                                
                                        ]
                                    }
                                    ]
                                },
                                "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 0,
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "FACEBOOK",
                                        "uri": Util().facebook_hos_link
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "โทร",
                                        "uri": "tel:026564500"
                                        },
                            
                                    },
                                
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "เส้นทาง",
                                        "uri": "https://www.google.com/maps/dir//%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%AA%E0%B8%A7%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%8D%E0%B8%88%E0%B8%81%E0%B8%B4%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%89%E0%B8%A5%E0%B8%B4%E0%B8%A1%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B8%95%E0%B8%B484%E0%B8%9E%E0%B8%A3%E0%B8%A3%E0%B8%A9%E0%B8%B2+%E0%B8%96%E0%B8%99%E0%B8%99%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%A3%E0%B8%B2%E0%B8%A1%E0%B8%97%E0%B8%B5%E0%B9%88+%E0%B9%94+%E0%B9%81%E0%B8%82%E0%B8%A7%E0%B8%87+%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B9%80%E0%B8%82%E0%B8%95%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3/@13.7224518,100.5582549,17z/data=!4m9!4m8!1m0!1m5!1m1!1s0x30e29f81891b5f77:0x8f5fd4128fa707b6!2m2!1d100.5538564!2d13.7245502!3e0"
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    }
                                    ]
                                }
                            }

                        ]
                    }
                else:
                    contents = {
                        "type":"carousel",
                        "contents":[
                            
                            content_vaccine,
                       
                            {
                                "type": "bubble",
                                "hero": {
                                    "type": "image",
                                    "url": "https://webhook.toat.co.th/linebot/web/src/hos_2.jpg",
                                    "size": "full",
                                    "aspectRatio": "20:13",
                                    "aspectMode": "fit",
                                    "action": {
                                        "type": "uri",
                                        "label": "Line",
                                        "uri": Util().facebook_hos_link
                                    }
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "โรงพยาบาลสวนเบญจกิติเฉลิมพระเกียรติ84พรรษา",
                                        "weight": "bold",
                                        "wrap": True,
                                        "size": "md",
                                        "contents": []
                                    },
                    
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "spacing": "sm",
                                        "margin": "lg",
                                        "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "spacing": "sm",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "ที่อยู่ :",
                                                "size": "sm",
                                                "color": "#AAAAAA",
                                                "flex": 1,
                                                "contents": []
                                            },
                                            {
                                                "type": "text",
                                                "text": "184 ถนนพระรามที่ 4 แขวงคลองเตย เขตคลองเตย กรุงเทพมหานคร 10110",
                                                "size": "sm",
                                                "color": "#666666",
                                                "flex": 5,
                                                "wrap": True,
                                                "contents": []
                                            }
                                            ]
                                        }
                                
                                        ]
                                    }
                                    ]
                                },
                                "footer": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "flex": 0,
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "FACEBOOK",
                                        "uri": Util().facebook_hos_link
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "โทร",
                                        "uri": "tel:026564500"
                                        },
                            
                                    },
                                
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "uri",
                                        "label": "เส้นทาง",
                                        "uri": "https://www.google.com/maps/dir//%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%AA%E0%B8%A7%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%8D%E0%B8%88%E0%B8%81%E0%B8%B4%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%89%E0%B8%A5%E0%B8%B4%E0%B8%A1%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B8%95%E0%B8%B484%E0%B8%9E%E0%B8%A3%E0%B8%A3%E0%B8%A9%E0%B8%B2+%E0%B8%96%E0%B8%99%E0%B8%99%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%A3%E0%B8%B2%E0%B8%A1%E0%B8%97%E0%B8%B5%E0%B9%88+%E0%B9%94+%E0%B9%81%E0%B8%82%E0%B8%A7%E0%B8%87+%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B9%80%E0%B8%82%E0%B8%95%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3/@13.7224518,100.5582549,17z/data=!4m9!4m8!1m0!1m5!1m1!1s0x30e29f81891b5f77:0x8f5fd4128fa707b6!2m2!1d100.5538564!2d13.7245502!3e0"
                                        },
                                        "height": "sm",
                                        "style": "link"
                                    },
                                    {
                                        "type": "spacer",
                                        "size": "sm"
                                    }
                                    ]
                                }
                            }

                        ]
                    }

        else:
            contents = {
                "type":"carousel",
                "contents":[
                
                    {
                            "type": "bubble",
                            "hero": {
                                "type": "image",
                                "url": "https://webhook.toat.co.th/linebot/web/src/hos_2.jpg",
                                "size": "full",
                                "aspectRatio": "20:13",
                                "aspectMode": "fit",
                                "action": {
                                    "type": "uri",
                                    "label": "Line",
                                    "uri": Util().facebook_hos_link
                                }
                            },
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "โรงพยาบาลสวนเบญจกิติเฉลิมพระเกียรติ84พรรษา",
                                    "weight": "bold",
                                    "wrap": True,
                                    "size": "md",
                                    "contents": []
                                },
                
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "sm",
                                    "margin": "lg",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "spacing": "sm",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "ที่อยู่ :",
                                            "size": "sm",
                                            "color": "#AAAAAA",
                                            "flex": 1,
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": "184 ถนนพระรามที่ 4 แขวงคลองเตย เขตคลองเตย กรุงเทพมหานคร 10110",
                                            "size": "sm",
                                            "color": "#666666",
                                            "flex": 5,
                                            "wrap": True,
                                            "contents": []
                                        }
                                        ]
                                    }
                            
                                    ]
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "flex": 0,
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "uri",
                                    "label": "FACEBOOK",
                                    "uri": Util().facebook_hos_link
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "uri",
                                    "label": "โทร",
                                    "uri": "tel:026564500"
                                    },
                        
                                },
                            
                                {
                                    "type": "button",
                                    "action": {
                                    "type": "uri",
                                    "label": "เส้นทาง",
                                    "uri": "https://www.google.com/maps/dir//%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%AA%E0%B8%A7%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%8D%E0%B8%88%E0%B8%81%E0%B8%B4%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%89%E0%B8%A5%E0%B8%B4%E0%B8%A1%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B8%95%E0%B8%B484%E0%B8%9E%E0%B8%A3%E0%B8%A3%E0%B8%A9%E0%B8%B2+%E0%B8%96%E0%B8%99%E0%B8%99%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%A3%E0%B8%B2%E0%B8%A1%E0%B8%97%E0%B8%B5%E0%B9%88+%E0%B9%94+%E0%B9%81%E0%B8%82%E0%B8%A7%E0%B8%87+%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B9%80%E0%B8%82%E0%B8%95%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3/@13.7224518,100.5582549,17z/data=!4m9!4m8!1m0!1m5!1m1!1s0x30e29f81891b5f77:0x8f5fd4128fa707b6!2m2!1d100.5538564!2d13.7245502!3e0"
                                    },
                                    "height": "sm",
                                    "style": "link"
                                },
                                {
                                    "type": "spacer",
                                    "size": "sm"
                                }
                                ]
                            }
                    }
                ]
            }


       
        body = {    
            "replyToken": str(devicetoken),
            "messages": [
                {
                    "type":"flex",
                    "altText":Util().intent_hos_ben,
                    "contents":contents
                }
            ]
    
        }

        

        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
        }


        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())


