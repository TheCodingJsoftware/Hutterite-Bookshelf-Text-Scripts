def hasNumbers(inputString): return any(char.isdigit() for char in inputString)
def orginize_text(file):
    """Remove all empty lines unless it has a number

    Args:
        file (string): path to file you want to edit
    """
    all_text = []
    with open(file, 'r') as infile: all_text = infile.readlines() 
    import os
    os.remove(file)
    with open(file, 'w') as outfile:
        for line in all_text:
            if not line.strip(): continue  # skip the empty line
            if hasNumbers(line): line = '\n' + line
            outfile.write(line)  # non-empty line. Write it to output