def extract_text(savelocation, file):
    # Open the File you want to orginze text from.
    with open(file, 'r', encoding='utf-8') as f:
        # read all the lines of the file this gives you a large list with each line.
        lines = f.readlines()
        # creating a list to store all the lines that have '1.' written on that line.
        ones_index = []
        # loop over every line inside the lines list.
        for idx, line in enumerate(lines):
            # if the line has `1.` then add that to the ones_index list.
            # if '1.' in line and not '11.' in line and not '21.' in line and not '31.' in line and not '41.' in line and not '51.' in line and not '61.' in line:
            if line[0] == '1' and line[1] == '.':
                lineIndex0 = line[0]
                lineIndex1 = line[1]
                # if not '11.' in line and not '21.' in line and not '31.' in line and not '41.' in line and not '51.' in line and not '61.' in line:
                if lineIndex0 == '1' and lineIndex1 == '.':
                    ones_index.append(idx)
        '''
        here we a the last line of the text file to the ones_index
        We do so when the last `1.` is found it gets all the text.
        It's more important for layer.
        '''
        ones_index[len(lines):] = [len(lines)]
        # We loop over all the ones_indexs elements.
        for j, i in enumerate(range(len(ones_index)-1)):
            # we set a variable to be the number we are currently in the iteration
            start = ones_index[i]
            # our stop variale is the next element in a list.
            stop = ones_index[i+1]
            ''' -=-=-=-=-= Make title =-=-=-=-=-=- '''
            # We set our title variable to the current lines text.
            title = lines[start].replace('\n', '')
            # if our title has punctiation at the end we want to remove it.
            # if title.endswith(',') or title.endswith('-') or title.endswith('.'):
            # title = title[:-1]
            title = title.replace(',', '')
            title = title.replace('?', '')
            title = title.replace('!', '')
            title = title.replace("'", '')
            title = title.replace("’", '')
            title = title.replace(":", '')
            title = title.replace("|", '')
            title = title.replace('\n', '')
            # we split the title into a list where ever a space is (' ')
            title = title.split('.')
            # We remove the first element in our splited list, because it always contains a number
            title.pop(0)
            # title = title.replace('.', '')
            # we join our title back together again with spaces (' ')
            title = ' '.join(title)
            # We set the number to be the number of the iteration we are in, in the loop.
            title = title.split(',')
            title1 = title[0]
            title2 = lines[start+1].replace('\n', '')

            if (title1.endswith('-')):
                title1 = title1.replace('-', '')
                title2 = title2.replace(',', ' ')
                title2 = title2.replace('!', '')
                title2 = title2.replace("'", '')
                title = str(j + 1) + '.' + title1 + title2
            else:
                title = str(j + 1) + '.' + title1
            title = title.replace('\t', ' ')
            '''
            Create a new file that is called what we set our title to.
            Write all the lines from the start variable to the stop variable.
            '''
            with open('{}\\{}.txt'.format(savelocation, title), 'w+', encoding='utf-8') as f:
                f.write(''.join(lines[start:stop]))
