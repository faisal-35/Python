import csv
fields=['name','branch','year','cgpa']
rows=[['saikot','coe','9.0'],
       ['ali','it','9.3'],
        ['sahil','cse','9.7']]
fileName='univeresity records.csv'
with open(fileName,'w') as csvfile:
    csvwritr=csv.writer(csvfile)
    csvwritr.writerow(fields)
    csvwritr.writerows(rows)
with open(fileName, "r") as file:
    content = file.read()
    
print(content)
    
