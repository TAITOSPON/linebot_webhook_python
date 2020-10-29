import json
import requests

from flask import make_response
from flask import Flask,request,render_template,url_for

from python.Util import Util

from python.Respons_user.ResponsReply import ResponsReply
from python.Respons_user.ResponsText import ResponsText
from python.Respons_user.ResponsMenu import ResponsMenu
from python.Respons_user.ResponsListItem import ResponsListItem
from python.Respons_user.ResponsQuickReply import ResponsQuickReply
from python.Respons_user.ResponsChecklogout import ResponsChecklogout

from python.Respons_user.ResponsLeave import ResponsLeave
# from python.Respons_user.ResponsLeaveSelectYear import ResponsLeaveSelectYear

from python.Api_backend.PostToDialog import PostToDialog
from python.Api_backend.PostLogout import PostLogout

from python.Api_backend.PostCheckLogin import PostCheckLogin

from python.Controller.CheckUserLogin import CheckUserLogin

# from python.Api_backend.PostLeaveyear import PostLeaveyear

from python.Controller.Leave import Leave



app = Flask(__name__)

class PrefixMiddleware(object):
#class for URL sorting 
    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):
        #in this line I'm doing a replace of the word flaskredirect which is my app name in IIS to ensure proper URL redirect
        if environ['PATH_INFO'].lower().replace('/linebot','').startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'].lower().replace('/linebot','')[len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])            
            return ["This url does not belong to the app.".encode()]


app.wsgi_app = PrefixMiddleware(app.wsgi_app, prefix='/webhook')


@app.route("/")
def hello():
    return Util().index


@app.route('/webhook', methods=['POST'])
def webhook():
   
    header = request.headers
    body = request.json
    message_type = header["User-Agent"]
    


    if message_type == "login-true": 
        Receive_Backend(body)
    else:
        Receive_LineAPI(body)

    return Util().index,200



def Receive_Backend(body):

    user_uid = str(body["user_line_uid"])
    text = "สวัสดีคุณ "+body["PERSON_NAME"]+" \nยินดีต้อนรับเข้าสู่ระบบ linebot system \nนี่คือระบบต้นแบบที่จะช่วยคุณ"
    ResponsText(user_uid,text)
    ResponsQuickReply(user_uid,"เลือกเมนูที่คุณต้องการใช้งาน")

    

def Receive_LineAPI(body):
    
    event_type = str(body["events"][0]['type'])
    user_uid = str(body["events"][0]['source']['userId'])

    if event_type == "message":
    
        message_type = str(body["events"][0]['message']['type'])

        if message_type == "text":    
            checktextintent(body)
        else :
            ResponsText(user_uid,body)

    elif event_type == "postback":
        # ResponsText(user_uid,str(body["events"]))
        postbackdata = str(body["events"][0]["postback"]["data"])
        checkmessagepostback(body,postbackdata)


def checktextintent(body):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])
    text = str(body["events"][0]['message']['text'])

    if str(checktextcase(body,text)) == "False":

    
        response = PostToDialog(Util().key_dialogflow,Util().key_dialogflow,text,Util().key_dialogflow_langu)

        if str(response.query_result.intent.display_name) == Util().Default_Fallback_Intent or str(response.query_result.intent.display_name) == Util().Default_Welcome_Intent:
            ResponsText(user_uid,str(response.query_result.fulfillment_text))
        else :
            # ResponsText(user_uid,str(response.query_result.intent.display_name))
            checktextcase(body,str(response.query_result.intent.display_name))



def checktextcase(body,text):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])

    if text == Util().intent_leave:

        if CheckUserLogin(user_uid):
            ResponsLeave(user_uid)
        return True

    elif text == Util().intent_meet:

        if CheckUserLogin(user_uid):
            ResponsText(user_uid,"กำลังพัฒนา (รอ API )")
       
        return True

    elif text == Util().intent_menu:
        
        ResponsMenu(user_uid)
        return True

    elif text == Util().intent_logout:


        # ResponsChecklogout(user_uid)

        response = PostLogout(user_uid)
        
        if response["status"]:
            ResponsReply(user,"ออกจากระบบสำเร็จ")
        else:
            ResponsReply(user,"ออกจากระบบไม่สำเร็จ")
        
        return True

    return False


def checkmessagepostback(body,postbackdata):
    user_uid = str(body["events"][0]['source']['userId'])
    # ResponsText(user_uid, str(postbackdata))

    postbackdata = json.loads(str(postbackdata))
    key = str(postbackdata["key"])
    
    if CheckUserLogin(user_uid):
        if key == Util().Leave_info:   
            Leave(user_uid,postbackdata)
        else:
            print()
            # ResponsText(user_uid,"in else")



# def leave(user_uid,postbackdata):

#     year = str(postbackdata["year"])
#     if year != "":
#         # ResponsText(user_uid,year)
#         respons = PostLeaveyear(user_uid,year)

#         user_name = str(respons["result"]["user"]["user_ad_name"])
#         SumLeaveYear = str(respons["result"]["leave_head"]["SumLeaveYear"])
#         TotalLeave = str(respons["result"]["leave_head"]["TotalLeave"])
#         TotalLeaveAvailable = str(respons["result"]["leave_head"]["TotalLeaveAvailable"])

#         leave_vacation = respons["result"]["leave_detail"]["leave_vacation"]
#         leave_leave = respons["result"]["leave_detail"]["leave_leave"]

#         if len(leave_vacation) == 0:
#             text_leave_vacation = ""
#         else:
#             array_leave_vacation = []
#             for i in range(len(leave_vacation)):
#                 text = "เดือน"+str(leave_vacation[i]["LeaveMM"])+" ปี "+str(leave_vacation[i]["LeaveYY"])+" ลาจำนวน "+str(leave_vacation[i]["LeaveDate"])+" วัน"
#                 array_leave_vacation.append(text) 
            

#             text_leave_vacation = str("\n\nลาพักร้อน\n"+str(array_leave_vacation))
#             # ResponsText(user_uid,text_leave_vacation)

#         if len(leave_leave) == 0:
#             text_leave_leave = ""
#         else:
#             array_leave_leave = []
#             for i in range(len(leave_leave)):
#                 text = "เดือน"+str(leave_leave[i]["LeaveMM"])+" ปี "+str(leave_leave[i]["LeaveYY"])+" ลาจำนวน "+str(leave_leave[i]["LeaveDate"])+" วัน"
#                 array_leave_leave.append(text) 

#             text_leave_leave = str("\n\nลากิจ\n"+str(array_leave_leave))
#             # ResponsText(user_uid,text_leave_leave)

#         text_leave = str(user_name+"\nปีงบประมาณ "+year+"\n\nจำนวนวันลาที่โอนมาจากปีที่แล้ว "+SumLeaveYear+" วัน\nจำนวนวันลาพักร้อนในปีนี้ "+TotalLeave+" วัน\nจำนวนวันลาพักร้อนคงเหลือ "+TotalLeaveAvailable+" วัน")
#         text = str(text_leave+text_leave_vacation+text_leave_leave)
#         ResponsText(user_uid,text)
#         ResponsLeaveSelectYear(user_uid)
#     else:       
#         ResponsLeaveSelectYear(user_uid)


if __name__ == '__main__':
    app.run()