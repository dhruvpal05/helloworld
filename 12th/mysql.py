import time
import mysql.connector as c
data=c.connect(host="localhost",user="root",passwd="1234",database="test")
from datetime import datetime as d
cursor=data.cursor()
website_name=input("enter website name")
starting_date=int(input("enter strating date"))
starting_time=int(input("enter starting time"))
ending_date=int(input('enter ending date'))
ending_time=int(input("enter ending time"))
query="insert into website values('{}',{},{},{},{})".format(website_name,starting_date,starting_time,ending_date,ending_time)
cursor.execute(query)
data.commit()

'''host="C:\Windows\System32\drivers\etc\hosts"
localip="127.0.0.1"
#website_list=["www.facebook.com","www.google.com","www.instagram.com","www.github.com"]

while True:
    if d(d.now().year,d.now().month,d.now().day,9)<d.now()<d(d.now().year,d.now().month,d.now().day,23):
        with open(host,"r+") as file:
            content=file.read()
            for website in website_name:
                if website in content:
                    pass
                else:
                    file.write("        "+localip+"       "+website+"\n")
                    print("done")'''

