
import requests
import json

class ResponsQuickReply:
    
    def __init__(self,devicetoken):
        serverToken = '4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU='
        # deviceToken = 'device token here'

        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + serverToken,
            }

        body = {

            "to": devicetoken,
            "messages": [
            
                 {
                    "type": "text",
                    "text": "This Quick Reply!",
                    "quickReply": {
                        "items": [
                            {
                                "type": "action",
                                "action": {
                                    "type": "datetimepicker",
                                    "label": "Select date",
                                    "data": "storeId=12345",
                                    "mode": "datetime",
                                    "initial": "2017-12-25t00:00",
                                    "max": "2018-01-24t23:59",
                                    "min": "2017-12-25t00:00"
                                }
                            },
                            {
                                "type": "action",
                                "action": {
                                    "type": "location",
                                    "label": "Location"
                                }
                            }
                        ]
                    }
                }
            ]

        
        }
        response = requests.post("https://api.line.me/v2/bot/message/push",headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

# ResponsQuickReply("Uc1e2655638774e42ab8cf38043744cdb")