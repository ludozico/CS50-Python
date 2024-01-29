""" figlet chore """
# imports
import sys
from pyfiglet import Figlet
import random

# list of fonts
list = [
    "3-d",
    "3x5",
    "5lineoblique",
    "acrobatic",
    "alligator",
    "alligator2",
    "alphabet",
    "avatar",
    "banner",
    "banner3-D",
    "banner3",
    "banner4",
    "barbwire",
    "basic",
    "bell",
    "big",
    "bigchief",
    "binary",
    "block",
    "bubble",
    "bulbhead",
    "calgphy2",
    "caligraphy",
    "catwalk",
    "chunky",
    "coinstak",
    "colossal",
    "computer",
    "contessa",
    "contrast",
    "cosmic",
    "cosmike",
    "cricket",
    "cyberlarge",
    "cybermedium",
    "cybersmall",
    "diamond",
    "digital",
    "doh",
    "doom",
    "dotmatrix",
    "drpepper",
    "eftichess",
    "eftifont",
    "eftipiti",
    "eftirobot",
    "eftitalic",
    "eftiwall",
    "eftiwater",
    "epic",
    "fender",
    "fourtops",
    "fuzzy",
    "goofy",
    "gothic",
    "graffiti",
    "hollywood",
    "invita",
    "isometric1",
    "isometric2",
    "isometric3",
    "isometric4",
    "italic",
    "ivrit",
    "jazmine",
    "jerusalem",
    "katakana",
    "kban",
    "larry3d",
    "lcd",
    "lean",
    "letters",
    "linux",
    "lockergnome",
    "madrid",
    "marquee",
    "maxfour",
    "mike",
    "mini",
    "mirror",
    "mnemonic",
    "morse",
    "moscow",
    "nancyj-fancy",
    "nancyj-underlined",
    "nancyj",
    "nipples",
    "ntgreek",
    "o8",
    "ogre",
    "pawp",
    "peaks",
    "pebbles",
    "pepper",
    "poison",
    "puffy",
    "pyramid",
    "rectangles",
    "relief",
    "relief2",
    "rev",
    "roman",
    "rot13",
    "rounded",
    "rowancap",
    "rozzo",
    "runic",
    "runyc",
    "sblood",
    "script",
    "serifcap",
    "shadow",
    "short",
    "slant",
    "slide",
    "slscript",
    "small",
    "smisome1",
    "smkeyboard",
    "smscript",
    "smshadow",
    "smslant",
    "smtengwar",
    "speed",
    "stampatello",
    "standard",
    "starwars",
    "stellar",
    "stop",
    "straight",
    "tanja",
    "tengwar",
    "term",
    "thick",
    "thin",
    "threepoint",
    "ticks",
    "ticksslant",
    "tinker-toy",
    "tombstone",
    "trek",
    "tsalagi",
    "twopoint",
    "univers",
    "usaflag",
    "weird"
]

# define mode
if len(sys.argv) == 1:
        mode = 'random'
elif len(sys.argv) == 3 and sys.argv[1] in ('-f' or '--font'):
        if sys.argv[2] in list:
             mode = 'uchoice'
        else:
             sys.exit(1)
# break the program
else:
    sys.exit(1)
#gets input
uinput = input()
# inializes my object
f = Figlet()

# Set the font and render the text
if mode == 'random':
    style = random.choice(list)
    f.setFont(font=style)
else:  # User choice mode
    style = sys.argv[2]
    f.setFont(font=style)

# Output the text in the desired font
print(f.renderText(uinput))
