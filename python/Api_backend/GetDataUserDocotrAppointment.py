
import requests
import json
import datetime
from python.Util import Util

# import sys, os
# sys.path.append("C:\inetpub\wwwroot\linebot\linebot_webhook\python")
# from Util import Util

class GetDataUserDocotrAppointment:
    
    def __new__(self,user_ad_code):

        date_today = datetime.date.today()

        empCode = "empCode="+str(user_ad_code)
        appmntDay = "&appmntDay="+str(date_today)

        url = Util().api_user_doctor_appointment+empCode+appmntDay

        response = requests.get(url)
        print(response.status_code)

        print(response.json())

        return response.json()
