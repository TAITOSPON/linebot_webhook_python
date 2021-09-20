
import requests
import json

from python.Api_backend.PostDataTimeAt import PostDataTimeAt

from python.Util import Util

class ResponsTimeAtFlex:
    
    def __init__(self,devicetoken,body):
       

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