# Hutterite Bookshelf
All song files and scripts used for the Hutterite Bookshelf app on the Google Play store.

**NOTE**
This repository also contains all of the third party software I used to generate the text from images (which are not included) that I scanned. If you have no interest in the code, and just want the songs, then delete the [Scripts folder](https://github.com/JareBear12418/Hutterite-Bookshelf/tree/8809bacf1f42eb0e3d9ed8f0064f4cd17544e74d/Scripts). Alternatively You can download **ONLY** the song files from this [Google Drive link](https://drive.google.com/file/d/1PbaSoZrwyWx6QPbw7vW9WlH7SbxrSsAL/view?usp=sharing). 

## Code
the [Scripts folder](https://github.com/JareBear12418/Hutterite-Bookshelf/tree/master/Scripts) on this repository is where you can find all of the source code for those programs. Below are each of them, and what they do.
- [Auto_Correct_Text.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/Auto_Correct_Text.py)
  - This script is to correct all errors in the extracted text from the images. When reading text from an image, it doesn't guarentee 100% accuracy, words may be mispelled or there may be artifacts, or non-native characters, this Script corrects the text using the [word fixes.txt](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/word_fixes.txt) for refrence. This file can be modified by addying more word fixes.
- [Auto_Orginize_Text.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/Auto_Orginize_Text.py) 
  - Is only used when your song has numbers, this will neatly sort all paragrahs depending what number it is. It will remove all empty lines, and join all lines together unless it has a number.
- [Auto_Read_Page.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/Auto_Read_Page.py)
  - This script is deprecated and was only used for testing.
- [Auto_Sort_Text.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/Auto_Sort_Text.py)
  - This script splits up the `output.txt` file into smaller files starting from the letter `1.` going till the next `1.`. This is used to organize all the songs into it's own file.
- [Book_Generator.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/Book_Generator.py)
  - This was not used in the development in the Hutterite Bookshelf, but merely just added to this repository so you can convert stories into Foldable books. It uses a text file, that fits that text into spesfic images, and then into a Word Document to print it.
- [GUI.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/GUI.py)
  - This is the graphical User Interface. It supports all the scripts except [Book_Generator.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/Book_Generator.py). It provides an easy to use interface that makes it easy to convert your images to text, you can also choose to use any of the above scripts after text has been generated.
- [List_Generator.py](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/List_Generator.py)
  - Another script that doesn't have much to do with text processing, but more or less make development of the app easier, this was used to generate LARGE lists for all of the songs in the app.
- [word_fixes.txt](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/master/Scripts/word_fixes.txt)
  - Like mentioned above, this file contains alot of word fixes that the [Converte Thread](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/8809bacf1f42eb0e3d9ed8f0064f4cd17544e74d/Scripts/GUI.py#L22) causes because image to text is not 100% accurate, and needs a bit of correcting. **NOTE** These are not ALL of the word fixes that can occur, these are just words that I found while manually going threw all the songs and fixed by hand. I made a list of as many as I could so I would not have to do this process again, because it was horrible! :) 

## Build
This software is still in development. It is usable. **BUT** it can only run from source at the moment, as I have not made a compiled version for this software, and do not intend to anytime soon. 

## Installation
As mentioned above, this software has no offical build, so here are the instructions to run the code from source.

1. Create a virtual enviroment.

```virtualenv [name]```

2. Activate the virtual enviroment.

```[name]/Scripts/activate```

3. Install all requirments with.

```pip install pyqt5 atexit pytesseract docx numpy opencv-python natsort ```

4. Run the `GUI.py` script with.

```python GUI.py```

I can't guarentee that everything installed correctly, or if these are all the requirements, they tend to change, and sometimes need other requirments. You may contact me if any problems occur, or open an issue.
