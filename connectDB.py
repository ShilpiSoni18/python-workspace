import pymysql
from datetime import date

# This will connect to mysql database
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="shilpi",
    database="shilpi"
)

# This will return the connection address which means it is successfully connected
print(conn);

#Created a cursor which is responsible for doing operations on database
cursor=conn.cursor()

# The code below will create a table named as event in database shilpi

create_table='''Create table event(
    event_id INTEGER PRIMARY KEY,
    event_name TEXT NOT NULL,
    event_venue TEXT NOT NULL,
    event_date DATE
)'''
cursor.execute(create_table)
conn.commit()
conn.close()
print("table created successfully")


# Inserting data within the recently created table (event)

event_date= date(2025,11,24)
insert_query='''Insert into event(event_id,event_name,event_venue,event_date) VALUES (101,"Wedding","Grand Imperial",%s)'''
values=(event_date)
cursor.execute(insert_query,values)
conn.commit()
print("Data added...")
