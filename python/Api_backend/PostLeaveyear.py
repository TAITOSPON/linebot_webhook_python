
import requests
import json

from python.Util import Util

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util

class PostLeaveyear:
    
    def __new__(self,user_line_uid,leave_year):


        body = {
            "user_line_uid": str(user_line_uid),
            "leave_year": str(leave_year)
        }

        # print(body)

        response = requests.post(Util().api_leave_get_by_year, data = body)
        print(response.status_code)

        print(response.json())

        return response.json()

# PostLeaveyear("U4f34652f4e163d5492b3fbe573a50d0a","2564")