""" scourgify (love the hp examples <3) task """
import sys
import os
import csv

if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
elif sys.argv[1][-4:] != '.csv' or not os.path.exists(sys.argv[1]):
        sys.exit('Could not read invalid_file.csv')
else:
    with open(sys.argv[1],'r') as file:
        before = list(csv.reader(file))
        newlist = [['first','last','house']]
        for item in before[1:]:
            lname, fname = item[0].split(',')
            newlist.append([fname.strip(),lname.strip(),item[1]])
    with open(sys.argv[2],'w') as file:
        after = csv.writer(file)
        for item in newlist:
              after.writerow(item)
