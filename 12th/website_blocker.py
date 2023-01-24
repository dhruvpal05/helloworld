import time
from datetime import datetime as d
host="C:\Windows\System32\drivers\etc\hosts"
localip="127.0.0.1"
website_list=["www.facebook.com","www.google.com","www.instagram.com"]

while True:
    if d(d.now().year,d.now().month,d.now().day,9)<d.now()<d(d.now().year,d.now().month,d.now().day,23):
        with open(host,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(        localip       +""+website+"\n")
                    print("done")


