
import requests
import json

from python.Util import Util
from python.Api_backend.PostLeaveYearSelect import PostLeaveYearSelect
from python.Api_backend.PostLeaveyear import PostLeaveyear

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util
# from Api_backend.PostLeaveYearSelect import PostLeaveYearSelect

class ResponsLeaveSelectYear:
    
    def __init__(self,body,year):
        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])

        result = PostLeaveYearSelect(user_uid)
        items = []
       
        # data =  '{ "key":"Leave_info", "year":"2564"}'

        # in_item = {
        #     "type": "action",
        #     "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_leave.png",
        #     "action": {
        #         "type": "postback",
        #         "label" : "aaa",
        #         "data": data
        #     }
        # }


        for i in range(len(result)):

            in_item = {
                "type": "action",
                "imageUrl": "https://webhook.toat.co.th/linebot/web/src/icon_leave.png",
                "action": {
                    "type": "postback",
                    "label" : str(result[i]["Value"]),
                    "data": str('{ "key":"'+str(Util().Leave_info)+'", "year":"'+str(result[i]["Value"])+'"}')
                }
            }
            if year == "":
                year = str(result[0]["Value"])

            items.append(in_item) 
        

       
        if year != "":
            respons = PostLeaveyear(user_uid,year)

            user_name = str(respons["result"]["user"]["user_ad_name"])
            SumLeaveYear = str(respons["result"]["leave_head"]["SumLeaveYear"])
            TotalLeave = str(respons["result"]["leave_head"]["TotalLeave"])
            TotalLeaveAvailable = str(respons["result"]["leave_head"]["TotalLeaveAvailable"])

            leave_vacation = respons["result"]["leave_detail"]["leave_vacation"]
            leave_leave = respons["result"]["leave_detail"]["leave_leave"]

            if len(leave_vacation) == 0:
                text_leave_vacation = ""
            else:
                array_leave_vacation = []
                for i in range(len(leave_vacation)):
                    text = "เดือน"+str(leave_vacation[i]["LeaveMM"])+" ปี "+str(leave_vacation[i]["LeaveYY"])+" ลาจำนวน "+str(leave_vacation[i]["LeaveDate"])+" วัน"
                    array_leave_vacation.append(text) 
                

                text_leave_vacation = str("\n\nลาพักผ่อน\n____________________\n"+str(array_leave_vacation)+"\n____________________\n")

            if len(leave_leave) == 0:
                text_leave_leave = ""
            else:
                array_leave_leave = []
                for i in range(len(leave_leave)):
                    text = "เดือน"+str(leave_leave[i]["LeaveMM"])+" ปี "+str(leave_leave[i]["LeaveYY"])+" ลาจำนวน "+str(leave_leave[i]["LeaveDate"])+" วัน"
                    array_leave_leave.append(text) 

                text_leave_leave = str("\n\nลากิจ\n____________________\n"+str(array_leave_leave)+"\n____________________\n")

            text_leave = str("คุณ "+user_name+"\nปีงบประมาณ "+year+"\n\nจำนวนวันลาที่โอนมาจากปีที่แล้ว "+SumLeaveYear+" วัน\nจำนวนวันลาพักผ่อนในปีนี้ "+TotalLeave+" วัน\nจำนวนวันลาพักผ่อนคงเหลือ "+TotalLeaveAvailable+" วัน")


            text_detail_more = str("\n\n\n____________________\nคลิกดูรายละเอียดในระบบสมาชิก\n"+Util().liff_url_profile_detail_leave)
            text = str(text_leave+text_leave_vacation+text_leave_leave+text_detail_more)


 


        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }

        body = {

            "replyToken": str(user),
            "messages": [
            
               {
                    "type": "text",
                    "text": text,
                    "quickReply": {
                        "items": items
                    }
                }
            ]
        }


   
        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())




# ResponsLeaveSelectYear("U4f34652f4e163d5492b3fbe573a50d0a")