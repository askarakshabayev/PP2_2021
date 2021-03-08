import csv
# csv.reader(file, delimiter = ',')

with open('employee.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row[0], row[1])



