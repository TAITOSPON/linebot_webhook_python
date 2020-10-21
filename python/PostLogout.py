
import requests
import json

class PostLogout:
    
    def __new__(self,user_line_uid):
        # serverToken = '4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU='
        # deviceToken = 'device token here'

    
        body = {"user_line_uid": str(user_line_uid)}

        response = requests.post("https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_logout", data=json.dumps(body))
        print(response.status_code)

        print(response.json())

        return response.json()

# PostLogout("U4f34652f4e163d5492b3fbe573a50d0a")