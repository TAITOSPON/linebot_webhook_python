import json
import requests

from flask import make_response
from flask import Flask,request,render_template

from python.ResponsListItem import ResponsListItem
from python.ResponsNotLogin import ResponsNotLogin
from python.ResponsQuickReply import ResponsQuickReply
from python.RequestGet import RequestGet
# from python.PostToDialog import PostToDialog


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')
  
@app.route('/webhook' , methods = ['POST']) 
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@app.route('/callback', methods=['POST'])
def callback():
  new_event = request.json

  user = new_event["events"][0]['replyToken']

  headers1 = request.headers

  

#   texts = ['ลา']
#   a = PostToDialog("nuengdevtoat-ihq9","nuengdevtoat-ihq9",texts,'th')
  sendText(user,str(new_event))

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



def processRequest(req):
    # Parsing the POST request body into a dictionary for easy access.
    req_dict = json.loads(request.data)
    print(req_dict)
    # Accessing the fields on the POST request boduy of API.ai invocation of the webhook
    intent = req_dict["queryResult"]["intent"]["displayName"]
    uuid = req_dict["originalDetectIntentRequest"]["payload"]["data"]["source"]["userId"]

    speech = str(req_dict)
    res = makeWebhookResult(speech)

    return res


def makeWebhookResult(speech):

    return {"fulfillmentText": speech}


if __name__ == '__main__':
  # app.run(debug=True)

  app.run(debug=False, port='5557', host='172.20.55.46', threaded=True)

