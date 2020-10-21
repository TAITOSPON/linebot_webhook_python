import json
import requests

from flask import make_response
from flask import Flask,request,render_template,url_for

from python.ResponsListItem import ResponsListItem
from python.ResponsNotLogin import ResponsNotLogin
from python.ResponsMenu import ResponsMenu
from python.PostToDialog import PostToDialog
from python.ResponsQuickReply import ResponsQuickReply
from python.RequestGet import RequestGet
from python.ResponsText import ResponsText
from python.PostCheckLogin import PostCheckLogin
from python.PostLogout import PostLogout


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
    return "THIS LINEBOT WEBHOOK SERVER!"


@app.route('/webhook', methods=['POST'])
def webhook():
   
    header = request.headers
    body = request.json
    message_type = header["User-Agent"]

    if message_type == "login-true": 
        Receive_Backend(header,body)
    else:
        Receive_LineAPI(header,body)

    return "THIS LINEBOT WEBHOOK SERVER!",200



def Receive_Backend(header,body):

    user_uid = body["user_line_uid"]
    user_name = "สวัสดีคุณ "+body["PERSON_NAME"]+" \nRock"
    ResponsText(serverToken,user_uid,user_name)

def Receive_LineAPI(header,body):
    
    user_uid = body["events"][0]['source']['userId']
    user = body["events"][0]['replyToken']
    message_type = body["events"][0]['message']['type']

    if message_type == "text":    

        text = str(body["events"][0]['message']['text'])

        if str(checktextcase(str(user),str(user_uid),text)) == "false":
         
            response = PostToDialog("linebot-toat-kyur","linebot-toat-kyur",text,'th')
            # response = PostToDialog("nuengdevtoat-ihq9","nuengdevtoat-ihq9",text,'th')

            if str(response.query_result.intent.display_name) == "Default Fallback Intent" or str(response.query_result.intent.display_name) == "Default Welcome Intent":
                 sendText(user,str(response.query_result.fulfillment_text))
            else :
                checktextcase(str(user),str(user_uid),str(response.query_result.intent.display_name))

    else :
        print(str(message_type))
        # sendText(user,str(message_type))


def checktextcase(user,user_uid,text):

    if text == "ลางาน":

        if checklogin(user,user_uid):
            sendText(user,"ลางานได้")
        else:
            ResponsNotLogin(serverToken,user_uid)

        return "true"
    elif text == "จองห้องประชุม":
        ResponsQuickReply(serverToken,user_uid)
        return "true"
    elif text == "เมนู":
        ResponsMenu(serverToken,user_uid)
        return "true"
    elif text == "ออกจากระบบ":
        response = PostLogout(user_uid)

        if response["status"] == True:
            sendText(user,"ออกจากระบบสำเร็จ")
        else:
            sendText(user,"ออกจากระบบไม่สำเร็จ")
      
        return "true"

    return  "false" 


def checklogin(user,user_uid):

    statuslogin = PostCheckLogin(user_uid)
    # sendText(user,str(statuslogin))

    if statuslogin == "notlogin":
        return False
    else :
        return True
   


def sendText(user,text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer '+serverToken
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization':Authorization}
    data = json.dumps({"replyToken":user, "messages":[{"type":"text","text":text}]})

    result = requests.post(LINE_API, headers=headers, data=data) 

# serverToken = "4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU="
serverToken = "1L1a7UVuYGa2A84PEq8AYl5tN6AkrgBO8/1eTch7Y7ttQ2EjrIV8aaAnjNN2wnzBhTOAKvNCIBHraMJjpVW4W92y72z1nRS+HNxxfStKTCUU/AVbl2qYlPIwITdcmMgLNIR0RfnzfiNl7wvv14vnLAdB04t89/1O/w1cDnyilFU="

if __name__ == '__main__':
    app.run()