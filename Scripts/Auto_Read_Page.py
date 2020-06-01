import os
import tempfile
import subprocess
import codecs
try: from PIL import Image
except ImportError: import Image
import pytesseract
import os
import glob
from natsort import natsort_keygen
natsort_key = natsort_keygen()

txtfiles = []

filepath = ''
filename = 'songs.txt'
folderlocation = ''
for file in glob.glob(f"{folderlocation}*.png"):
    txtfiles.append(file)
txtfiles.sort(key=natsort_key)
# print(txtfiles)
start = 0
# print((txtfiles[start:]))
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
for i, j in enumerate(txtfiles[start:]):
    path = j
    s = pytesseract.image_to_string(path)
    with codecs.open(filename, 'a', encoding='utf-8', errors="ignore") as f:
        f.write(s + '\n')
    # text_file = codecs.open('All Songs test 1.txt',
    #                         mode='a', encoding='utf-8', errors="ignore")
    # text_file.write(s + '\n')
    # text_file.close()
    print(f'Completed {j} - {i+1}/{len(txtfiles)-start}')
print('done')
