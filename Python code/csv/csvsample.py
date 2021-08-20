import csv

with open("routerlist.csv") as fh:
    csv_list = csv.reader(fh)
    # Loop over each row in csv and leverage the data in code
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device} is in {location.rstrip()} and has IP {ip}.")


    


