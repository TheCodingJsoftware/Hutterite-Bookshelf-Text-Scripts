import os
from natsort import natsort_keygen
files = []
filepath = ''
for file in os.listdir(filepath):
    if file.endswith(".txt"):
        file = file.replace('.txt', '')
        file = file.replace('-', ' ')
        file = '"' + file + '"' + ","
        files.append(file)
        # print(file)

natsort_key = natsort_keygen()
files.sort(key=natsort_key)
with open('LIST.txt', 'w+', encoding='utf-8') as f:
    for i in files:
        # print(i)
        f.write(i + '\n')
# 99 Herr Jesu Christ du
