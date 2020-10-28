
import requests
import json

from python.Util import Util

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util

class PostLeaveYearSelect:
    
    def __new__(self,user_line_uid):


        body = {
            "user_line_uid": str(user_line_uid)
        }

        response = requests.post(Util().api_leave_get_year_for_select, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

        return response.json()
