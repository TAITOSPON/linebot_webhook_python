import requests
from bs4 import BeautifulSoup
from datetime import datetime

class TimeThai:

    def __new__(self):
        url = "https://www.timeanddate.com/worldclock/fullscreen.html?n=28"
        web_data = requests.get(url)

        soup = BeautifulSoup(web_data.text,'html.parser')


        find_i_time = soup.find(id="i_time")
        find_i_date = soup.find(id="i_date")


        for i in find_i_time:
            i_time = i

        for i in find_i_date:
            i_date = i


        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")

        date = str(year+"-"+month+"-"+day)
   
        value = str(i_time+":"+date+":"+i_date)
        return value

# TimeThai()