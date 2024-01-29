""" shirt exercise! """
import sys
import os
from PIL import Image, ImageOps

sys.argv[1] = sys.argv[1].lower()
sys.argv[2] = sys.argv[2].lower()

if len(sys.argv) < 3:
     sys.exit('Too few command-line arguments')

elif len(sys.argv) > 3:
     sys.exit('Too many command-line arguments')

elif not os.path.exists(sys.argv[1]):
     sys.exit('Input does not exist')

elif sys.argv[1][-3:] != sys.argv[2][-3:]:
     sys.exit('Input does not exist')

elif sys.argv[1][-4:] != '.jpg' and sys.argv[1][-5:] != '.jpeg' and sys.argv[1][-4:] != '.png':
     sys.exit('Invalid input')

elif sys.argv[2][-4:] != '.jpg' and sys.argv[2][-5:] != '.jpeg' and sys.argv[2][-4:] != '.png':
     sys.exit('Invalid output')

else:
    output = Image.open(sys.argv[1], mode='r')
    output = ImageOps.fit(output,(600,600))
    shirt = Image.open('shirt.png')
    output.paste(shirt, box=(0, 0), mask=shirt)
    output.save(sys.argv[2])


