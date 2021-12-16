
import requests
import json

from python.Util import Util



class PostDataPermitSaleReport:
    
    def __new__(self,user_ad_code):

        body = {"userid" : str(user_ad_code)}
        
        response = requests.post(Util().api_check_permit_sale_report, data=json.dumps(body) , headers={'Content-Type': 'application/json'})

        print(response.status_code)

        print(response.json())

        return response.json()

# PostUserWithUid("U4f34652f4e163d5492b3fbe573a50d0a")