import json
import requests

from flask import make_response
from flask import Flask,request,render_template,url_for

from python.Util import Util

from python.Respons_user.ResponsReply import ResponsReply
from python.Respons_user.ResponsStick import ResponsStick
from python.Respons_user.ResponsMenu import ResponsMenu

from python.Respons_user.ResponsQuickReply import ResponsQuickReply
from python.Respons_user.ResponsChecklogout import ResponsChecklogout
from python.Respons_user.ResponsLogout import ResponsLogout

from python.Respons_user.ResponsListItem import ResponsListItem
from python.Respons_user.ResponsTimeAtFlex import ResponsTimeAtFlex
from python.Respons_user.ResponsTimeAtFlexAndVaccine import ResponsTimeAtFlexAndVaccine
from python.Respons_user.ResponsMemberFlex import ResponsMemberFlex
from python.Respons_user.ResponsPushmessage import ResponsPushmessage
from python.Respons_user.ResponsItemHos import ResponsItemHos

from python.Respons_user.ResponsFlextest import ResponsFlextest


from python.Api_backend.PostToDialog import PostToDialog
from python.Api_backend.PostCheckLogin import PostCheckLogin
from python.Api_backend.PostLogout import PostLogout
from python.Api_backend.PostUserWithUid import PostUserWithUid

from python.Controller.CheckUserLogin import CheckUserLogin
from python.Controller.Leave import Leave
from python.Controller.TimeAt import TimeAt
from python.Controller.TimeThai import TimeThai


from python.Respons_user.ResponsHelpCenter import ResponsHelpCenter


app = Flask(__name__)

class PrefixMiddleware(object):

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

@app.route("/datenow")
def datenow():
    return TimeThai()



@app.route('/webhook', methods=['POST'])
def webhook():

    
    header = request.headers
    body = request.json

    if str(header["User-Agent"]) == "back_end_Covid":
        Recrive_BackEnd(body)
    elif str(header["User-Agent"]) == "back_end_Member":
        Recrive_BackEnd(body)
    else:
        Recrive_LineAPI(body)
    
    return Util().index,200



def Recrive_BackEnd(body):

    devicetoken = str(body[0]['devicetoken'])
    text = str(body[0]['text'])
    ResponsPushmessage(devicetoken,text)



def Recrive_LineAPI(body):
    
    event_type = str(body["events"][0]['type'])
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])

    if event_type == "message": 
        message_type = str(body["events"][0]['message']['type'])

        if message_type == "text":  
            checktextintent(body)

        elif message_type == "sticker":
            text = "ให้ฉันช่วยอะไรคะ"
            ResponsQuickReply(user,text)
            print()
        else :
            text = "ให้ฉันช่วยอะไรคะ"
            ResponsQuickReply(user,text)
            print()

    elif event_type == "postback":
        postbackdata = str(body["events"][0]["postback"]["data"])
        checkmessagepostback(body,postbackdata)

    # if user_uid == "U4f34652f4e163d5492b3fbe573a50d0a":

    #     if event_type == "message":
        
    #         message_type = str(body["events"][0]['message']['type'])

    #         if message_type == "text":    
    #             checktextintent(body)
    #         else :
    #             ResponsReply(Util().serverToken,user,str(body))

    #     elif event_type == "postback":
    #         postbackdata = str(body["events"][0]["postback"]["data"])
    #         checkmessagepostback(body,postbackdata)
    # else:
    #     ResponsReply(Util().serverToken,user,Util().Maintenance)


def checktextintent(body):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])
    text = str(body["events"][0]['message']['text'])

    if str(checktextcase(body,text)) == "False":

        response = PostToDialog(Util().key_dialogflow,Util().key_dialogflow,text,Util().key_dialogflow_langu)

        if str(response.query_result.intent.display_name) == Util().Default_Fallback_Intent or str(response.query_result.intent.display_name) == Util().Default_Welcome_Intent:
            # ResponsReply(Util().serverToken,user,str(response.query_result.fulfillment_text))
            text = str(response.query_result.fulfillment_text) +" ให้ฉันช่วยอะไรคะ"
            ResponsQuickReply(user,text)
        else :
            checktextcase(body,str(response.query_result.intent.display_name))


