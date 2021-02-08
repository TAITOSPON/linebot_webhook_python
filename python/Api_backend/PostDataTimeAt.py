
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



        # date_ = {
        #     "status": "true",
        #     "result": {
        #         "result_user": {
        #             "status": "true",
        #             "result": [
        #                 {
        #                     "user_connect_id": "15",
        #                     "user_ad_code": "003596",
        #                     "user_line_uid": "U49d9a81fa28bc62750a330ca8413b393",
        #                     "user_connect_status": "true"
        #                 }
        #             ]
        #         },
        #         "result_time_at": [
        #             {
        #                 "Emp_Code": "003596",
        #                 "dept_code": "19010400",
        #                 "fullname": "กษน พิลาฤทธิ์",
        #                 "Stamp_Date": "2021-02-05",
        #                 "in_CHK": "07:35:22",
        #                 "in_status": "OK",
        #                 "in_location": "100",
        #                 "in_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "in_channel": "LINE_KT",
        #                 "out_CHK": "15:17:59",
        #                 "out_status": "Before",
        #                 "out_location": "100",
        #                 "out_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "out_channel": "LINE_KT"
        #             },
        #             {
        #                 "Emp_Code": "003596",
        #                 "dept_code": "19010400",
        #                 "fullname": "กษน พิลาฤทธิ์",
        #                 "Stamp_Date": "2021-02-05",
        #                 "in_CHK": "07:35:22",
        #                 "in_status": "OK",
        #                 "in_location": "100",
        #                 "in_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "in_channel": "LINE_KT",
        #                 "out_CHK": "16:16:09",
        #                 "out_status": "OK",
        #                 "out_location": "100",
        #                 "out_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "out_channel": "LINE_KT"
        #             }
        #         ]
        #     }
        # }


        # return date_


        # nueng = {
        #     "status": "true",
        #     "result": {
        #         "result_user": {
        #             "status": true,
        #             "result": [
        #                 {
        #                     "user_connect_id": "14",
        #                     "user_ad_code": "003599",
        #                     "user_line_uid": "U4f34652f4e163d5492b3fbe573a50d0a",
        #                     "user_connect_status": "true"
        #                 }
        #             ]
        #         },
        #         "result_time_at": [
        #             {
        #                 "Emp_Code": "003599",
        #                 "dept_code": "19010300",
        #                 "fullname": "ทศพล โพชะเรือง",
        #                 "Stamp_Date": "2021-02-05",
        #                 "in_CHK": "07:42:45",
        #                 "in_status": "OK",
        #                 "in_location": 100,
        #                 "in_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "in_channel": "LINE_KT",
        #                 "out_CHK": "15:12:59",
        #                 "out_status": "Before",
        #                 "out_location": 100,
        #                 "out_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "out_channel": "LINE_KT"
        #             },
        #             {
        #                 "Emp_Code": "003599",
        #                 "dept_code": "19010300",
        #                 "fullname": "ทศพล โพชะเรือง",
        #                 "Stamp_Date": "2021-02-05",
        #                 "in_CHK": "07:42:45",
        #                 "in_status": "OK",
        #                 "in_location": 100,
        #                 "in_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "in_channel": "LINE_KT",
        #                 "out_CHK": "16:27:33",
        #                 "out_status": "OK",
        #                 "out_location": 100,
        #                 "out_location_name": "LINE@ TOAT การยาสูบแห่งประเทศไทย คลองเตย กรุงเทพฯ ",
        #                 "out_channel": "LINE_KT"
        #             }
        #         ]
        #     }
        # }

# PostDataTimeAt("U4f34652f4e163d5492b3fbe573a50d0a")