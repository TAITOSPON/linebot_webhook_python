
import requests
import json

class RequestGet:
    
    def __new__(self):
     
        response = requests.get("http://nuengdevtoat.byethost5.com/Dev/index.php?/api/Api_list/list_user/")
        print(response.status_code)

        # print(response.text)

        return response.text
        # users = json.loads(response.text)
        # for user in users:
        #     print(user)

# print(RequestGet())