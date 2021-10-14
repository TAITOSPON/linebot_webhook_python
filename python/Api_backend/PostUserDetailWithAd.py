
import requests
import json

from python.Util import Util

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util

class PostUserDetailWithAd:
    
    def __new__(self,user_ad_code):

        body = {"user_ad_code": str(user_ad_code)}

        response = requests.post(Util().api_get_user_datail_with_ad, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

        return response.json()

# PostUserWithUid("U4f34652f4e163d5492b3fbe573a50d0a")