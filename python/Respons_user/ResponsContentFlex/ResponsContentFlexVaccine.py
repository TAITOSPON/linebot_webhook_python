

import json
from python.Util import Util

from python.Api_backend.GetDataUserVaccine import GetDataUserVaccine

class ResponsContentFlexVaccine:

    def __new__(self,user_ad_code):

        try:
            
            status,data_vaccine = GetDataUserVaccine(user_ad_code)

            if  data_vaccine != "null": 

                status = "normal"    
                if data_vaccine["Appointment"] != "":   #มีนัด

                    if data_vaccine["VaccineDate2"] == "":  #นัดเข็ม 2
                            
                        body = {
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
                        }

                    else :   #นัดเข็ม 3
                        
                        body = {
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
                        }


                else : #ไม่มีนัด
                    
                    if data_vaccine["VaccineDate3"] != "": #ครบ 3 เข็ม
                        
                        body = {
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
                        }

                            
                    else :  #ครบ 2 เข็ม
                        if data_vaccine["VaccineDate2"] == "": #ครบ 2 เข็ม (no data)
                            
                        
                            body = {
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
                            }

                    
                        else :
                            
                            body = {
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
                            }

                                    
            else:
                status = "except"  
                body = {}    

        except :

            status = "except"  
            body = {}    

      
 
        return status,body