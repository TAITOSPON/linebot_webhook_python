
import requests
import json

from python.Util import Util

class ResponsMenu:
    
    def __init__(self,serverToken,devicetoken):
       
        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + serverToken
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
                                      "alignItems": "flex-end",
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

                                                # {
                                                #     "type": "icon",
                                                #     "url": "https://webhook.toat.co.th/linebot/web/src/LOGO_82.png",
                                                #     "size": "5xl"
                                                # }

                                               
                                            ]
                                        },
                                         
                                        # {
                                        #     "type": "box",
                                        #     "layout": "baseline",
                                        #     "contents": [
                                        #         {
                                        #             "type": "icon",
                                        #             "url": "https://webhook.toat.co.th/linebot/web/src/LOGO_82.png",
                                        #             "size": "5xl"
                                        #         }
                                        #     ]
                                        # },

                                      
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "text",
                                                    "align": "end",
                                                    "text": " ",
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
                                                        "uri": Util().liff_url_profile_detail,
                                                        "altUri": {
                                                            "desktop" : Util().url_profile_detail+"detailprofile"
                                                        }
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
                                                        "uri": Util().liff_url_profile_detail_searchtelephonenumber,
                                                        "altUri": {
                                                            "desktop" : Util().url_profile_detail+"searchtelephonenumber"
                                                        }
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
                                                                    "text": Util().intent_searchtelephonenumber,
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
                                                        "uri": Util().liff_url_profile_detail_financial,
                                                        "altUri": {
                                                            "desktop" : Util().url_profile_detail+"financial"
                                                        }
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
                                                                    "text":  Util().intent_financial,
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
                                                        "uri": Util().liff_url_profile_detail_cooperativesaving,
                                                        "altUri": {
                                                            "desktop" : Util().url_profile_detail+"cooperativesaving"
                                                        }
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
                                                                    "text": Util().intent_cooperativesaving,
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
                                                        "uri": "https://www.facebook.com/177054399691705/posts/953322305398240/"
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
                                                                    "text": " รพ.สวนเบญจกิติฯ",
                                                                    "color": "#FFFFFFFF",
                                                                    "align": "start",
                                                                    "gravity": "center",
                                                                    "offsetBottom": "2px",
                                                                    "offsetStart": "2px",
                                                                    "contents": []
                                                                },

                                                                {
                                                                    "type": "icon",
                                                                    "url": "https://webhook.toat.co.th/linebot/web/src/facebook_icon.png",
                                                                    "size" : "xl"
                                                                    
                                                                }, 
                                                                {
                                                                    "type": "icon",
                                                                    "url": "https://webhook.toat.co.th/linebot/web/src/trans.png",
                                                                    "size" : "sm"
                                                                }, 
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
                                                        "text": Util().help_center
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
                                                                    "text": Util().help_center,
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
                                            ]
                                        }
                                    ]
                                },


                                
                              
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