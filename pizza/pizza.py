""" pizza task """
import sys
import os
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
elif sys.argv[1][-4:] != '.csv' and os.path.exists(sys.argv[1]):
        sys.exit('Not a CSV file')
elif not os.path.exists(sys.argv[1]):
        sys.exit('File does not exist')
else:
    with open(sys.argv[1],'r') as file:
            menu = list(csv.reader(file))
            menufinal = tabulate(menu,headers='firstrow',tablefmt='grid')
            print(menufinal)
