import json
import requests

from flask import make_response
from flask import Flask,request,render_template,url_for

from python.Util import Util

from python.Respons_user.ResponsReply import ResponsReply
from python.Respons_user.ResponsMenu import ResponsMenu
from python.Respons_user.ResponsQuickReply import ResponsQuickReply
from python.Respons_user.ResponsChecklogout import ResponsChecklogout
from python.Respons_user.ResponsLeave import ResponsLeave

from python.Respons_user.ResponsListItem import ResponsListItem

from python.Api_backend.PostToDialog import PostToDialog
from python.Api_backend.PostLogout import PostLogout
from python.Api_backend.PostUserWithUid import PostUserWithUid


from python.Controller.CheckUserLogin import CheckUserLogin
from python.Controller.Leave import Leave



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



@app.route('/webhook', methods=['POST'])
def webhook():
   
    header = request.headers
    body = request.json
    message_type = header["User-Agent"]

    Receive_LineAPI(body)

    return Util().index,200

    

def Receive_LineAPI(body):
    
    event_type = str(body["events"][0]['type'])
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])

    if event_type == "message":
    
        message_type = str(body["events"][0]['message']['type'])

        if message_type == "text":    
            checktextintent(body)
        else :
            ResponsReply(user,str(body))

    elif event_type == "postback":
        postbackdata = str(body["events"][0]["postback"]["data"])
        checkmessagepostback(body,postbackdata)


def checktextintent(body):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])
    text = str(body["events"][0]['message']['text'])

    if str(checktextcase(body,text)) == "False":

    
        response = PostToDialog(Util().key_dialogflow,Util().key_dialogflow,text,Util().key_dialogflow_langu)

        if str(response.query_result.intent.display_name) == Util().Default_Fallback_Intent or str(response.query_result.intent.display_name) == Util().Default_Welcome_Intent:
            ResponsReply(user,str(response.query_result.fulfillment_text))
        else :
            checktextcase(body,str(response.query_result.intent.display_name))


def checktextcase(body,text):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])

    if text == Util().intent_login:
        if CheckUserLogin(body):
            result_user = PostUserWithUid(user_uid)
            user_ad_name = str(result_user[0]["user_ad_name"])
            text = "สวัสดีคุณ "+user_ad_name+" \nยินดีต้อนรับเข้าสู่ระบบ linebot system \nนี่คือระบบต้นแบบที่จะช่วยคุณ"
            ResponsQuickReply(user,text)
        
        return True

    if text == Util().intent_leave:
        if CheckUserLogin(body):
            ResponsLeave(user)
        return True

    elif text == Util().intent_meet:

        if CheckUserLogin(body):
            ResponsReply(user,"กำลังพัฒนา")
        return True

    elif text == Util().intent_menu:
        
        ResponsMenu(user)
        return True

    elif text == Util().intent_logout:
        ResponsChecklogout(user)
        return True

    return False


def checkmessagepostback(body,postbackdata):
    user_uid = str(body["events"][0]['source']['userId'])
    user = str(body["events"][0]['replyToken'])

    postbackdata = json.loads(str(postbackdata))
    key = str(postbackdata["key"])
    
    if CheckUserLogin(body):
        if key == Util().Leave_info:   
            Leave(body,postbackdata)
       
        elif key == Util().User_logout:
            
            response = PostLogout(user_uid)
            
            if response["status"]:
                ResponsReply(user,"ออกจากระบบสำเร็จ")
            else:
                ResponsReply(user,"ออกจากระบบไม่สำเร็จ")
        else:
            print()
    

if __name__ == '__main__':
    app.run()