import mysql.connector as c
data=c.connect(host="localhost",user="root",passwd="1234",database="mysql")
webs={"facebook.com":["09.30", "17.30"], "instagram.com":["10.30", "17.30"]}



cursor=data.cursor()
website_name=input("enter website name")
starting_time=int(input("enter starting time"))
ending_time=int(input("enter ending time"))
query="insert into website values('{}',{},{})".format(webs.keys(),webs.values(0),webs.values()1)
print()
cursor.execute(query)
data.commit()
print("insterted")
