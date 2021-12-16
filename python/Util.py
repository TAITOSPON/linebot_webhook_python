class Util:
    
    def __new__(self):

        self.index = "THIS LINEBOT WEBHOOK SERVER!"
        self.Maintenance = "ขออภัยในความไม่สะดวก กำลังแก้ไขระบบ \nSorry! Server maintenance time \udbc0\udc8e \udbc0\udcaa \udbc0\udc3a"
     
        self.Bearer = "Bearer "

        
        self.serverToken = "1L1a7UVuYGa2A84PEq8AYl5tN6AkrgBO8/1eTch7Y7ttQ2EjrIV8aaAnjNN2wnzBhTOAKvNCIBHraMJjpVW4W92y72z1nRS+HNxxfStKTCUU/AVbl2qYlPIwITdcmMgLNIR0RfnzfiNl7wvv14vnLAdB04t89/1O/w1cDnyilFU=" 
        self.destination = "U6adcb805527f4b1077a6e1ce34d5ab2e"
        
        self.serverToken_dev = "4d7QOg7qteXxTxhGEQ5ROBfc2wiBVyRTAnbA73hrZcsWLM7etaAcqpP/IS+Pv5/Psxa2nxyeSrvww7NrsRnl4n4i2Edzk36Dr5wzQZIItg1paczCVHU+/LnIEz27U68OrJSTiDooQf0xHZRx2FTp5gdB04t89/1O/w1cDnyilFU="
        self.destination_dev = "U28e8cf44dbfdfb4cf4c1e027641a5306"
        

        self.liff_url_login ="https://liff.line.me/1655109480-NdbD97GK"
        self.liff_url_create_leave = "https://liff.line.me/1655109480-VOMzYnqm"
        self.liff_url_time_att_detail = "https://liff.line.me/1655109480-jrRy7m25"
        self.liff_url_time_stamp = "https://liff.line.me/1655109480-MXKb06wG"
        self.liff_url_profile_detail = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Profile"
        self.liff_url_profile_detail_leave = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Leave"
        self.liff_url_profile_detail_financial = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Financial"   
        self.liff_url_profile_detail_cooperativesaving = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Cooperativesaving"   
        self.liff_url_profile_detail_searchtelephonenumber = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_SearchTelephoneNumber"  
        self.liff_url_profile_detail_askinout = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Askinout"  
        self.liff_url_profile_detail_taxt = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Tax"  
        self.liff_url_profile_detail_lineoaformsettingtelephonenumber = "line://app/1655109480-j7nN8VqP?liff.state=MemberPage%2FMember_TOAT_Lineoaformsettingtelephonenumber"  
        
        self.liff_url_logout = "https://liff.line.me/1655109480-GoLo5myJ"
        self.liff_url_help_center = "https://liff.line.me/1655109480-jXW76xR8"
        self.liff_url_covid_emp_form = " https://liff.line.me/1655109480-VjdKrvBX"

        self.liff_url_km_and_im = "https://liff.line.me/1655109480-Ka61NvXx"
        
        self.liff_url_work_system_report_sale = "line://app/1655109480-k7MoQ9jP?liff.state=SystemWorkPage%2FSystemWork_Sale_report"

        self.url_profile_detail = "https://memberapp.toat.co.th/memberttm/"
        self.url_timeat = "https://change.toat.co.th/timeatt/"
        self.url_member_tax = "https://memberapp.toat.co.th/memberttm/tax/"
        self.profile_detail_leaveyear = "https://memberapp.toat.co.th/memberttm/leaveyear"
        self.profile_detail_lineoaformsettingtelephonenumber = "https://memberapp.toat.co.th/memberttm/lineoaformsettingtelephonenumber"
        
        
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
        self.edit_tel ="ปรับปรุงเบอร์โทรภายใน"
        self.intent_financial = "สลิปเงินเดือน"
        self.intent_searchtelephonenumber = "ค้นหาเบอร์โทรพนักงาน"
        self.intent_cooperativesaving = "สหกรณ์ฯยาสูบ"
        self.intent_time_work = "ตรวจสอบเวลาเข้างาน"
        self.intent_time_att = "บันทึกเวลา"
        self.intent_meet = "จองห้องประชุม"
        self.intent_menu  = "เมนู"
        self.intent_logout = "ออกจากระบบ"
        self.intent_covid ="สถานการณ์โควิด"
        self.intent_hos_ben = "รพ.สวนเบญฯ"
        self.intent_covid_form ="ประเมินความเสี่ยงโควิด19"
        self.intent_covid_confrim ="ยืนยันพนักงานประเมินความเสี่ยง"
        self.help_center = "ศูนย์ช่วยเหลือ"
        self.help_rules = "กฎระเบียบ ยสท."
        self.work_system = "ระบบงาน ยสท."
        
        self.help_rules_link = "https://datastudio.google.com/u/0/reporting/e8d25a8f-c147-439e-a2cf-2e301cd855ff/page/p_6ohwqwbbnc?s=qJ-q59gnbhU"
        self.facebook_hos_link = "https://www.facebook.com/177054399691705/posts/953322305398240/"
    

        # path backend
        self.api_check_login = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_check_login"
        self.api_log_out = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_logout"
        self.api_get_user_with_uid = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_User/User_with_uid"
        self.api_get_data_time_at_with_uid = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_TimeAt/TimeAt_feed"
        self.api_get_user_datail_with_ad = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_Member/Member_User_Profile_withAD"
        self.api_check_permit_sale_report = "https://change.toat.co.th/api_list/index.php/api/users/chkPermit"


        self.api_leave_get_year_for_select = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_Leave/Leave_year_select"
        self.api_leave_get_by_year = "https://webhook.toat.co.th/linebot/web/index.php/api/Api_Leave/Leave_year"

    

        #text_leave
        self.Leave_info = "Leave_info"
    
        self.User_logout = "User_logout"
        

        return self


    
# print(Util().Api_login)