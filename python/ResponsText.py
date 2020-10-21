
import requests
import json

class ResponsText:
    
    def __init__(self,serverToken,devicetoken,text):
        # serverToken = '4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU='
        # deviceToken = 'device token here'

        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' +  str(serverToken),
            }

        body = {

            "to": str(devicetoken),
            "messages": [
                {
                    "type": "text",
                    "text": str(text)
                }
            ]

        
        }
        response = requests.post("https://api.line.me/v2/bot/message/push",headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

# ResponsQuickReply("Uc1e2655638774e42ab8cf38043744cdb")