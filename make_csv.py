import csv

with open ('cars.csv', 'w', newline ='') as file:
    write = csv.writer(file)

    write.writerow(['Make', 'Model', 'Year'])
    write.writerow(['Honda', 'Accord', '2008'])
    write.writerow(['Acura','RSX','2006'])
    write.writerow(['BMW','M3','2020'])
