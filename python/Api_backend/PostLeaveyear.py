
import requests
import json

from python.Util import Util

class PostLeaveyear:
    
    def __new__(self,user_line_uid,leave_year):


        body = {
            "user_line_uid": str(user_line_uid),
            "leave_year": str(leave_year)
        }

        response = requests.post(Util().api_leave_get_by_year, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

        return response.json()
