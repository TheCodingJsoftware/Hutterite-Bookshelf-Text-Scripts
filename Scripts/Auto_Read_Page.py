import pytesseract, os, glob, codecs, subprocess
try: from PIL import Image
except ImportError: import Image
# from natsort import natsort_keygen
# natsort_key = natsort_keygen()

# imgFiles = []

# filepath = ''
# filename = 'songs.txt'
# folderlocation = ''
# for file in glob.glob(f"{folderlocation}*.png"):
    # imgFiles.append(file)
# imgFiles.sort(key=natsort_key)
# print(imgFiles)
# start = 0
# print((imgFiles[start:]))
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
def imgtostr(imgFiles, filename, start = 0):
    for i, j in enumerate(imgFiles[start:]):
        path = j
        s = pytesseract.image_to_string(path)
        with codecs.open(filename, 'a', encoding='utf-8', errors="ignore") as f:
            f.write(s + '\n')
        # text_file = codecs.open('All Songs test 1.txt',
        #                         mode='a', encoding='utf-8', errors="ignore")
        # text_file.write(s + '\n')
        # text_file.close()
        print(f'Completed {j} - {i+1}/{len(imgFiles)-start}')
    print('done')
