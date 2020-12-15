from python.Respons_user.ResponsReply import ResponsReply
from python.Respons_user.ResponsTimeAt import ResponsTimeAt
from python.Api_backend.PostDataTimeAt import PostDataTimeAt
from python.Util import Util

class TimeAt:
    
    def __new__(self,body): 
        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])
       
        respons = PostDataTimeAt(user_uid)
        try:

            name = str(respons["result"]["result_time_at"][0]["fullname"])
            date = str(respons["result"]["result_time_at"][0]["Stamp_Date"])

            in_time = str(respons["result"]["result_time_at"][0]["in_CHK"])
            in_place = str(respons["result"]["result_time_at"][0]["in_location_name"])
            in_type = str(respons["result"]["result_time_at"][0]["in_channel"])

            out_time = str(respons["result"]["result_time_at"][0]["out_CHK"])
            out_place = str(respons["result"]["result_time_at"][0]["out_location_name"])
            out_type = str(respons["result"]["result_time_at"][0]["out_channel"])

            try:
                none = "None"
                txt_none = "ไม่มีข้อมูล"
           
                if in_time == none:
                    in_time = txt_none
                if in_place == none:
                    in_place = txt_none
                if in_type == none:
                    in_type = txt_none
                if out_time == none:
                    out_time = txt_none
                if out_place == none:
                    out_place = txt_none
                if out_type == none:
                    out_type = txt_none
            except:
                print("except")

            text = str("คุณ "+name+"\nวันที่ : "+date+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n\n____________________\nดูรายละเอียดเวลาเข้าออกงาน\n\n"+Util().liff_url_time_att_detail)
            # text = str("คุณ "+name+"\nวันที่ : "+date+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n\n____________________")
            ResponsReply(user,text)
            # ResponsTimeAt(user,text)
        except:
            print("except")
            # ResponsReply(user,"except")
        


     

        

