
import requests
import json

from python.Util import Util

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util

class PostDataTimeAt:
    
    def __new__(self,user_line_uid):

        body = {"user_line_uid": str(user_line_uid)}

        response = requests.post(Util().api_get_data_time_at_with_uid, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

        return response.json()

# PostDataTimeAt("U4f34652f4e163d5492b3fbe573a50d0a")