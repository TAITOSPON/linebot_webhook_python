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

    user = body["events"][0]['replyToken']
    user_uid = body["events"][0]['source']['userId']
    message_type = body["events"][0]['message']['type']

    
    if message_type == "text":    
        result = PostToDialog("nuengdevtoat-ihq9","nuengdevtoat-ihq9",str(body["events"][0]['message']['text']),'th')
        checktextcase(str(user),str(user_uid),str(result))

    else :
        print(str(message_type))
        # sendText(user,str(message_type))

    return '',200


def checktextcase(user,user_uid,text):
    if text == "ลางาน":
        print()
        ResponsNotLogin(user_uid)
    elif text == "จองห้องประชุม":
        print()
    elif text == "เมนู":
        ResponsMenu(user_uid)
    else:
        sendText(user,text)




def sendText(user,text):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer 4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
    headers = {'Content-Type': 'application/json; charset=UTF-8', 'Authorization':Authorization}
    data = json.dumps({"replyToken":user, "messages":[{"type":"text","text":text}]})

    result = requests.post(LINE_API, headers=headers, data=data) 



if __name__ == '__main__':
    app.run()