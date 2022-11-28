

import requests
import json
from python.Util import Util



class ResponsContentPR:

    def __new__(self,user_ad_code,devicetoken,use_type):

        if use_type == "single" : 
            try:
                
                content =  {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://www.thaitobacco.or.th/wp-content/uploads/2022/09/intro_view01.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "action": {
                            "type": "uri",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                            "altUri": {
                                "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                            }
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "สำหรับพนักงานทุกท่าน",
                                "weight": "bold",
                                "size": "xl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "ตอบแบบสำรวจสภาพแวดล้อมในการทำงาน",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "ภายในวันที่ 9 ธันวาคม 2565",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                    ]
                                }
                                ]
                            }
                            ],
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                            "altUri": {
                                "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                            }
                            }
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "uri",
                                "label": "ตอบแบบสำรวจ",
                                "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                                "altUri": {
                                    "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                                }
                                }
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "margin": "sm"
                            }
                            ],
                            "flex": 0,
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                            "altUri": {
                                "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                            }
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
                        "hero": {
                            "type": "image",
                            "url": "https://www.thaitobacco.or.th/wp-content/uploads/2022/09/intro_view01.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "action": {
                            "type": "uri",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                            "altUri": {
                                "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                            }
                            }
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "สำหรับพนักงานทุกท่าน",
                                "weight": "bold",
                                "size": "xl"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "margin": "lg",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "ตอบแบบสำรวจสภาพแวดล้อมในการทำงาน",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "spacing": "sm",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "ภายใน 9 ธันวาคม 2565",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                    ]
                                }
                                ]
                            }
                            ],
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                            "altUri": {
                                "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                            }
                            }
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                "type": "uri",
                                "label": "ตอบแบบสำรวจ",
                                "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                                "altUri": {
                                    "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                                }
                                }
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "margin": "sm"
                            }
                            ],
                            "flex": 0,
                            "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform",
                            "altUri": {
                                "desktop": "https://docs.google.com/forms/d/e/1FAIpQLSdwXYj5HCef-SZBx62kC8KuWpsbYBp89aWvY8xQTKqD1SZFfA/viewform"
                            }
                            }
                        }
                    }
                status = "normal"
            except:
                content = {}
                status = "except"

            return status,content
 
       