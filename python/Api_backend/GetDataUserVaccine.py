import json
import datetime
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint

from python.Util import Util

class GetDataUserVaccine:

    def __new__(self,user_ad_code):
       
        try:
            date = datetime.datetime.now()
            date_today = datetime.date.today()

            read = open("python/Api_backend/data_vaccine/data_vac.json", "r")
            json_string = read.read()



            json_obj = json.loads(json_string)
            data_use = json_obj["data"]
            data_date = json_obj["date"]


            date_form_read = datetime.date(json_obj["date"]["year"], json_obj["date"]["month"], json_obj["date"]["day"])


            if date_today != date_form_read :

                scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 
                creds = ServiceAccountCredentials.from_json_keyfile_name("python/Api_backend/data_vaccine/connect-sheet-324601.json", scope) 
                client = gspread.authorize(creds) 
                sheet = client.open("Vaccine Recive").sheet1 
                data = sheet.get_all_records() 

                json_string = {
                    "date" : {
                        "day" : date.day,
                        "month" : date.month,
                        "year" : date.year
                    },
                    "data": data
                }


                json_obj = json.dumps(json_string)
            
                write = open("python/Api_backend/data_vaccine/data_vac.json", "w")
                write.write(str(json_obj))
                write.close()

                
                read = open("python/Api_backend/data_vaccine/data_vac.json", "r")
                json_string = read.read()

                json_obj = json.loads(json_string)
                data_use = json_obj["data"]


                string = user_ad_code

                user_code = str(string[0:2] + "-" +string[2:6])

                status = "false"
                for index, user in enumerate(data_use):

                    if str(data_use[index]['EmpNo']) == user_code:
                        data = json.loads(json.dumps(data_use[index]))
                        status = "true"
                        return data
            
                if  status != "true":
                    return "null"
                
            

            else :

                string = user_ad_code

                user_code = str(string[0:2] + "-" +string[2:6])

                status = "false"
                for index, user in enumerate(data_use):

                    if str(data_use[index]['EmpNo']) == user_code:
                        data = json.loads(json.dumps(data_use[index]))
                        status = "true"
                        return data
            
                if  status != "true":
                    return "null"
                    
        except:

            scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 
            creds = ServiceAccountCredentials.from_json_keyfile_name("python/Api_backend/data_vaccine/connect-sheet-324601.json", scope) 
            client = gspread.authorize(creds) 
            sheet = client.open("Vaccine Recive").sheet1 
            data = sheet.get_all_records() 


    
            string = user_ad_code

            user_code = str(string[0:2] + "-" +string[2:6])

            status = "false"
            for index, user in enumerate(data_use):

                if str(data_use[index]['EmpNo']) == user_code:
                    data = json.loads(json.dumps(data_use[index]))
                    status = "true"
                    return data
        
            if  status != "true":
                return "null"
    


