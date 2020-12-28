
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
                                "text": "ภาพรวมของผู้ติดเชื้อ (โควิด-19) ในประเทศไทย",
                               
                                "actions": [
                                 
                                    {
                                        "type": "uri",
                                        "label": "ดูภาพรวม",
                                        "uri": "https://covid19.th-stat.com/th/share/dashboard"
                                    }
                                ]
                            },
                            {
                                "thumbnailImageUrl": "https://www.enterpriseitpro.net/wp-content/uploads/2020/03/google-establishes-covid-19-fund.jpg",
                                "imageBackgroundColor": "#000000",
                                "title": "โรคติดเชื้อไวรัสโคโรนา (COVID-19)",
                                "text": "ข้อมูลรอบโลกและสถิติ",
                               
                                "actions": [
                                   
                                    {
                                        "type": "uri",
                                        "label": "ดูรายละเอียด",
                                        "uri": "https://news.google.com/covid19/map?hl=th&gl=TH&ceid=TH%3Ath"
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
                                        "label": "facebook",
                                        "uri": "https://www.facebook.com/Benchakitti/"
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

