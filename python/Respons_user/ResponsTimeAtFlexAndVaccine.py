
import requests
import json

from python.Api_backend.PostDataTimeAt import PostDataTimeAt
from python.Api_backend.GetDataUserVaccine import GetDataUserVaccine

from python.Api_backend.PostLeaveYearSelect import PostLeaveYearSelect
from python.Api_backend.PostLeaveyear import PostLeaveyear


# from python.Respons_user.ResponsLeave import ResponsLeave

from python.Util import Util

class ResponsTimeAtFlexAndVaccine:
    
    def __init__(self,devicetoken,body):
       

        user_uid = str(body["events"][0]['source']['userId'])
        user = str(body["events"][0]['replyToken'])
       
        respons = PostDataTimeAt(user_uid)

        LeaveYearSelect = PostLeaveYearSelect(user_uid)
        Leaveyear = PostLeaveyear(user_uid,LeaveYearSelect[0]["Value"])

        

        try:

            
            name = str(respons["result"]["result_time_at"][0]["fullname"])
            date = str(respons["result"]["result_time_at"][0]["Stamp_Date"])
            user_ad_code = str(respons["result"]["result_user"][0]["user_ad_code"])
            
            try:
                date = date.split('-')
                month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[int(date[1])]
                thai_year = int(date[0]) + 543
                day = date[2]
                date = str(day)+" "+str(month_name)+" "+str(thai_year)
            except:
                print("except date")

            try:
                try:
                    index = len(respons["result"]["result_time_at"])-1

                    if str(respons["result"]["result_time_at"][0]["in_CHK"]) < str(respons["result"]["result_time_at"][index]["in_CHK"]):
                        in_time = str(respons["result"]["result_time_at"][0]["in_CHK"])
                        in_place = str(respons["result"]["result_time_at"][0]["in_location_name"])
                        in_type = str(respons["result"]["result_time_at"][0]["in_channel"])
                    else:
                        in_time = str(respons["result"]["result_time_at"][index]["in_CHK"])
                        in_place = str(respons["result"]["result_time_at"][index]["in_location_name"])
                        in_type = str(respons["result"]["result_time_at"][index]["in_channel"])

                except:

                    in_time = str(respons["result"]["result_time_at"][0]["in_CHK"])
                    in_place = str(respons["result"]["result_time_at"][0]["in_location_name"])
                    in_type = str(respons["result"]["result_time_at"][0]["in_channel"])


                o_index = len(respons["result"]["result_time_at"])-1


                if str(respons["result"]["result_time_at"][0]["out_CHK"]) > str(respons["result"]["result_time_at"][o_index]["out_CHK"]):

                    out_time = str(respons["result"]["result_time_at"][0]["out_CHK"])
                    out_place = str(respons["result"]["result_time_at"][0]["out_location_name"])
                    out_type = str(respons["result"]["result_time_at"][0]["out_channel"])

                else:

                    out_time = str(respons["result"]["result_time_at"][o_index]["out_CHK"])
                    out_place = str(respons["result"]["result_time_at"][o_index]["out_location_name"])
                    out_type = str(respons["result"]["result_time_at"][o_index]["out_channel"])



            except:
                
                try:
                    index = len(respons["result"]["result_time_at"])-1
                    
                    if str(respons["result"]["result_time_at"][0]["in_CHK"]) < str(respons["result"]["result_time_at"][index]["in_CHK"]):
                        in_time = str(respons["result"]["result_time_at"][0]["in_CHK"])
                        in_place = str(respons["result"]["result_time_at"][0]["in_location_name"])
                        in_type = str(respons["result"]["result_time_at"][0]["in_channel"])
                    else:
                        in_time = str(respons["result"]["result_time_at"][index]["in_CHK"])
                        in_place = str(respons["result"]["result_time_at"][index]["in_location_name"])
                        in_type = str(respons["result"]["result_time_at"][index]["in_channel"])

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

            try:
                if user_ad_code == "003599":

                    data_vaccine = GetDataUserVaccine("003599")
          
                else:
                    data_vaccine = GetDataUserVaccine(user_ad_code)
      
               

                if  data_vaccine != "null": 
                    if data_vaccine["Appointment"] != "":   #มีนัด

                        if data_vaccine["VaccineDate2"] == "":  #นัดเข็ม 2
                            text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
                            
                            body = {    
                                "replyToken": str(devicetoken),
                                "messages": [
                                    {
                                        "type":"flex",
                                        "altText":Util().intent_time_work,
                                        "contents":{
                                            "type":"carousel",
                                            "contents":[
                                                
                                                {
                                                    "type": "bubble",
                                                    # "size": "giga",
                                                    "direction": "ltr",
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                
                                                                    {
                                                                        "type": "text",
                                                                        "text": name,
                                                                        "weight": "bold",
                                                                        "size": "lg",
                                                                        "margin": "none",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "วันที่ : "+str(date),
                                                                        "size": "sm",
                                                                        "color": "#D39D2B",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "vertical",
                                                                        "spacing": "sm",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "เวลาเข้างาน :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_time,
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "ด้วย  :",
                                                                        
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_type,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "สถานที่  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_place,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "wrap": True,
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "spacing": "sm",
                                                                        "layout": "vertical",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "เวลาออกงาน  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_time,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "ด้วย  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_type,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "สถานที่  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_place,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "wrap": True,
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "รายละเอียด",
                                                                    "uri": Util().liff_url_profile_detail_askinout,
                                                                    "altUri": {
                                                                        "desktop" : Util().url_timeat
                                                                    }
                                                                },
                                                                
                                                                "color": "#D39D2B",
                                                                "style": "primary"
                                                            }
                                                        ]
                                                    }
                                                } , 

                                                {
                                                    "type": "bubble",
                                                    "direction": "ltr",
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                
                                                                    {
                                                                        "type": "text",
                                                                        "text": Util().intent_leave,
                                                                        "weight": "bold",
                                                                        "size": "lg",
                                                                        "margin": "none",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "ปีงบประมาณ : "+str(LeaveYearSelect[0]["Value"]),
                                                                        "size": "sm",
                                                                        "color": "#D39D2B",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "vertical",
                                                                        "spacing": "sm",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว : "+str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },

                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  : "+str(Leaveyear['result']['leave_head']['TotalLeave']),
                                                                        
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },

                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนคงเหลือ  : "+str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "รายละเอียด",
                                                                    "uri": Util().liff_url_profile_detail_leave,
                                                                    "altUri": {
                                                                        "desktop" : Util().profile_detail_leaveyear
                                                                    }
                                                                },
                                                                
                                                                "color": "#D39D2B",
                                                                "style": "primary"
                                                            }
                                                        ]
                                                    }
                                                } , 

                                                {
                                                    "type":"bubble",
                                                    "hero":{
                                                        "type":"image",
                                                        "url":"https://scontent.fbkk7-2.fna.fbcdn.net/v/t1.6435-9/167258776_837023323694806_5324680110308309427_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=973b4a&_nc_ohc=avJfTmaIGwAAX9RCiJ-&_nc_ht=scontent.fbkk7-2.fna&oh=92cc72e1eda55b114032f55e3df6918f&oe=614C8A7E",
                                                        "size":"full",
                                                        "aspectRatio":"10:3",
                                                        "aspectMode":"fit"
                                                    },
                                                    "body":{
                                                        "type":"box",
                                                        "layout":"vertical",
                                                        "backgroundColor":"#d9ebce",
                                                        "contents":[
                                                            {
                                                                "type":"text",
                                                                "text":"นัดฉีดวัคซีน (เข็มที่ 2)",
                                                                "weight":"bold",
                                                                "color":"#1DB446",
                                                                "size":"xl"
                                                            },
                                                            {
                                                                "type":"text",
                                                                "text":"วันที่ : "+str(data_vaccine["Appointment"]),
                                                                "weight":"bold",
                                                                "size":"md",
                                                                "margin":"md"
                                                            },
                                                            {
                                                                "type":"text",
                                                                "text":str(data_vaccine["Name"]),
                                                                "size":"md",
                                                                "color":"#000000",
                                                                "margin":"sm",
                                                                "wrap":True
                                                            },

                                                            {
                                                                "type":"separator",
                                                                "color":"#ffffff",
                                                                "margin":"md"
                                                            },
                                                            {
                                                                "type":"box",
                                                                "layout":"vertical",
                                                                "margin":"sm",
                                                                "spacing":"sm",
                                                                "contents":[

                                                                    
                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 1) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["VaccineDate1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineName1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":str(data_vaccine["VaccineLot1"]),
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },
                                                                    
                                                                    
                                                
                                                                    {
                                                                        "type":"separator",
                                                                        "color":"#ffffff",
                                                                        "margin":"md"
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 2) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["Appointment"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":"-",
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":"-",
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },
                                                                
                                                                ]
                                                            },
                                                            {
                                                                "type":"separator",
                                                                "color":"#ffffff",
                                                                "margin":"md"
                                                            },
                                                        
                                                        ]
                                                    },
                                                    "styles":{
                                                        "footer":{
                                                            "separator":True
                                                        }
                                                    }
                                                },


                                            ]
                                        }
                                    }
                                ]
                        
                            }

                        else :   #นัดเข็ม 3
                            text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
                            
                            body = {    
                                "replyToken": str(devicetoken),
                                "messages": [
                                    {
                                        "type":"flex",
                                        "altText":Util().intent_time_work,
                                        "contents":{
                                            "type":"carousel",
                                            "contents":[
                                                
                                                {
                                                    "type": "bubble",
                                                    # "size": "giga",
                                                    "direction": "ltr",
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                
                                                                    {
                                                                        "type": "text",
                                                                        "text": name,
                                                                        "weight": "bold",
                                                                        "size": "lg",
                                                                        "margin": "none",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "วันที่ : "+str(date),
                                                                        "size": "sm",
                                                                        "color": "#D39D2B",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "vertical",
                                                                        "spacing": "sm",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "เวลาเข้างาน :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_time,
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "ด้วย  :",
                                                                        
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_type,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "สถานที่  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_place,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "wrap": True,
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "spacing": "sm",
                                                                        "layout": "vertical",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "เวลาออกงาน  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_time,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "ด้วย  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_type,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "สถานที่  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_place,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "wrap": True,
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "รายละเอียด",
                                                                    "uri": Util().liff_url_profile_detail_askinout,
                                                                    "altUri": {
                                                                        "desktop" : Util().url_timeat
                                                                    }
                                                                },
                                                                
                                                                "color": "#D39D2B",
                                                                "style": "primary"
                                                            }
                                                        ]
                                                    }
                                                } , 

                                                {
                                                    "type": "bubble",
                                                    "direction": "ltr",
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                
                                                                    {
                                                                        "type": "text",
                                                                        "text": Util().intent_leave,
                                                                        "weight": "bold",
                                                                        "size": "lg",
                                                                        "margin": "none",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "ปีงบประมาณ : "+str(LeaveYearSelect[0]["Value"]),
                                                                        "size": "sm",
                                                                        "color": "#D39D2B",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "vertical",
                                                                        "spacing": "sm",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว : "+str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },

                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  : "+str(Leaveyear['result']['leave_head']['TotalLeave']),
                                                                        
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },

                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนคงเหลือ  : "+str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "รายละเอียด",
                                                                    "uri": Util().liff_url_profile_detail_leave,
                                                                    "altUri": {
                                                                        "desktop" : Util().profile_detail_leaveyear
                                                                    }
                                                                },
                                                                
                                                                "color": "#D39D2B",
                                                                "style": "primary"
                                                            }
                                                        ]
                                                    }
                                                } , 
 

                                                {
                                                    "type":"bubble",
                                                    "hero":{
                                                        "type":"image",
                                                        "url":"https://scontent.fbkk7-2.fna.fbcdn.net/v/t1.6435-9/167258776_837023323694806_5324680110308309427_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=973b4a&_nc_ohc=avJfTmaIGwAAX9RCiJ-&_nc_ht=scontent.fbkk7-2.fna&oh=92cc72e1eda55b114032f55e3df6918f&oe=614C8A7E",
                                                        "size":"full",
                                                        "aspectRatio":"10:3",
                                                        "aspectMode":"fit"
                                                    },
                                                    "body":{
                                                        "type":"box",
                                                        "layout":"vertical",
                                                        "backgroundColor":"#d9ebce",
                                                        "contents":[
                                                            {
                                                                "type":"text",
                                                                "text":"นัดฉีดวัคซีน (เข็มที่ 3)",
                                                                "weight":"bold",
                                                                "color":"#1DB446",
                                                                "size":"xl"
                                                            },
                                                            {
                                                                "type":"text",
                                                                "text":"วันที่ : "+str(data_vaccine["Appointment"]),
                                                                "weight":"bold",
                                                                "size":"md",
                                                                "margin":"md"
                                                            },
                                                            {
                                                                "type":"text",
                                                                "text":str(data_vaccine["Name"]),
                                                                "size":"md",
                                                                "color":"#000000",
                                                                "margin":"sm",
                                                                "wrap":True
                                                            },

                                                            {
                                                                "type":"separator",
                                                                "color":"#ffffff",
                                                                "margin":"md"
                                                            },
                                                            {
                                                                "type":"box",
                                                                "layout":"vertical",
                                                                "margin":"sm",
                                                                "spacing":"sm",
                                                                "contents":[

                                                                    
                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 1) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["VaccineDate1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineName1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":str(data_vaccine["VaccineLot1"]),
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },
                                                                    
                                                                    
                                                
                                                                    {
                                                                        "type":"separator",
                                                                        "color":"#ffffff",
                                                                        "margin":"md"
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 2) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["VaccineDate2"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineName2"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":str(data_vaccine["VaccineLot2"]),
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },


                                                                     {
                                                                        "type":"separator",
                                                                        "color":"#ffffff",
                                                                        "margin":"md"
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 3) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["Appointment"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":"-",
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":"-",
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },
                                                                
                                                                ]
                                                            },
                                                            {
                                                                "type":"separator",
                                                                "color":"#ffffff",
                                                                "margin":"md"
                                                            },
                                                        
                                                        ]
                                                    },
                                                    "styles":{
                                                        "footer":{
                                                            "separator":True
                                                        }
                                                    }
                                                },

                                            ]
                                        }
                                    }
                                ]
                        
                            }

                    else : #ไม่มีนัด
                        
                        if data_vaccine["VaccineDate3"] != "": #ครบ 3 เข็ม
                            text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
                            
                            body = {    
                                "replyToken": str(devicetoken),
                                "messages": [
                                    {
                                        "type":"flex",
                                        "altText":Util().intent_time_work,
                                        "contents":{
                                            "type":"carousel",
                                            "contents":[
                                                
                                                {
                                                    "type": "bubble",
                                                    # "size": "giga",
                                                    "direction": "ltr",
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                
                                                                    {
                                                                        "type": "text",
                                                                        "text": name,
                                                                        "weight": "bold",
                                                                        "size": "lg",
                                                                        "margin": "none",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "วันที่ : "+str(date),
                                                                        "size": "sm",
                                                                        "color": "#D39D2B",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "vertical",
                                                                        "spacing": "sm",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "เวลาเข้างาน :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_time,
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "ด้วย  :",
                                                                        
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_type,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "สถานที่  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": in_place,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "wrap": True,
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "spacing": "sm",
                                                                        "layout": "vertical",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "เวลาออกงาน  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_time,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "ด้วย  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_type,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "สถานที่  :",
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            {
                                                                                "type": "text",
                                                                                "text": out_place,
                                                                                "size": "sm",
                                                                                "align": "start",
                                                                                "wrap": True,
                                                                                "contents": []
                                                                            }
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "รายละเอียด",
                                                                    "uri": Util().liff_url_profile_detail_askinout,
                                                                    "altUri": {
                                                                        "desktop" : Util().url_timeat
                                                                    }
                                                                },
                                                                
                                                                "color": "#D39D2B",
                                                                "style": "primary"
                                                            }
                                                        ]
                                                    }
                                                } , 

                                                {
                                                    "type": "bubble",
                                                    "direction": "ltr",
                                                    "body": {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [
                                                            {
                                                                "type": "box",
                                                                "layout": "vertical",
                                                                "contents": [
                                                
                                                                    {
                                                                        "type": "text",
                                                                        "text": Util().intent_leave,
                                                                        "weight": "bold",
                                                                        "size": "lg",
                                                                        "margin": "none",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "text",
                                                                        "text": "ปีงบประมาณ : "+str(LeaveYearSelect[0]["Value"]),
                                                                        "size": "sm",
                                                                        "color": "#D39D2B",
                                                                        "contents": []
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    {
                                                                        "type": "box",
                                                                        "layout": "vertical",
                                                                        "spacing": "sm",
                                                                        "margin": "xs",
                                                                        "contents": [
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "margin": "md",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว : "+str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },

                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  : "+str(Leaveyear['result']['leave_head']['TotalLeave']),
                                                                        
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },

                                                                        {
                                                                            "type": "box",
                                                                            "layout": "horizontal",
                                                                            "contents": [
                                                                            {
                                                                                "type": "text",
                                                                                "text": "วันลาพักผ่อนคงเหลือ  : "+str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                                                                "size": "sm",
                                                                                "contents": []
                                                                            },
                                                                            
                                                                            ]
                                                                        }
                                                                        ]
                                                                    },
                                                                    {
                                                                        "type": "separator",
                                                                        "margin": "md"
                                                                    },
                                                                    
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    "footer": {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                            {
                                                                "type": "button",
                                                                "action": {
                                                                    "type": "uri",
                                                                    "label": "รายละเอียด",
                                                                    "uri": Util().liff_url_profile_detail_leave,
                                                                    "altUri": {
                                                                        "desktop" : Util().profile_detail_leaveyear
                                                                    }
                                                                },
                                                                
                                                                "color": "#D39D2B",
                                                                "style": "primary"
                                                            }
                                                        ]
                                                    }
                                                } , 


                                                {
                                                    "type":"bubble",
                                                    "hero":{
                                                        "type":"image",
                                                        "url":"https://scontent.fbkk7-2.fna.fbcdn.net/v/t1.6435-9/167258776_837023323694806_5324680110308309427_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=973b4a&_nc_ohc=avJfTmaIGwAAX9RCiJ-&_nc_ht=scontent.fbkk7-2.fna&oh=92cc72e1eda55b114032f55e3df6918f&oe=614C8A7E",
                                                        "size":"full",
                                                        "aspectRatio":"10:3",
                                                        "aspectMode":"fit"
                                                    },
                                                    "body":{
                                                        "type":"box",
                                                        "layout":"vertical",
                                                        "backgroundColor":"#d9ebce",
                                                        "contents":[
                                                            
                                                            {
                                                                "type":"text",
                                                                "text":str(data_vaccine["Name"]),
                                                                "size":"md",
                                                                "color":"#000000",
                                                                "margin":"sm",
                                                                "wrap":True
                                                            },

                                                            {
                                                                "type":"separator",
                                                                "color":"#ffffff",
                                                                "margin":"md"
                                                            },
                                                            {
                                                                "type":"box",
                                                                "layout":"vertical",
                                                                "margin":"sm",
                                                                "spacing":"sm",
                                                                "contents":[

                                                                    
                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 1) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["VaccineDate1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineName1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":str(data_vaccine["VaccineLot1"]),
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },
                                                                    
                                                                    
                                                
                                                                    {
                                                                        "type":"separator",
                                                                        "color":"#ffffff",
                                                                        "margin":"md"
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 2) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["VaccineDate2"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineName2"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":str(data_vaccine["VaccineLot2"]),
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },

                                                                     {
                                                                        "type":"separator",
                                                                        "color":"#ffffff",
                                                                        "margin":"md"
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                        
                                                                            {
                                                                                "type":"text",
                                                                                "text":"วันที่รับวัคซีน (เข็มที่ 3) :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text": str(data_vaccine["VaccineDate3"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                                "type":"text",
                                                                                "text":"ชื่อวัคซีน :",
                                                                                "size":"sm",
                                                                                "color":"#555555",
                                                                                "flex":0
                                                                            },
                                                                            {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineName3"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end"
                                                                            },
                                                                            
                                                                            
                                                                        ]
                                                                    },

                                                                    {
                                                                        "type":"box",
                                                                        "layout":"horizontal",
                                                                        "contents":[
                                                                            {
                                                                            "type":"text",
                                                                            "text":"รุ่นการผลิต :",
                                                                            "size":"sm",
                                                                            "color":"#555555"
                                                                            },
                                                                            {
                                                                            "type":"text",
                                                                            "text":str(data_vaccine["VaccineLot3"]),
                                                                            "size":"sm",
                                                                            "color":"#111111",
                                                                            "align":"end",
                                                                            "wrap": True,
                                                                            }
                                                                        ]
                                                                    },
                                                                
                                                                ]
                                                            },
                                                            {
                                                                "type":"separator",
                                                                "color":"#ffffff",
                                                                "margin":"md"
                                                            },
                                                        
                                                        ]
                                                    },
                                                    "styles":{
                                                        "footer":{
                                                            "separator":True
                                                        }
                                                    }
                                                },

                                            ]
                                        }
                                    }
                                ]
                        
                            }
                              
                        else :  #ครบ 2 เข็ม
                            if data_vaccine["VaccineDate2"] == "": #ครบ 2 เข็ม (no data)
                                text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
                                
                                body = {    
                                    "replyToken": str(devicetoken),
                                    "messages": [
                                        {
                                            "type":"flex",
                                            "altText":Util().intent_time_work,
                                            "contents":{
                                                "type":"carousel",
                                                "contents":[
                                                    
                                                    {
                                                        "type": "bubble",
                                                        # "size": "giga",
                                                        "direction": "ltr",
                                                        "body": {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "vertical",
                                                                    "contents": [
                                                    
                                                                        {
                                                                            "type": "text",
                                                                            "text": name,
                                                                            "weight": "bold",
                                                                            "size": "lg",
                                                                            "margin": "none",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "วันที่ : "+str(date),
                                                                            "size": "sm",
                                                                            "color": "#D39D2B",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "spacing": "sm",
                                                                            "margin": "xs",
                                                                            "contents": [
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "margin": "md",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "เวลาเข้างาน :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": in_time,
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "ด้วย  :",
                                                                            
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": in_type,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "สถานที่  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": in_place,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "wrap": True,
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "spacing": "sm",
                                                                            "layout": "vertical",
                                                                            "margin": "xs",
                                                                            "contents": [
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "margin": "md",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "เวลาออกงาน  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": out_time,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "ด้วย  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": out_type,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "สถานที่  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": out_place,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "wrap": True,
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        "footer": {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                                {
                                                                    "type": "button",
                                                                    "action": {
                                                                        "type": "uri",
                                                                        "label": "รายละเอียด",
                                                                        "uri": Util().liff_url_profile_detail_askinout,
                                                                        "altUri": {
                                                                            "desktop" : Util().url_timeat
                                                                        }
                                                                    },
                                                                    
                                                                    "color": "#D39D2B",
                                                                    "style": "primary"
                                                                }
                                                            ]
                                                        }
                                                    } , 

                                                    {
                                                        "type": "bubble",
                                                        "direction": "ltr",
                                                        "body": {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "vertical",
                                                                    "contents": [
                                                    
                                                                        {
                                                                            "type": "text",
                                                                            "text": Util().intent_leave,
                                                                            "weight": "bold",
                                                                            "size": "lg",
                                                                            "margin": "none",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "ปีงบประมาณ : "+str(LeaveYearSelect[0]["Value"]),
                                                                            "size": "sm",
                                                                            "color": "#D39D2B",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "spacing": "sm",
                                                                            "margin": "xs",
                                                                            "contents": [
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "vertical",
                                                                                "margin": "md",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว : "+str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                
                                                                                ]
                                                                            },

                                                                            {
                                                                                "type": "separator",
                                                                                "margin": "md"
                                                                            },

                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  : "+str(Leaveyear['result']['leave_head']['TotalLeave']),
                                                                            
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                
                                                                                ]
                                                                            },

                                                                            {
                                                                                "type": "separator",
                                                                                "margin": "md"
                                                                            },

                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "วันลาพักผ่อนคงเหลือ  : "+str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                
                                                                                ]
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        "footer": {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                                {
                                                                    "type": "button",
                                                                    "action": {
                                                                        "type": "uri",
                                                                        "label": "รายละเอียด",
                                                                        "uri": Util().liff_url_profile_detail_leave,
                                                                        "altUri": {
                                                                            "desktop" : Util().profile_detail_leaveyear
                                                                        }
                                                                    },
                                                                    
                                                                    "color": "#D39D2B",
                                                                    "style": "primary"
                                                                }
                                                            ]
                                                        }
                                                    } , 


                                                    {
                                                        "type":"bubble",
                                                        "hero":{
                                                            "type":"image",
                                                            "url":"https://scontent.fbkk7-2.fna.fbcdn.net/v/t1.6435-9/167258776_837023323694806_5324680110308309427_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=973b4a&_nc_ohc=avJfTmaIGwAAX9RCiJ-&_nc_ht=scontent.fbkk7-2.fna&oh=92cc72e1eda55b114032f55e3df6918f&oe=614C8A7E",
                                                            "size":"full",
                                                            "aspectRatio":"10:3",
                                                            "aspectMode":"fit"
                                                        },
                                                        "body":{
                                                            "type":"box",
                                                            "layout":"vertical",
                                                            "backgroundColor":"#d9ebce",
                                                            "contents":[
                                                                
                                                                {
                                                                    "type":"text",
                                                                    "text":str(data_vaccine["Name"]),
                                                                    "size":"md",
                                                                    "color":"#000000",
                                                                    "margin":"sm",
                                                                    "wrap":True
                                                                },

                                                                {
                                                                    "type":"separator",
                                                                    "color":"#ffffff",
                                                                    "margin":"md"
                                                                },
                                                                {
                                                                    "type":"box",
                                                                    "layout":"vertical",
                                                                    "margin":"sm",
                                                                    "spacing":"sm",
                                                                    "contents":[

                                                                        
                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                            
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"วันที่รับวัคซีน (เข็มที่ 1) :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text": str(data_vaccine["VaccineDate1"]),
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end",
                                                                                    "wrap": True,
                                                                                },
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"ชื่อวัคซีน :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":str(data_vaccine["VaccineName1"]),
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end",
                                                                                    "wrap": True,
                                                                                },
                                                                                
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                "type":"text",
                                                                                "text":"รุ่นการผลิต :",
                                                                                "size":"sm",
                                                                                "color":"#555555"
                                                                                },
                                                                                {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineLot1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                                }
                                                                            ]
                                                                        },
                                                                        
                                                                        
                                                    
                                                                        {
                                                                            "type":"separator",
                                                                            "color":"#ffffff",
                                                                            "margin":"md"
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                            
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"วันที่รับวัคซีน (เข็มที่ 2) :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text": "-",
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end"
                                                                                },
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"ชื่อวัคซีน :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"-",
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end"
                                                                                },
                                                                                
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                "type":"text",
                                                                                "text":"รุ่นการผลิต :",
                                                                                "size":"sm",
                                                                                "color":"#555555"
                                                                                },
                                                                                {
                                                                                "type":"text",
                                                                                "text":"-",
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                                }
                                                                            ]
                                                                        },
                                                                    
                                                                    ]
                                                                },
                                                                {
                                                                    "type":"separator",
                                                                    "color":"#ffffff",
                                                                    "margin":"md"
                                                                },
                                                            
                                                            ]
                                                        },
                                                        "styles":{
                                                            "footer":{
                                                                "separator":True
                                                            }
                                                        }
                                                    },

                                                ]
                                            }
                                        }
                                    ]
                            
                                }
                            else :
                                text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
                                
                                body = {    
                                    "replyToken": str(devicetoken),
                                    "messages": [
                                        {
                                            "type":"flex",
                                            "altText":Util().intent_time_work,
                                            "contents":{
                                                "type":"carousel",
                                                "contents":[
                                                    
                                                    {
                                                        "type": "bubble",
                                                        # "size": "giga",
                                                        "direction": "ltr",
                                                        "body": {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "vertical",
                                                                    "contents": [
                                                    
                                                                        {
                                                                            "type": "text",
                                                                            "text": name,
                                                                            "weight": "bold",
                                                                            "size": "lg",
                                                                            "margin": "none",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "วันที่ : "+str(date),
                                                                            "size": "sm",
                                                                            "color": "#D39D2B",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "spacing": "sm",
                                                                            "margin": "xs",
                                                                            "contents": [
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "margin": "md",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "เวลาเข้างาน :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": in_time,
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "ด้วย  :",
                                                                            
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": in_type,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "สถานที่  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": in_place,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "wrap": True,
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "spacing": "sm",
                                                                            "layout": "vertical",
                                                                            "margin": "xs",
                                                                            "contents": [
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "margin": "md",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "เวลาออกงาน  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": out_time,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "ด้วย  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": out_type,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            },
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "สถานที่  :",
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": out_place,
                                                                                    "size": "sm",
                                                                                    "align": "start",
                                                                                    "wrap": True,
                                                                                    "contents": []
                                                                                }
                                                                                ]
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        "footer": {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                                {
                                                                    "type": "button",
                                                                    "action": {
                                                                        "type": "uri",
                                                                        "label": "รายละเอียด",
                                                                        "uri": Util().liff_url_profile_detail_askinout,
                                                                        "altUri": {
                                                                            "desktop" : Util().url_timeat
                                                                        }
                                                                    },
                                                                    
                                                                    "color": "#D39D2B",
                                                                    "style": "primary"
                                                                }
                                                            ]
                                                        }
                                                    } , 

                                                    {
                                                        "type": "bubble",
                                                        "direction": "ltr",
                                                        "body": {
                                                            "type": "box",
                                                            "layout": "vertical",
                                                            "contents": [
                                                                {
                                                                    "type": "box",
                                                                    "layout": "vertical",
                                                                    "contents": [
                                                    
                                                                        {
                                                                            "type": "text",
                                                                            "text": Util().intent_leave,
                                                                            "weight": "bold",
                                                                            "size": "lg",
                                                                            "margin": "none",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "text",
                                                                            "text": "ปีงบประมาณ : "+str(LeaveYearSelect[0]["Value"]),
                                                                            "size": "sm",
                                                                            "color": "#D39D2B",
                                                                            "contents": []
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        {
                                                                            "type": "box",
                                                                            "layout": "vertical",
                                                                            "spacing": "sm",
                                                                            "margin": "xs",
                                                                            "contents": [
                                                                            {
                                                                                "type": "box",
                                                                                "layout": "vertical",
                                                                                "margin": "md",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "วันลาพักผ่อนรวมที่โอนมาจากปีที่แล้ว : "+str(Leaveyear['result']['leave_head']['TotalLeaveAvailable']),
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                
                                                                                ]
                                                                            },

                                                                            {
                                                                                "type": "separator",
                                                                                "margin": "md"
                                                                            },

                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "วันลาพักผ่อนที่ใช้ไปแล้ว  : "+str(Leaveyear['result']['leave_head']['TotalLeave']),
                                                                            
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                
                                                                                ]
                                                                            },

                                                                            {
                                                                                "type": "separator",
                                                                                "margin": "md"
                                                                            },

                                                                            {
                                                                                "type": "box",
                                                                                "layout": "horizontal",
                                                                                "contents": [
                                                                                {
                                                                                    "type": "text",
                                                                                    "text": "วันลาพักผ่อนคงเหลือ  : "+str(Leaveyear['result']['leave_head']['SumLeaveYear']),
                                                                                    "size": "sm",
                                                                                    "contents": []
                                                                                },
                                                                                
                                                                                ]
                                                                            }
                                                                            ]
                                                                        },
                                                                        {
                                                                            "type": "separator",
                                                                            "margin": "md"
                                                                        },
                                                                        
                                                                    ]
                                                                }
                                                            ]
                                                        },
                                                        "footer": {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                                {
                                                                    "type": "button",
                                                                    "action": {
                                                                        "type": "uri",
                                                                        "label": "รายละเอียด",
                                                                        "uri": Util().liff_url_profile_detail_leave,
                                                                        "altUri": {
                                                                            "desktop" : Util().profile_detail_leaveyear
                                                                        }
                                                                    },
                                                                    
                                                                    "color": "#D39D2B",
                                                                    "style": "primary"
                                                                }
                                                            ]
                                                        }
                                                    } , 

                                                  

                                                    {
                                                        "type":"bubble",
                                                        "hero":{
                                                            "type":"image",
                                                            "url":"https://scontent.fbkk7-2.fna.fbcdn.net/v/t1.6435-9/167258776_837023323694806_5324680110308309427_n.jpg?_nc_cat=110&ccb=1-5&_nc_sid=973b4a&_nc_ohc=avJfTmaIGwAAX9RCiJ-&_nc_ht=scontent.fbkk7-2.fna&oh=92cc72e1eda55b114032f55e3df6918f&oe=614C8A7E",
                                                            "size":"full",
                                                            "aspectRatio":"10:3",
                                                            "aspectMode":"fit"
                                                        },
                                                        "body":{
                                                            "type":"box",
                                                            "layout":"vertical",
                                                            "backgroundColor":"#d9ebce",
                                                            "contents":[
                                                                
                                                                {
                                                                    "type":"text",
                                                                    "text":str(data_vaccine["Name"]),
                                                                    "size":"md",
                                                                    "color":"#000000",
                                                                    "margin":"sm",
                                                                    "wrap":True
                                                                },

                                                                {
                                                                    "type":"separator",
                                                                    "color":"#ffffff",
                                                                    "margin":"md"
                                                                },
                                                                {
                                                                    "type":"box",
                                                                    "layout":"vertical",
                                                                    "margin":"sm",
                                                                    "spacing":"sm",
                                                                    "contents":[

                                                                        
                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                            
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"วันที่รับวัคซีน (เข็มที่ 1) :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text": str(data_vaccine["VaccineDate1"]),
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end",
                                                                                    "wrap": True,
                                                                                },
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"ชื่อวัคซีน :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":str(data_vaccine["VaccineName1"]),
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end",
                                                                                    "wrap": True,
                                                                                },
                                                                                
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                "type":"text",
                                                                                "text":"รุ่นการผลิต :",
                                                                                "size":"sm",
                                                                                "color":"#555555"
                                                                                },
                                                                                {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineLot1"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                                }
                                                                            ]
                                                                        },
                                                                        
                                                                        
                                                    
                                                                        {
                                                                            "type":"separator",
                                                                            "color":"#ffffff",
                                                                            "margin":"md"
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                            
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"วันที่รับวัคซีน (เข็มที่ 2) :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text": str(data_vaccine["VaccineDate2"]),
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end"
                                                                                },
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":"ชื่อวัคซีน :",
                                                                                    "size":"sm",
                                                                                    "color":"#555555",
                                                                                    "flex":0
                                                                                },
                                                                                {
                                                                                    "type":"text",
                                                                                    "text":str(data_vaccine["VaccineName2"]),
                                                                                    "size":"sm",
                                                                                    "color":"#111111",
                                                                                    "align":"end"
                                                                                },
                                                                                
                                                                                
                                                                            ]
                                                                        },

                                                                        {
                                                                            "type":"box",
                                                                            "layout":"horizontal",
                                                                            "contents":[
                                                                                {
                                                                                "type":"text",
                                                                                "text":"รุ่นการผลิต :",
                                                                                "size":"sm",
                                                                                "color":"#555555"
                                                                                },
                                                                                {
                                                                                "type":"text",
                                                                                "text":str(data_vaccine["VaccineLot2"]),
                                                                                "size":"sm",
                                                                                "color":"#111111",
                                                                                "align":"end",
                                                                                "wrap": True,
                                                                                }
                                                                            ]
                                                                        },
                                                                    
                                                                    ]
                                                                },
                                                                {
                                                                    "type":"separator",
                                                                    "color":"#ffffff",
                                                                    "margin":"md"
                                                                },
                                                            
                                                            ]
                                                        },
                                                        "styles":{
                                                            "footer":{
                                                                "separator":True
                                                            }
                                                        }
                                                    },

                                                ]
                                            }
                                        }
                                    ]
                            
                                }
                else:
                    text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
                
                    body = {    
                        "replyToken": str(devicetoken),
                        "messages": [
                            {
                                "type": "flex",
                                "altText": Util().intent_time_work,
                                "contents": 


                                {
                                    "type": "bubble",
                                    # "size": "giga",
                                    "direction": "ltr",
                                    "body": {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                
                                                    {
                                                        "type": "text",
                                                        "text": name,
                                                        "weight": "bold",
                                                        "size": "lg",
                                                        "margin": "none",
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": "วันที่ : "+str(date),
                                                        "size": "sm",
                                                        "color": "#D39D2B",
                                                        "contents": []
                                                    },
                                                    {
                                                        "type": "separator",
                                                        "margin": "md"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "spacing": "sm",
                                                        "margin": "xs",
                                                        "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "margin": "md",
                                                            "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "เวลาเข้างาน :",
                                                                "size": "sm",
                                                                "contents": []
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": in_time,
                                                                "size": "sm",
                                                                "contents": []
                                                            }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "ด้วย  :",
                                                        
                                                                "size": "sm",
                                                                "contents": []
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": in_type,
                                                                "size": "sm",
                                                                "align": "start",
                                                                "contents": []
                                                            }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "สถานที่  :",
                                                                "size": "sm",
                                                                "contents": []
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": in_place,
                                                                "size": "sm",
                                                                "align": "start",
                                                                "wrap": True,
                                                                "contents": []
                                                            }
                                                            ]
                                                        }
                                                        ]
                                                    },
                                                    {
                                                        "type": "separator",
                                                        "margin": "md"
                                                    },
                                                    {
                                                        "type": "box",
                                                        "spacing": "sm",
                                                        "layout": "vertical",
                                                        "margin": "xs",
                                                        "contents": [
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "margin": "md",
                                                            "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "เวลาออกงาน  :",
                                                                "size": "sm",
                                                                "contents": []
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": out_time,
                                                                "size": "sm",
                                                                "align": "start",
                                                                "contents": []
                                                            }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "ด้วย  :",
                                                                "size": "sm",
                                                                "contents": []
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": out_type,
                                                                "size": "sm",
                                                                "align": "start",
                                                                "contents": []
                                                            }
                                                            ]
                                                        },
                                                        {
                                                            "type": "box",
                                                            "layout": "horizontal",
                                                            "contents": [
                                                            {
                                                                "type": "text",
                                                                "text": "สถานที่  :",
                                                                "size": "sm",
                                                                "contents": []
                                                            },
                                                            {
                                                                "type": "text",
                                                                "text": out_place,
                                                                "size": "sm",
                                                                "align": "start",
                                                                "wrap": True,
                                                                "contents": []
                                                            }
                                                            ]
                                                        }
                                                        ]
                                                    },
                                                    {
                                                        "type": "separator",
                                                        "margin": "md"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    "footer": {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                    "type": "uri",
                                                    "label": "รายละเอียด",
                                                    "uri": Util().liff_url_profile_detail_askinout,
                                                    "altUri": {
                                                        "desktop" : Util().url_timeat
                                                    }
                                                },
                                                
                                                "color": "#D39D2B",
                                                "style": "primary"
                                            }
                                        ]
                                    }
                                }  


                            }     
                        ]
                
                    }    
            
            except:
                text = str("คุณ "+name+"\nวันที่ : "+str(date)+"\n\nเวลาเข้างาน : "+in_time+"\nด้วย : "+in_type+"\nสถานที่ : "+in_place+"\n____________________\nเวลาออกงาน : "+out_time+" \nด้วย : "+out_type+"\nสถานที่ : "+out_place+"\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)
            
                body = {    
                    "replyToken": str(devicetoken),
                    "messages": [
                        {
                            "type": "flex",
                            "altText": Util().intent_time_work,
                            "contents": 


                            {
                                "type": "bubble",
                                # "size": "giga",
                                "direction": "ltr",
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                            
                                                {
                                                    "type": "text",
                                                    "text": name,
                                                    "weight": "bold",
                                                    "size": "lg",
                                                    "margin": "none",
                                                    "contents": []
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "วันที่ : "+str(date),
                                                    "size": "sm",
                                                    "color": "#D39D2B",
                                                    "contents": []
                                                },
                                                {
                                                    "type": "separator",
                                                    "margin": "md"
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "vertical",
                                                    "spacing": "sm",
                                                    "margin": "xs",
                                                    "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "margin": "md",
                                                        "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "เวลาเข้างาน :",
                                                            "size": "sm",
                                                            "contents": []
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": in_time,
                                                            "size": "sm",
                                                            "contents": []
                                                        }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "ด้วย  :",
                                                    
                                                            "size": "sm",
                                                            "contents": []
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": in_type,
                                                            "size": "sm",
                                                            "align": "start",
                                                            "contents": []
                                                        }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "สถานที่  :",
                                                            "size": "sm",
                                                            "contents": []
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": in_place,
                                                            "size": "sm",
                                                            "align": "start",
                                                            "wrap": True,
                                                            "contents": []
                                                        }
                                                        ]
                                                    }
                                                    ]
                                                },
                                                {
                                                    "type": "separator",
                                                    "margin": "md"
                                                },
                                                {
                                                    "type": "box",
                                                    "spacing": "sm",
                                                    "layout": "vertical",
                                                    "margin": "xs",
                                                    "contents": [
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "margin": "md",
                                                        "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "เวลาออกงาน  :",
                                                            "size": "sm",
                                                            "contents": []
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": out_time,
                                                            "size": "sm",
                                                            "align": "start",
                                                            "contents": []
                                                        }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "ด้วย  :",
                                                            "size": "sm",
                                                            "contents": []
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": out_type,
                                                            "size": "sm",
                                                            "align": "start",
                                                            "contents": []
                                                        }
                                                        ]
                                                    },
                                                    {
                                                        "type": "box",
                                                        "layout": "horizontal",
                                                        "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "สถานที่  :",
                                                            "size": "sm",
                                                            "contents": []
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": out_place,
                                                            "size": "sm",
                                                            "align": "start",
                                                            "wrap": True,
                                                            "contents": []
                                                        }
                                                        ]
                                                    }
                                                    ]
                                                },
                                                {
                                                    "type": "separator",
                                                    "margin": "md"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                "footer": {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                                "type": "uri",
                                                "label": "รายละเอียด",
                                                "uri": Util().liff_url_profile_detail_askinout,
                                                "altUri": {
                                                    "desktop" : Util().url_timeat
                                                }
                                            },
                                            
                                            "color": "#D39D2B",
                                            "style": "primary"
                                        }
                                    ]
                                }
                            }  


                        }     
                    ]
            
                }
        except:
            

            name = str(respons["result"]["result_user"][0]["user_ad_name"])
            text = str("คุณ "+name+"\n\n____________________\nคลิกดูรายละเอียดเวลาเข้าออกงาน\n"+Util().liff_url_profile_detail_askinout)

            body = {    
                "replyToken": str(devicetoken),
                "messages": [
                    {
                        "type": "flex",
                        "altText": Util().intent_time_work,
                        "contents": 


                    {
                        "type": "bubble",
                        # "size": "giga",
                        "direction": "ltr",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                     
                                {
                                    "type": "text",
                                    "text": name,
                                    "weight": "bold",
                                    "size": "lg",
                                    "margin": "none",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": " ",
                                    "size": "sm",
                                    "color": "#D39D2B",
                                    "contents": []
                                },
                               
                                ]
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                            {
                                "type": "button",
                                "action": {
                                "type": "uri",
                                "label": "รายละเอียด",
                                "uri": Util().liff_url_profile_detail_askinout
                                },
                                "color": "#D39D2B",
                                "style": "primary"
                            }
                            ]
                        }
                        }  


                    }     
                ]
        
            }




        headers = {
                'Content-Type': 'application/json',
                'Authorization':  Util().Bearer + Util().serverToken
            }


        response = requests.post(Util().line_api_reply,headers = headers, data=json.dumps(body))
        print(response.status_code)
        print(response.json())


# ResponsMenu("Uc1e2655638774e42ab8cf38043744cdb")