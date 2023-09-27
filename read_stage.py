import sqlite3
import datetime

# connecting to database
con = sqlite3.connect("sql.db")
cur = con.cursor()

# users requests information
log_file_path = "log.txt"

# open the file to read line by line
file = open(log_file_path, mode="r")
temps = file.readlines()

# split lines to 9 fields and add to database
for temp in temps:
    fields = [temp]

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

    cur.execute("""INSERT INTO logs VALUES (?,?,?,?,?,?,?,?,?,?)""", fields)
    con.commit()