def checktextcase(body,text):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])
    destination = str(body["destination"])

    if destination == Util().destination:

        if text == Util().intent_login:
            if CheckUserLogin(body):
                result_user = PostUserWithUid(user_uid)
                user_ad_name = str(result_user[0]["user_ad_name"])
                text = "สวัสดีคุณ "+user_ad_name+" \nขอต้อนรับเข้าสู่ระบบ LINE TOAT CHATBOT \nนี่คือระบบที่ช่วยให้คุณทำงานได้เร็วขึ้น"
                ResponsQuickReply(user,text)
            
            return True

        elif text == Util().intent_profile_sys:
            if CheckUserLogin(body):
                ResponsMemberFlex(user,body,Util().intent_profile_sys,Util().liff_url_profile_detail)
                # ResponsReply(Util().serverToken,user,Util().intent_profile_sys)
            return True

        elif text == Util().intent_leave:
            if CheckUserLogin(body):
                ResponsMemberFlex(user,body,Util().intent_leave,Util().liff_url_profile_detail_leave)
                # Leave(body,"")
            return True

        elif text == Util().intent_financial:
            if CheckUserLogin(body):
                ResponsMemberFlex(user,body,Util().intent_financial,Util().liff_url_profile_detail_financial)
            return True

        elif text == Util().intent_cooperativesaving:
            if CheckUserLogin(body):
                ResponsMemberFlex(user,body,Util().intent_cooperativesaving,Util().liff_url_profile_detail_cooperativesaving)
            return True

        elif text == Util().intent_searchtelephonenumber:
            if CheckUserLogin(body):
                ResponsMemberFlex(user,body,Util().intent_searchtelephonenumber,Util().liff_url_profile_detail_searchtelephonenumber)
            return True

        elif text == Util().intent_time_work:
            if CheckUserLogin(body):
                ResponsTimeAtFlex(user,body)
                # ResponsTimeAtFlexAndVaccine(user,body)
            return True

        elif text == Util().intent_time_att:
            if CheckUserLogin(body):
                ResponsMemberFlex(user,body,Util().intent_time_att,Util().liff_url_time_stamp)
            return True 

        elif text == Util().intent_meet:
            if CheckUserLogin(body):
                ResponsReply(Util().serverToken,user,"กำลังพัฒนาจ้า ใจเย็นๆนะจ๊ะ\uDBC0\uDC84\n\nคณะวิเคราะห์สารสนเทศ \nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")
            return True

        elif text == Util().intent_menu:
            ResponsMenu(Util().serverToken,user)
            return True
        
        elif text == Util().intent_hos_ben:
            ResponsItemHos(user)
            return True
        
        elif text == Util().intent_covid:
            ResponsListItem(user)
            return True

        elif text == Util().intent_covid_form:
            CheckUserLogin(body)
            return True
        elif text == Util().intent_covid_confrim:
            CheckUserLogin(body)
            return True

        elif text == Util().help_center:
            if CheckUserLogin(body):
                ResponsHelpCenter(user)
            return True

        elif text == Util().intent_logout:
    
            response = PostCheckLogin(user_uid)
            if response["status"]:
                ResponsChecklogout(user)
            else:
                response = PostLogout(user_uid)
                if response["status"]:
                    ResponsLogout(user,"ออกจากระบบสำเร็จ")
                else:
                    ResponsReply(Util().serverToken,user,"ออกจากระบบไม่สำเร็จ")

            return True



        elif text == "Nuengdev":
       
            # ResponsFlextest(user,body)
            ResponsReply(Util().serverToken,user,  str( body ))
            return True

        return False
        



    elif destination == Util().destination_dev:
       
        if text == "Nuengdev":
            ResponsReply(Util().serverToken_dev,user,str(body))
            return True
        elif text == Util().intent_menu:
            ResponsMenu(Util().serverToken_dev,user)
            return True
        else:
            ResponsReply(Util().serverToken_dev,user,str(body))
            return True

        return False

    return False

def checkmessagepostback(body,postbackdata):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])

    postbackdata = json.loads(str(postbackdata))
    key = str(postbackdata["key"])
    
    if CheckUserLogin(body):
        if key == Util().Leave_info:   
            Leave(body,str(postbackdata["year"]))
       
        elif key == Util().User_logout:
            
            response = PostLogout(user_uid)
            
            if response["status"]:
                ResponsLogout(user,"ออกจากระบบสำเร็จ")
            else:
                ResponsReply(Util().serverToken,user,"ออกจากระบบไม่สำเร็จ")

        elif key == Util().intent_time_work:
            ResponsReply(Util().serverToken,user,"กำลังพัฒนาอยู่จ้า ใจเย็นๆนะจ๊ะ\uDBC0\uDC30\uDBC0\uDC3B\uDBC0\uDC37")
        else:
            print()


if __name__ == '__main__':
    app.run()