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
            
            try:
                date = date.split('-')
                month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[int(date[1])]
                thai_year = int(date[0]) + 543
                day = date[2]
                date = str(day)+" "+str(month_name)+" "+str(thai_year)
            except:
                print("except date")

            try:
                in_time = str(respons["result"]["result_time_at"][0]["in_CHK"])
                in_place = str(respons["result"]["result_time_at"][0]["in_location_name"])
                in_type = str(respons["result"]["result_time_at"][0]["in_channel"])

                index = len(respons["result"]["result_time_at"])-1

                h_f, m_f, s_f = [int(i) for i in str(respons["result"]["result_time_at"][0]["out_CHK"]).split(':')]

                h_l, m_l, s_l = [int(i) for i in str(respons["result"]["result_time_at"][index]["out_CHK"]).split(':')]

                time_f = int(str(h_f)+str(m_f)+str(s_f))
                time_l = int(str(h_l)+str(m_l)+str(s_l))
                
                if time_f > time_l:
                    out_time = str(respons["result"]["result_time_at"][0]["out_CHK"])
                    out_place = str(respons["result"]["result_time_at"][0]["out_location_name"])
                    out_type = str(respons["result"]["result_time_at"][0]["out_channel"])
                else:
                    out_time = str(respons["result"]["result_time_at"][index]["out_CHK"])
                    out_place = str(respons["result"]["result_time_at"][index]["out_location_name"])
                    out_type = str(respons["result"]["result_time_at"][index]["out_channel"])

            except:
                in_time = str(respons["result"]["result_time_at"][0]["in_CHK"])
                in_place = str(respons["result"]["result_time_at"][0]["in_location_name"])
                in_type = str(respons["result"]["result_time_at"][0]["in_channel"])

                out_time = "None"
                out_place = "None"
                out_type = "None"

                

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

            text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_time_att_detail)
            # text = str("คุณ "+name+"\nวันที่ : "+date+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n\n____________________")
            ResponsReply(user,text)
            # ResponsTimeAt(user,text)
        except:
            
            # result_time_at = str(respons["result"]["result_time_at"])

            # if result_time_at == "":

            name = str(respons["result"]["result_user"][0]["user_ad_name"])
            text = str("คุณ "+name+"\n\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_time_att_detail)
            ResponsReply(user,text)




     

        

