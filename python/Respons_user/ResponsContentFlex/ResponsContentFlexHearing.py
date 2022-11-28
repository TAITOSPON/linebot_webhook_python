

import requests
import json
from python.Util import Util



class ResponsContentFlexHearing:

    def __new__(self,user_ad_code,devicetoken,use_type):

        if use_type == "single" : 
            try:
        
                
                content =  {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://webhook.toat.co.th/linebot/linebot_web/src/OK_Ad_TOAT_GROUP_HEARING.jpg",
                        "size": "full",
                        "aspectMode": "cover",
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
                                    "text": "ลงทะเบียน",
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
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdek8jiViWLfap63WpnVKs5og1hrbX-rO-sqJ8jGvLDB4wBQw/viewform"
                            }
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#03303Acc",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    }
                    ],
                    "paddingAll": "0px",
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdek8jiViWLfap63WpnVKs5og1hrbX-rO-sqJ8jGvLDB4wBQw/viewform"
                    }
                }
                }
                status = "normal"

                body = {    
                        "replyToken": str(devicetoken),
                        "messages": [
                            {
                                "type":"flex",
                                "altText":Util().intent_time_work,
                                "contents":content
                            }
                        ]
                
                    }

        

                headers = {
                        'Content-Type': 'application/json',
                        'Authorization':  Util().Bearer + Util().serverToken
                }


            except:
                content = {}
                status = "except"

           
            response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
            print(response.status_code)
            print(response.json())
            
        else :

            try:
        
                
                content =  {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "image",
                        "url": "https://webhook.toat.co.th/linebot/linebot_web/src/OK_Ad_TOAT_GROUP_HEARING.jpg",
                        "size": "full",
                        "aspectMode": "cover",
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
                                    "text": "ลงทะเบียน",
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
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdek8jiViWLfap63WpnVKs5og1hrbX-rO-sqJ8jGvLDB4wBQw/viewform"
                            }
                        }
                        ],
                        "position": "absolute",
                        "offsetBottom": "0px",
                        "offsetStart": "0px",
                        "offsetEnd": "0px",
                        "backgroundColor": "#03303Acc",
                        "paddingAll": "20px",
                        "paddingTop": "18px"
                    }
                    ],
                    "paddingAll": "0px",
                    "action": {
                    "type": "uri",
                    "label": "action",
                    "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdek8jiViWLfap63WpnVKs5og1hrbX-rO-sqJ8jGvLDB4wBQw/viewform"
                    }
                }
                }
                status = "normal"
            except:
                content = {}
                status = "except"

            return status,content
 
       