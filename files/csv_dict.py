import csv

mydict=[
    {"first":"Harry","last":"Potter"},
    {"first":"Ron","last":"Weasely"}
]

with open("new.csv",'w') as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last"])
    writer.writeheader()
    writer.writerows(mydict)

with open("new.csv") as csvfile:
    file = csv.DictReader(csvfile)
    for row in file:
        print(row)