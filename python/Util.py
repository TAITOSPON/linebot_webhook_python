class Util:
    
    def __new__(self):

        self.index = "THIS LINEBOT WEBHOOK SERVER!"
        self.Maintenance = "Server Maintenance time"
     
        self.Bearer = "Bearer "

        
        self.serverToken = "1L1a7UVuYGa2A84PEq8AYl5tN6AkrgBO8/1eTch7Y7ttQ2EjrIV8aaAnjNN2wnzBhTOAKvNCIBHraMJjpVW4W92y72z1nRS+HNxxfStKTCUU/AVbl2qYlPIwITdcmMgLNIR0RfnzfiNl7wvv14vnLAdB04t89/1O/w1cDnyilFU=" 
        self.liff_url_login ="https://liff.line.me/1655109480-NdbD97GK"
        # self.serverToken = "4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU="
        # self.liff_url_login ="https://liff.line.me/1654967329-yQRPp5rQ"

        self.liff_url_create_leave = "https://liff.line.me/1655109480-VOMzYnqm"
        self.liff_url_time_att_detail = "https://liff.line.me/1655109480-jrRy7m25"
        self.liff_url_profile_detail = "https://liff.line.me/1655109480-wLRoWZpg"
        self.liff_url_profile_detail_leave = "https://liff.line.me/1655109480-lKekYNJK"   
        self.liff_url_logout = "https://liff.line.me/1655109480-GoLo5myJ"


        
        self.line_api_reply = "https://api.line.me/v2/bot/message/reply"
        self.line_api_push = "https://api.line.me/v2/bot/message/push"
   

        # key dialogflow
        self.key_dialogflow = "linebot-toat-kyur"
        self.key_dialogflow_langu = "th"

        self.Default_Fallback_Intent = "Default Fallback Intent"
        self.Default_Welcome_Intent = "Default Welcome Intent"

        # text intent case
        self.intent_login = "เข้าสู่ระบบ"
        self.intent_profile_sys = "ระบบสมาชิก"
        self.intent_leave = "ข้อมูลการขาดลา"
        self.intent_time_work = "ตรวจสอบเวลาเข้างาน"
        self.intent_meet = "จองห้องประชุม"
        self.intent_menu  = "เมนู"
        self.intent_logout = "ออกจากระบบ"
        self.intent_covid ="สถานการณ์โควิด"


        # path backend
        self.api_check_login = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_check_login"
        self.api_log_out = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_logout"
        self.api_get_user_with_uid = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_with_uid"
        self.api_get_data_time_at_with_uid = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_TimeAt/TimeAt_feed"


        self.api_leave_get_year_for_select = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_Leave/Leave_year_select"
        self.api_leave_get_by_year = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_Leave/Leave_year"

    

        #text_leave
        self.Leave_info = "Leave_info"
    
        self.User_logout = "User_logout"
        

        return self


    
# print(Util().Api_login)