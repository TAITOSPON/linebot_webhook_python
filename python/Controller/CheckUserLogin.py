
import requests
import json

from python.Api_backend.PostCheckLogin import PostCheckLogin
from python.Respons_user.ResponsNotLogin import ResponsNotLogin

class CheckUserLogin:
    
    def __new__(self,body):

        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])

        response = PostCheckLogin(user_uid)
        if response["status"]:
            return True
        else:
            if response["result"]=="check_login_false":
                ResponsNotLogin(user)
            return False


