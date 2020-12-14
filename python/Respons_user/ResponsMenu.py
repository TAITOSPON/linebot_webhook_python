
import requests
import json

from python.Util import Util

class ResponsMenu:
    
    def __init__(self,devicetoken):
       
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {    
            "replyToken": str(devicetoken),
            "messages": [
                {
                    "type": "flex",
                    "altText": "เมนู",
                    "contents": {
                        "type": "bubble",
                        "size": "giga",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "md",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "spacing": "sm",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "contents": [
                                                {
                                                    "type": "icon",
                                                    "url": "https://www.thaitobacco.or.th/th/wp-content/uploads/2015/09/logo-ttm-admin.png",
                                                    "size": "5xl"
                                                }
                                            ]
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "align": "end",
                                                    "text": "เมนู",
                                                    "weight": "bold",
                                                    "margin": "sm",
                                                    "size": "3xl",
                                                    "contents": []
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "text",
                                    "text": "การยาสูบแห่งประเทศไทย",
                                    "size": "xxs",
                                    "color": "#AAAAAA",
                                    "contents": []
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": "https://www.thaitobacco.or.th/th/category/pr-ttm"
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                              
                                                                {
                                                                    "type": "text",
                                                                    "text": "ข่าวประชาสัมพันธ์",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "xs",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "message",
                                                        "label": "Action",
                                                        "text": Util().intent_meet
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                            
                                                                {
                                                                    "type": "text",
                                                                    "text":  Util().intent_meet,
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "margin": "xs",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": "https://www.facebook.com/Benchakitti/"
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                            
                                                                {
                                                                    "type": "text",
                                                                    "text": "รพ.สวนเบญฯ",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "xs",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": "https://linecorp.com"
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                            
                                                                {
                                                                    "type": "text",
                                                                    "text": "สโมสร พนง.ยาสูบ",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "type": "box",
                                    "margin": "xs",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "horizontal",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": Util().liff_url_profile_detail
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                              
                                                                {
                                                                    "type": "text",
                                                                    "text": "ระบบสมาชิก",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "margin": "xs",
                                                    "backgroundColor": "#D39D2B",
                                                    "cornerRadius": "5px",
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "Action",
                                                        "uri": Util().liff_url_logout
                                                    },
                                                    "contents": [
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "baseline",
                                                            "contents": [
                                                                {
                                                                    "type": "spacer"
                                                                },
                                                             
                                                                {
                                                                    "type": "text",
                                                                    "text": "ออกจากระบบ",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "type": "spacer",
                                                            "size": "xl"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }      
            ]
        
        }
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())


# ResponsMenu("Uc1e2655638774e42ab8cf38043744cdb")