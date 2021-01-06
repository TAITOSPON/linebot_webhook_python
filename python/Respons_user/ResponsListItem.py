
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
                                        "uri": "https://www.facebook.com/Benchakitti/"
                                    },
                                    {
                                        "type": "uri",
                                        "label": "โทร",
                                        "uri": "tel:026564500"
                                    }, 
                                    {
                                        "type": "uri",
                                        "label": "เส้นทาง",
                                        "uri": "https://g.page/Benchakitti?share"
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

