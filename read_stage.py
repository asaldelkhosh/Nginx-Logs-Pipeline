log_file_path = "log.txt"

file = open(log_file_path, mode="r")
temps = file.readlines()

for temp in temps:
 fields = [x.strip() for x in temp.split(" ")]
 print(fields)
