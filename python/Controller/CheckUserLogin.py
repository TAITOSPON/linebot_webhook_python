
import requests
import json

from python.Api_backend.PostCheckLogin import PostCheckLogin
from python.Respons_user.ResponsNotLogin import ResponsNotLogin

class CheckUserLogin:
    
    def __new__(self,user_line_uid):

        response = PostCheckLogin(user_line_uid)
        if response["status"]:
            return True
        else:
            if response["result"]=="check_login_false":
                ResponsNotLogin(user_line_uid)
            return False


