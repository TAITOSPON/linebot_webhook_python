
import requests
import json

from python.Util import Util
from python.Api_backend.PostUserWithUid import PostUserWithUid
from python.Api_backend.PostDataPermitSaleReport import PostDataPermitSaleReport
from python.Respons_user.ResponsWorkSystem import ResponsWorkSystem
from python.Respons_user.ResponsReply import ResponsReply

class CheckPermitSaleReport:
    
    def __new__(self,user,user_line_uid):

        try:
            result_user = PostUserWithUid(user_line_uid)
            user_ad_code = str(result_user[0]["user_ad_code"])
            
            
            status_permit = PostDataPermitSaleReport(user_ad_code)
            status_permit = str(status_permit["status"])

            # ResponsReply(Util().serverToken,user,str(status_permit ))
            
            if status_permit == "true":
                ResponsWorkSystem(user)
                # ResponsReply(Util().serverToken,user,"Developing..\uDBC0\uDC84\nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")
            elif status_permit == "false":
                # ResponsWorkSystem(user)
                ResponsReply(Util().serverToken,user,"Developing..\uDBC0\uDC84\nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")




        except:
            ResponsReply(Util().serverToken,user,"Developing..\uDBC0\uDC84\nสำนักเทคโนโลยีสารสนเทศ\udbc0\udc30\udbc0\udc3b")
    




