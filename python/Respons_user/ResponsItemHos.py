
import requests
import json

from python.Util import Util

class ResponsItemHos:
    
    def __init__(self,devicetoken):

        headers = {
                'Content-Type': 'application/json',
                'Authorization': Util().Bearer + Util().serverToken
            }

        body = {

            "replyToken": str(devicetoken),
            "messages": [
            
                {
                    "type": "template",
                    "altText": Util().intent_covid,
                    "template": {
                        "type": "carousel",
                        "columns": [
                            
                           
                            {
                                "thumbnailImageUrl": "https://scontent.fbkk13-2.fna.fbcdn.net/v/t1.6435-9/165024853_836871947043277_9019435235398477533_n.png?_nc_cat=106&ccb=1-3&_nc_sid=973b4a&_nc_ohc=_v7NcXuPc4cAX_sxfzm&_nc_ht=scontent.fbkk13-2.fna&oh=f4197d0f0ed2162608a9d89f15097488&oe=60A87B7C",
                                "imageBackgroundColor": "#000000",
                                "title": "โรงพยาบาลสวนเบญจกิติเฉลิมพระเกียรติ84พรรษา",
                                "text": "https://www.facebook.com/Benchakitti/",
                               
                                "actions": [
                                   
                                    {
                                        "type": "uri",
                                        "label": "Facebook",
                                        "uri": "https://www.facebook.com/Benchakitti/?openExternalBrowser=1"
                                    },
                                    {
                                        "type": "uri",
                                        "label": "โทร",
                                        "uri": "tel:026564500"
                                    }, 
                                    {
                                        "type": "uri",
                                        "label": "เส้นทาง",
                                        "uri": "https://www.google.com/maps/dir//%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B8%9E%E0%B8%A2%E0%B8%B2%E0%B8%9A%E0%B8%B2%E0%B8%A5%E0%B8%AA%E0%B8%A7%E0%B8%99%E0%B9%80%E0%B8%9A%E0%B8%8D%E0%B8%88%E0%B8%81%E0%B8%B4%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%89%E0%B8%A5%E0%B8%B4%E0%B8%A1%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%81%E0%B8%B5%E0%B8%A2%E0%B8%A3%E0%B8%95%E0%B8%B484%E0%B8%9E%E0%B8%A3%E0%B8%A3%E0%B8%A9%E0%B8%B2+%E0%B8%96%E0%B8%99%E0%B8%99%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%A3%E0%B8%B2%E0%B8%A1%E0%B8%97%E0%B8%B5%E0%B9%88+%E0%B9%94+%E0%B9%81%E0%B8%82%E0%B8%A7%E0%B8%87+%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B9%80%E0%B8%82%E0%B8%95%E0%B8%84%E0%B8%A5%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%95%E0%B8%A2+%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A3/@13.7224518,100.5582549,17z/data=!4m9!4m8!1m0!1m5!1m1!1s0x30e29f81891b5f77:0x8f5fd4128fa707b6!2m2!1d100.5538564!2d13.7245502!3e0"
                                    }
                                ]
                            }

                        ],
                        "imageAspectRatio": "rectangle",
                        "imageSize": "cover"
                    }
                }
            ]

        
        }
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())

