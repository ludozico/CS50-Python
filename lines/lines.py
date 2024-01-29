""" line counter """
import sys
import os
counter = 0
if len(sys.argv) < 2:
                sys.exit('Too few command-line arguments')
else:
    name = sys.argv[1]
    with open(name,'r') as file:
        for line in file:
                if len(sys.argv) > 2:
                     sys.exit('Too many command-line arguments')
                elif not os.path.exists(name):
                     sys.exit('File does not exist')
                elif name[-3:] != '.py':
                     sys.exit('Not a Python file')
                elif line.lstrip().startswith('#'):
                     pass
                elif line.isspace():
                     pass
                else:
                      counter += 1

print(counter)
