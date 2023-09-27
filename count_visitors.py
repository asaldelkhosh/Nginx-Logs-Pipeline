import sqlite3
import datetime


# connecting to database
con = sqlite3.connect("sql.db")
cur = con.cursor()

# input date
time = datetime.date(2017, 3, 9)

# fetch all data
result = cur.execute("SELECT time_local, remote_addr FROM logs")
view = result.fetchall()

# create a set
ip_list = []
for item in view:
    date = item[0]
    # convert date local to datetime.date
    enter_date = datetime.datetime.strptime(date, '[%d/%b/%Y:%H:%M:%S+0000]').date()
    # check if the date is the same
    if enter_date == time:
        # add ip into set
        ip = item[1]
        ip_list.append(ip)

ip_set = set(ip_list)
print(len(ip_set))
