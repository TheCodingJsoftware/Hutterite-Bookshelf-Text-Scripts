file = 'Kleine Gesangbuch/kleine gesang buch.txt'
def hasNumbers(inputString): return any(char.isdigit() for char in inputString)
with open(file) as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        if hasNumbers(line): line = '\n' + line
        outfile.write(line)  # non-empty line. Write it to output