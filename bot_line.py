# import json
# import os

# import requests
# import json

# from flask import Flask,render_template
# from flask import request
# from flask import make_response

# from python.ResponsListItem import ResponsListItem
# from python.ResponsNotLogin import ResponsNotLogin
# from python.ResponsQuickReply import ResponsQuickReply
# from python.RequestGet import RequestGet

# # Flask app should start in global layout
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return render_template('login.html')

# @app.route('/webhook', methods=['POST'])
# def webhook():

#     req = request.get_json(silent=True, force=True)
#     res = processRequest(req)
#     res = json.dumps(res, indent=4)
#     r = make_response(res)
#     r.headers['Content-Type'] = 'application/json'
#     return r

# def processRequest(req):
#     # Parsing the POST request body into a dictionary for easy access.
#     req_dict = json.loads(request.data)
#     print(req_dict)
#     # Accessing the fields on the POST request boduy of API.ai invocation of the webhook
#     intent = req_dict["queryResult"]["intent"]["displayName"]
#     uuid = req_dict["originalDetectIntentRequest"]["payload"]["data"]["source"]["userId"]

#     # speech = str(req_dict)
#     # res = makeWebhookResult(speech)

#     if intent == 'request detail':
#         speech = str(req_dict)
#         res = makeWebhookResult(speech)

#     elif intent == 'ลางาน':
#         # alert hot login
#         ResponsNotLogin(str(uuid))
    
#     elif intent == 'ตารางหมอ':
#         # speech = "https://liff.line.me/1654967329-5AMQZKN1"
#         # speech = "coming soon"
#         ResponsListItem(str(uuid)) 

        

#     elif intent == 'จองห้องประชุม':
#         # speech = "coming soon"
#         # res = makeWebhookResult(speech)

#         ResponsListItem(str(uuid)) 
   
#     elif intent == 'ออกจากระบบ':
#         # speech = "coming soon"
#         # res = makeWebhookResult(speech)

#         speech = str(RequestGet())
#         res = makeWebhookResult(speech)

#     elif intent == 'เมนู':

#         ResponsQuickReply(str(uuid))
#         # speech = "coming soon"
#         # res = makeWebhookResult(speech)
       

#     else:
#         speech = "what you want ?"
#         res = makeWebhookResult(speech)


#     # speech = str(req_dict)
#     # res = makeWebhookResult(speech)

#     return res


# def makeWebhookResult(speech):

#     return {"fulfillmentText": speech}

 

# if __name__ == '__main__':
#     port = int(os.getenv('PORT', 5000))

#     print("Starting app on port %d" % port)

#     app.run(debug=False, port=port, host='0.0.0.0', threaded=True)