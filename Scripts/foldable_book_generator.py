# Import libraries
from PIL import ImageFont, ImageDraw, Image

# Declare needed variables
TEXT_FILE = 'perils to Christain living - Finished.txt'
TEXT_FILE_CONTENTS = None

FONT_SIZE = 20
FONT = ImageFont.truetype('arial.ttf', FONT_SIZE)

DPI = 300
MARGIN_SIZE = 40
PAPER_SIZE = (11, 8.5) #INCHES
PIXEL_SIZE = (int(PAPER_SIZE[0]*DPI), int(PAPER_SIZE[1]*DPI))

# Read text file
with open(TEXT_FILE, 'r', encoding='utf-8') as file: TEXT_FILE_CONTENTS = file.read()
print(TEXT_FILE_CONTENTS)

# How many lines of text do i have

# How many lines fit into one page with margins 

# Put lines in order of pages

# Figure out order of pages

# How many pages will i need

# Create blank image 
img = Image.new("RGB", PIXEL_SIZE, (255, 255, 255))
img.save("image.png", "PNG")

# Add text to image.
img = Image.open('image.png')
d = ImageDraw.Draw(img)
d.text((10,10), TEXT_FILE_CONTENTS, fill=(0,0,0), font = FONT)
img.save('image.png')

# Add margin if neccasary

# Add page numbers in footer

# 

# Save
