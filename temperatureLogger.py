import mysql.connector
from datetime import date, datetime

try:
    conn = mysql.connector.connect(user='temperatureLogger',
                                   password='tempLogger123',
                                   host='192.168.1.2',
                                   database='homeData')
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))


cursor = conn.cursor()

add_temperature = ("INSERT INTO temperature "
                   "(timeDate, value) "
                   "VALUES (%s, %s)")

now = datetime.now()
data = (now, 19.5)

try:
    cursor.execute(add_temperature, data)
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

conn.commit()
cursor.close()
conn.close()
