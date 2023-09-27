import sqlite3
import datetime


con = sqlite3.connect("sql.db")
cur = con.cursor()

log_file_path = "log.txt"

file = open(log_file_path, mode="r")
temps = file.readlines()

for temp in temps:
    fields = []
    fields.append(temp)
    split_line = temp.split(" ")
    fields.append(split_line[0])
    fields.append(split_line[3] + split_line[4])
    fields.append(split_line[5])
    fields.append(split_line[6])
    fields.append(split_line[8])
    fields.append(split_line[9])
    fields.append(split_line[10])
    fields.append(" ".join(split_line[11:]))
    fields.append(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
    print(fields)
    cur.execute("""INSERT INTO logs VALUES (?,?,?,?,?,?,?,?,?,?)""", fields)
    con.commit()
