import csv
# csv.writer
# csv.writerow

with open("emoployee1.csv", mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(["Askar", "IT", "February"])
    employee_writer.writerow(["Balzhan", "Support", "November"])
    employee_writer.writerow(["aaa", "bbb", "ccc"])
