import csv
import json

with open ('names.json', 'r') as file:
    json = json.load(file)
    names = json["names"]

with open ('newcsv.csv', 'w', newline='') as file:
    fieldnames = names[0].keys()
    write = csv.DictWriter(file, fieldnames)
    for name in names:
        write.writerow(name)