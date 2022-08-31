import json
from re import A
from python.Util import Util

from python.Api_backend.GetDataUserDocotrAppointment import GetDataUserDocotrAppointment
from python.Api_backend.PostUserDetailWithAd import PostUserDetailWithAd
class ResponsContentFlexDoctorAppointment:
    
    def __new__(self,user_ad_code):
        
        try:
   
        
            user_detail = PostUserDetailWithAd(user_ad_code)
            user_doctor_appointment = GetDataUserDocotrAppointment(user_ad_code)

            name = user_detail['result']['personal']['PersonalName']

            if len(user_doctor_appointment) > 0:
        
                appointment =  {
                            "type":"box",
                            "layout":"vertical",
                            "backgroundColor":"#d9ebce",
                            "contents":[]
                        }

                if len(user_doctor_appointment) > 2:
                    for i in range(2):
                        AppointDateTime = str(user_doctor_appointment[i]['AppointDateTime'])
                        ClinicName = str(user_doctor_appointment[i]['ClinicCode'])+" "+str(user_doctor_appointment[i]['ClinicName'])
                        DocName = str(user_doctor_appointment[i]['DocName'])
                        DocName = DocName.split('\\')
                        DocName = str(DocName[1])+str(DocName[0])
                        Hn = str(user_doctor_appointment[i]['HN'])
                    
                        date_time_str = AppointDateTime.split()
                        date = date_time_str[0]
                        date = date_time_str[0].split('-')
                        year    = date[0]
                        month   = date[1]
                        day     = date[2]
                        month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[int(month)]
                        thai_year = int(year) + 543
                        time_str = date_time_str[1]
                        time_str = time_str.split(':')
                        time_str = str(str(time_str[0])+":"+str(time_str[1]))
                    
                        AppointDateTime = str(str(day)+" "+str(month_name)+" "+str(thai_year))
                    
        
                        appointment_detail =  {
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
                                            "text":"วันที่นัด :",
                                            "size":"sm",
                                            "color":"#555555",
                                            "flex":0
                                        },
                                        {
                                            "type":"text",
                                            "text": str(AppointDateTime)+" เวลา "+str(time_str)+" น.",
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
                                            "text":"คลีนิค :",
                                            "size":"sm",
                                            "color":"#555555",
                                            "flex":0
                                        },
                                        {
                                            "type":"text",
                                            "text":str(ClinicName),
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
                                        "text":"แพทย์ :",
                                        "size":"sm",
                                        "color":"#555555"
                                        },
                                        {
                                        "type":"text",
                                        "text":str(DocName),
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

                            ]
                        }
                        appointment['contents'].append(appointment_detail)
                    
                    content =  {
                            "type":"bubble",
                            "hero":{
                                "type":"image",
                                "url":"https://webhook.toat.co.th/linebot/web/src/hos_1.jpg",
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
                                        "text":"ใบนัด รพ. สวนเบญจกิติฯ",
                                        "weight":"bold",
                                        "color":"#1DB446",
                                        "size":"xl"
                                    },
                                    {
                                        "type":"text",
                                        "text":"HN : "+str(Hn),
                                        "weight":"bold",
                                        "size":"md",
                                        "margin":"md"
                                    },
                                    {
                                        "type":"text",
                                        "text":str(name),
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
                                    appointment

                        
                                ]
                            },
                            # "styles":{
                            #     "footer":{
                            #         "separator":True
                            #     }
                            # }
                             "footer": {
                                "type": "box",
                                "layout": "horizontal",
                                "backgroundColor":"#d9ebce",
                                "contents": [
                                    {
                                        "type": "button",
                                        "action": {
                                            "type": "uri",
                                            "label": "รายละเอียด",
                                            "uri": Util().liff_url_detail_doctor_appointment+str(user_ad_code),
                                        
                                        },
                                        
                                        "color": "#1DB446",
                                        "style": "primary"
                                    }
                                ]
                            }
                        }
                
                else:
                    for i in range(len(user_doctor_appointment)):
                        AppointDateTime = str(user_doctor_appointment[i]['AppointDateTime'])
                        ClinicName = str(user_doctor_appointment[i]['ClinicCode'])+" "+str(user_doctor_appointment[i]['ClinicName'])
                        DocName = str(user_doctor_appointment[i]['DocName'])
                        DocName = DocName.split('\\')
                        DocName = str(DocName[1])+str(DocName[0])
                        Hn = str(user_doctor_appointment[i]['HN'])
                    
                        date_time_str = AppointDateTime.split()
                        date = date_time_str[0]
                        date = date_time_str[0].split('-')
                        year    = date[0]
                        month   = date[1]
                        day     = date[2]
                        month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[int(month)]
                        thai_year = int(year) + 543
                        time_str = date_time_str[1]
                        time_str = time_str.split(':')
                        time_str = str(str(time_str[0])+":"+str(time_str[1]))
                    
                        AppointDateTime = str(str(day)+" "+str(month_name)+" "+str(thai_year))
                    
        
                        appointment_detail =  {
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
                                            "text":"วันที่นัด :",
                                            "size":"sm",
                                            "color":"#555555",
                                            "flex":0
                                        },
                                        {
                                            "type":"text",
                                            "text": str(AppointDateTime)+" เวลา "+str(time_str)+" น.",
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
                                            "text":"คลีนิค :",
                                            "size":"sm",
                                            "color":"#555555",
                                            "flex":0
                                        },
                                        {
                                            "type":"text",
                                            "text":str(ClinicName),
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
                                        "text":"แพทย์ :",
                                        "size":"sm",
                                        "color":"#555555"
                                        },
                                        {
                                        "type":"text",
                                        "text":str(DocName),
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

                            ]
                        }
                        appointment['contents'].append(appointment_detail)

                    content =  {
                            "type":"bubble",
                            "hero":{
                                "type":"image",
                                "url":"https://webhook.toat.co.th/linebot/web/src/hos_1.jpg",
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
                                        "text":"ใบนัด รพ. สวนเบญจกิติฯ",
                                        "weight":"bold",
                                        "color":"#1DB446",
                                        "size":"xl"
                                    },
                                    {
                                        "type":"text",
                                        "text":"HN : "+str(Hn),
                                        "weight":"bold",
                                        "size":"md",
                                        "margin":"md"
                                    },
                                    {
                                        "type":"text",
                                        "text":str(name),
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
                                    appointment

                        
                                ]
                            },
                            "styles":{
                                "footer":{
                                    "separator":True
                                }
                            }
                            #  "footer": {
                            #     "type": "box",
                            #     "layout": "horizontal",
                            #     "backgroundColor":"#d9ebce",
                            #     "contents": [
                            #         {
                            #             "type": "button",
                            #             "action": {
                            #                 "type": "uri",
                            #                 "label": "รายละเอียด",
                            #                 "uri": Util().liff_url_detail_doctor_appointment+str(user_ad_code),
                                        
                            #             },
                                        
                            #             "color": "#1DB446",
                            #             "style": "primary"
                            #         }
                            #     ]
                            # }
                        }
                        
                status = "normal"
            
            else :

                appointment =  {
                                    "type":"box",
                                    "layout":"vertical",
                                    "backgroundColor":"#d9ebce",
                                    "contents":[
                                        
                                    ]
                                }
                content =  {
                            "type":"bubble",
                            "hero":{
                                "type":"image",
                                "url":"https://webhook.toat.co.th/linebot/web/src/hos_1.jpg",
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
                                        "text":"ใบนัด รพ. สวนเบญจกิติฯ",
                                        "weight":"bold",
                                        "color":"#1DB446",
                                        "size":"xl"
                                    },
                                
                                    {
                                        "type":"text",
                                        "text":str(name),
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
                                    appointment

                        
                                ]
                            },
                            "styles":{
                                "footer":{
                                    "separator":True
                                }
                            }
                        }
                status = "except"

            
        except:
            content = {}
            status = "except"

      
 
        return status,content