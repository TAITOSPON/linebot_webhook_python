from python.Respons_user.ResponsReply import ResponsReply
from python.Api_backend.PostLeaveyear import PostLeaveyear

from python.Respons_user.ResponsLeaveSelectYear import ResponsLeaveSelectYear

class Leave:
    
    def __new__(self,body,year):

        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])
     
      
        ResponsLeaveSelectYear(body,year)
        
        # if year != "":
        #     respons = PostLeaveyear(user_uid,year)

        #     user_name = str(respons["result"]["user"]["user_ad_name"])
        #     SumLeaveYear = str(respons["result"]["leave_head"]["SumLeaveYear"])
        #     TotalLeave = str(respons["result"]["leave_head"]["TotalLeave"])
        #     TotalLeaveAvailable = str(respons["result"]["leave_head"]["TotalLeaveAvailable"])

        #     leave_vacation = respons["result"]["leave_detail"]["leave_vacation"]
        #     leave_leave = respons["result"]["leave_detail"]["leave_leave"]

        #     if len(leave_vacation) == 0:
        #         text_leave_vacation = ""
        #     else:
        #         array_leave_vacation = []
        #         for i in range(len(leave_vacation)):
        #             text = "เดือน"+str(leave_vacation[i]["LeaveMM"])+" ปี "+str(leave_vacation[i]["LeaveYY"])+" ลาจำนวน "+str(leave_vacation[i]["LeaveDate"])+" วัน"
        #             array_leave_vacation.append(text) 
                

        #         text_leave_vacation = str("\n\nลาพักร้อน\n"+str(array_leave_vacation))

        #     if len(leave_leave) == 0:
        #         text_leave_leave = ""
        #     else:
        #         array_leave_leave = []
        #         for i in range(len(leave_leave)):
        #             text = "เดือน"+str(leave_leave[i]["LeaveMM"])+" ปี "+str(leave_leave[i]["LeaveYY"])+" ลาจำนวน "+str(leave_leave[i]["LeaveDate"])+" วัน"
        #             array_leave_leave.append(text) 

        #         text_leave_leave = str("\n\nลากิจ\n"+str(array_leave_leave))

        #     text_leave = str(user_name+"\nปีงบประมาณ "+year+"\n\nจำนวนวันลาที่โอนมาจากปีที่แล้ว "+SumLeaveYear+" วัน\nจำนวนวันลาพักผ่อนในปีนี้ "+TotalLeave+" วัน\nจำนวนวันลาพักผ่อนคงเหลือ "+TotalLeaveAvailable+" วัน")
        #     text = str(text_leave+text_leave_vacation+text_leave_leave)
        #     # ResponsReply(user,text)
        #     ResponsLeaveSelectYear(body,text)
        # else:       
        #     ResponsLeaveSelectYear(body,"เลือกปีงบประมาณ")

        

