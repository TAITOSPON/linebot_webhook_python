import json
import requests

from flask import make_response
from flask import Flask,request,render_template,url_for

from python.ResponsListItem import ResponsListItem
from python.ResponsNotLogin import ResponsNotLogin
from python.ResponsMenu import ResponsMenu
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

@app.route('/callback', methods=['POST'])
def callback():
  new_event = request.json

  user = new_event["events"][0]['replyToken']

  headers1 = request.headers

  return '',200

if __name__ == '__main__':
    app.run()