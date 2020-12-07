from python.Respons_user.ResponsTimeAt import ResponsTimeAt
from python.Api_backend.PostDataTimeAt import PostDataTimeAt

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
            out_place = str(respons["result"]["result_time_at"][0]["out_location"])
            out_type = str(respons["result"]["result_time_at"][0]["out_channel"])

            text = str("คุณ "+name+"\nวันที่ : "+date+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place)

            ResponsTimeAt(user,text)
        except:
            print("An exception occurred")
        
        # ResponsReply(user,str(PostDataTimeAt(user_uid)))
       

     

        

