import json
import gspread 
from oauth2client.service_account import ServiceAccountCredentials 
from pprint import pprint

from python.Util import Util

class GetDataUserVaccine:

    def __new__(self,user_ad_code):



        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] 
        creds = ServiceAccountCredentials.from_json_keyfile_name("python/Api_backend/connect-sheet-324601.json", scope) 
        client = gspread.authorize(creds) 
        sheet = client.open("Vaccine Recive").sheet1 
        data = sheet.get_all_records() 


   
        string = user_ad_code

        user_code = str(string[0:2] + "-" +string[2:6])

        status = "false"
        for index, user in enumerate(data):

            if str(data[index]['EmpNo']) == user_code:
                data = json.loads(json.dumps(data[index]))
                status = "true"
                return data
    
        if  status != "true":
            return "null"
    


