
import requests
import json

from python.Util import Util

class PostCheckLogin:
    
    def __new__(self,user_line_uid):

        body = {"user_line_uid": str(user_line_uid)}

        response = requests.post(Util().api_check_login, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

        return response.json()

# PostCheckLogin("U4f34652f4e163d5492b3fbe573a50d0a")