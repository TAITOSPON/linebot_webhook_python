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
#app.debug = True

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
  
    event = request.json

    user = event["events"][0]['replyToken']

    message_type = event["events"][0]['message']['type']

    headers1 = request.headers

    if message_type == "text":    
        ResponsQuickReply("Uc1e2655638774e42ab8cf38043744cdb")   
        # texts = ['ประชุม']
        # a = PostToDialog("nuengdevtoat-ihq9","nuengdevtoat-ihq9",texts,'th')
        # print('nueng = ',a)
        # sendText(user,a)

    # sendText(user,str(message_type))
    
    return '',200





def sendText(user,text):
  LINE_API = 'https://api.line.me/v2/bot/message/reply'
  Authorization = 'Bearer 4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU=' # ใส่ ENTER_ACCESS_TOKEN เข้าไป
  headers = {
  'Content-Type': 'application/json; charset=UTF-8',
  'Authorization':Authorization}
  data = json.dumps({
  "replyToken":user,
  "messages":[{"type":"text","text":text}]})


  r = requests.post(LINE_API, headers=headers, data=data) 
  #print(r.text)

if __name__ == '__main__':
    app.run()