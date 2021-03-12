
import requests
import json

from python.Util import Util

class ResponsListItem:
    
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
                                "thumbnailImageUrl": "https://webhook.toat.co.th/linebot/Covid_web/src/covid_report_daily.jpg",
                                "imageBackgroundColor": "#FFFFFF",
                                "title": "รายงานสถานการณ์ โควิด-19",
                                "text": "ภาพรวมของผู้ติดเชื้อ (โควิด-19) ในประเทศไทย by AwayCovid-19",
                               
                                "actions": [
                                    {
                                        "type": "uri",
                                        "label": "เตือนภัยพื้นที่เสี่ยง",
                                        "uri": "https://liff.line.me/1653981898-q0jEx1on"
                                    },
                                    {
                                        "type": "uri",
                                        "label": "สถิติผู้ติดเชื้อในไทย",
                                        "uri": "https://liff.line.me/1653981898-EK590Od2"
                                    },
                                    {
                                        "type": "uri",
                                        "label": "สถานพยาบาล",
                                        "uri": "https://liff.line.me/1653981898-QwWOp3PN"
                                    }
                                   
                                    
                                ]
                            },
                           
                            {
                                "thumbnailImageUrl": "https://webhook.toat.co.th/linebot/Covid_web/src/Benchakitti_logo.jpg",
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

