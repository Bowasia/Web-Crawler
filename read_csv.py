import csv
with open('data_personal_link_1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
             print(row['Number'], row['Name'],row['Link'])
