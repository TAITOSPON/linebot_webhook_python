
import requests
import json

from python.Util import Util

from python.Respons_user.ResponsContentFlex.ResponsContentFlexTimeatt import ResponsContentFlexTimeatt
from python.Respons_user.ResponsContentFlex.ResponsContentFlexEditTel import ResponsContentFlexEditTel
from python.Respons_user.ResponsContentFlex.ResponsContentFlexLeave import ResponsContentFlexLeave
from python.Respons_user.ResponsContentFlex.ResponsContentFlexVaccine import ResponsContentFlexVaccine



class ResponsTimeAtFlex:
    
    def __init__(self,devicetoken,body):

        status_flex_timeatt,respons_timeatt,content_time = ResponsContentFlexTimeatt(body)
    
        status_flex_leave,content_leave = ResponsContentFlexLeave(body)

        user_ad_code = str(respons_timeatt["result"]["result_user"][0]["user_ad_code"])
        status_flex_vaccine,content_vaccine = ResponsContentFlexVaccine(user_ad_code)

        status_flex_edittel,content_edit_tel = ResponsContentFlexEditTel(user_ad_code)

        if status_flex_leave == "normal":
            
            if status_flex_vaccine == "normal":
                    
                contents = {
                    "type":"carousel",
                    "contents":[
                        
                        content_time,
                        content_edit_tel,
                        content_leave,
                        content_vaccine,

                    ]
                }
            else :
                contents = {
                    "type":"carousel",
                    "contents":[
                        
                        content_time,
                        content_edit_tel,
                        content_leave,
            
                    ]
                }
        else:

            if status_flex_vaccine == "normal":
                    
                contents = {
                    "type":"carousel",
                    "contents":[
                        
                        content_time,
                        content_edit_tel,
                        content_vaccine,

                    ]
                }
                
            else :
                contents = {
                    "type":"carousel",
                    "contents":[
                        
                        content_time,
                        content_edit_tel,
                        
                    ]
                }


       
        body = {    
            "replyToken": str(devicetoken),
            "messages": [
                {
                    "type":"flex",
                    "altText":Util().intent_time_work,
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


# ResponsMenu("Uc1e2655638774e42ab8cf38043744cdb")