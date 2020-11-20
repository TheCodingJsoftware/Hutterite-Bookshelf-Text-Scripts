# Import libraries
from PIL import ImageFont, ImageDraw, Image

# Declare constant variables
TEXT_FILE = 'perils to Christain living - Finished.txt'
TEXT_FILE_CONTENTS = None
LINES_PER_PAGE = 26
CHARACTERS_PER_LINE = 55

FONT_SIZE = 20
FONT = ImageFont.truetype('arial.ttf', FONT_SIZE)

DPI = 300
MARGIN_SIZE = 40
PAPER_SIZE = (11, 8.5) #INCHES
PIXEL_SIZE = (int(PAPER_SIZE[0]*DPI), int(PAPER_SIZE[1]*DPI))

# Declare global variables
orginized_text_file_contents = []
orginized_line = []
# Read text file
with open(TEXT_FILE, 'r', encoding='utf-8') as file: TEXT_FILE_CONTENTS = file.readlines()

# Orginize text to fit on pages (start to end)
for line_index, line_contents in enumerate(TEXT_FILE_CONTENTS):
    words = line_contents.split(' ')
    char_count = 0
    for word_index, word_contents in enumerate(words):
        for char_index, char_contents in enumerate(word_contents):
            char_count += 1
            orginized_line += word_contents + ' '
            if char_count >= CHARACTERS_PER_LINE:
                
                print(word_contents)
    

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
