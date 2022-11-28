
import requests
import json

from python.Util import Util
from python.Api_backend.PostUserWithUid import PostUserWithUid
from python.Api_backend.PostDataPermitSaleReport import PostDataPermitSaleReport
from python.Respons_user.ResponsWorkSystem import ResponsWorkSystem
from python.Respons_user.ResponsReply import ResponsReply

class CheckPermitSaleReport:
    
    def __new__(self,user,user_line_uid):

        try:
            result_user = PostUserWithUid(user_line_uid)
            user_ad_code = str(result_user[0]["user_ad_code"])
            
            
            status_permit = PostDataPermitSaleReport(user_ad_code)
            status = str(status_permit["status"])
            result = status_permit["result"]


            contents_report_sale =  {
                                        "type": "box",
                                        "layout": "vertical",
                                        "backgroundColor": "#d3af04",
                                        "cornerRadius": "5px",
                                        "action": {
                                            "type": "uri",
                                            "label": "Action",
                                            "uri": Util().liff_url_work_system_report_sale,
                                            
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
                                                        "text": "รายงานการขาย",
                                                        "color": "#FFFFFFFF",
                                                        "align": "start",
                                                        "gravity": "center",
                                                        "offsetBottom": "2px",
                                                        "offsetStart": "2px",
                                                        "contents": []
                                                    },
                                        

                                                ]
                                            },

                                            
                                            
                                            {
                                                "type": "spacer",
                                                "size": "xl"
                                            }
                                        ]

                                    }
                            
            contents_period  =  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "xs",
                                    "backgroundColor": "#d3af04",
                                    "cornerRadius": "5px",

                                        "action": {
                                        "type": "uri",
                                        "label": "Action",
                                        "uri": Util().liff_url_work_system_timeatt_period
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
                                                    "text": "ระบบการแลกเปลี่ยนเวร",
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
            
            contents_km_im  =  {
                                    "type": "box",
                                    "layout": "vertical",
                                    "margin": "xs",
                                    "backgroundColor": "#d3af04",
                                    "cornerRadius": "5px",

                                        "action": {
                                        "type": "uri",
                                        "label": "Action",
                                        "uri": Util().km_im_link
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
                                                    "text": "KM & IM",
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
                                    

            contents = []       
            for data in result :
                if data == "1" :
                    # contents.append()
                    contents.append(contents_report_sale)
                elif data == "2" :
                    contents.append(contents_period)
                else :  
                    print()
           
            # ResponsReply(Util().serverToken,user,str(contents))
            # contents.append(contents_km_im)
            ResponsWorkSystem(user,contents)


            # if status_permit == "true":
                # ResponsWorkSystem(user,contents)
            #     # ResponsReply(Util().serverToken,user,"Developing..\uDBC0\uDC84\nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")
            # elif status_permit == "false":
            #     # ResponsWorkSystem(user)
            #     ResponsReply(Util().serverToken,user,"Developing..\uDBC0\uDC84\nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")


     
         
                            
                     

        except:
            ResponsReply(Util().serverToken,user,"Developing..\uDBC0\uDC84\nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")
    




