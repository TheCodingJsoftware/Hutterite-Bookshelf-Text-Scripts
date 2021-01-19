<p align="center">
    <a href="https://img.shields.io/github/license/JareBear12418/Hutterite-Bookshelf?color=blue&style=for-the-badge" alt="License">
        <img src="https://img.shields.io/github/license/JareBear12418/Hutterite-Bookshelf?color=blue&style=for-the-badge" /></a>
    <a href="https://img.shields.io/github/repo-size/JareBear12418/Hutterite-Bookshelf?label=Size&style=for-the-badge" alt="Size">
        <img src="https://img.shields.io/github/repo-size/JareBear12418/Hutterite-Bookshelf?label=Size&style=for-the-badge" /></a>
    <a href="https://img.shields.io/github/languages/count/JareBear12418/Hutterite-Bookshelf?style=for-the-badge">
        <img src="https://img.shields.io/github/languages/count/JareBear12418/Hutterite-Bookshelf?style=for-the-badge"
            alt="Languages"></a>
    <a href="https://img.shields.io/github/languages/top/JareBear12418/Hutterite-Bookshelf?style=for-the-badge">
        <img src="https://img.shields.io/github/languages/top/JareBear12418/Hutterite-Bookshelf?style=for-the-badge"
            alt="Top_Language"></a>
</p>

# Hutterite Bookshelf
All song files and scripts used for the development of the Hutterite Bookshelf app on the Google Play store.


**NOTE**
This repository contains all of the third party software I used to generate the text from images (which are not included) that I scanned. If you have no interest in the code, and just want the songs, then delete the [Scripts folder](https://github.com/JareBear12418/Hutterite-Bookshelf/tree/8809bacf1f42eb0e3d9ed8f0064f4cd17544e74d/Scripts). Alternatively You can download **ONLY** the song files from this [Google Drive link](https://drive.google.com/file/d/1PbaSoZrwyWx6QPbw7vW9WlH7SbxrSsAL/view?usp=sharing). 

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
  - Like mentioned above, this file contains alot of word fixes that the [ConvertThread](https://github.com/JareBear12418/Hutterite-Bookshelf/blob/8809bacf1f42eb0e3d9ed8f0064f4cd17544e74d/Scripts/GUI.py#L22) because because image to text is not 100% accurate, and needs a bit of correcting. **NOTE** These are not ALL of the word fixes that can occur, these are just words that I found while manually going threw all the songs and fixed by hand. I made a list of as many as I could so I would not have to do this process again, because it was horrible! :) 

## Build
This software is still in development. It is usable. **BUT** it can only run from source at the moment, as I have not made a compiled version for this software, and do not intend to anytime soon. [Instructions to install.](https://github.com/JareBear12418/Hutterite-Bookshelf#installation) 

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

## Request a Custom book arrangment
If you want to a request a special arrangment of songs unique to either you or your community, please provide the following:
1. The code you want to use to grant access to the book. *(ex. [community_name][event], it can be however you please.)*
2. For the songs please provide the following:
    - Exact scanned copy of the songs you want added, or the text files for the songs.
    - The exact order you want the songs in.
3. The name that you want for the book. *(ex. ("[your_name]/[community_name]) Song book", Or just like the code name, but spaced and capital letters)*
4. An Icon for the book (Optional). 
    - Dimensions (recommended): (128x128) or any 1:1 size ratio.
    - Must be white.
    - If you choose to not provide an Icon, the default icon for books will be used. 
5. Any other information you feel is important to include about your request.

**NOTE**
Your request will **NOT** be fulfilled over night or the next day, or possibly even the next week. 
This is a free service and is achieved in my own time, so please be reasonable and patient. They take lots of time and testing to complete.

Your request is added **via an update** so if I reply back saying your request is completed and ready to be used. **Make sure you update to the latest version** 

If you are not pleased by the code/name/icon/song arrangment then please contact me the code that is used for that book, and your requested changes. **The changes will be added via the next update.**

Why don't you do this threw the cloud?
- I hate dealing with the cloud, it adds unnecessary complexity.
- Due to how some community networks are set up, by blocking alot of website and services, it could provide a further problems to your network admin.

## FAQ
### Why did you provide all these songs for free?
- These songs are the exact versions found in all of the Hutterite Books, Please note, I do not own any of these songs. I am just providing them for anyone to use if they want to make an app similar to mine, Or use small songs to print small booklets for certain events. 
- Going about why I provide these songs for free, again, I don't own ownership to these songs. I do have physical copies of song books that were used to get the text for all of these. Which leads me to my next point.
- Getting text from images is a super tedious process, and no one should really edit 3000 songs by hand (It's crazy). I don't want anyone to repeat the same process like I did, as it really makes no sense to do so. If you just want to have 'ownership' to songs that you got yourself, it really doesn't matter. These songs are provided freely for anyone and everyone to use openly, so you don't have to.

### How long did it take to develop the Hutterite Bookshelf?
- Started development on March 4, 2020. Since then and some gaps between I've been working almost fully on the app. I'm always trying to make it more unique and stand out to the other competitor apps.

### Why did you make 'another' Bookshelf app if there are already good ones?
- Complicated question, I was super dissatisfied with both [Bookshelf](https://play.google.com/store/apps/details?id=com.cedrontech.adb) and [IchSing](https://play.google.com/store/apps/details?id=io.cs.ichsing). Don't get me wrong, they are great apps. But they lack features that I think a Digital Song book should have, and features that I personaly wanted. 
  - One small issue I had was, the lack of **dark theme**. Silly as it may seem, but this is true. Being a developer and spending lots of my day staring a screen is hard on the eyes, I payed extra attention to detail when designing dark theme for my app, simply because it's something any new application should include. I am aware that IchSing does provide dark theme.
  - Another feature that the other song book apps don't deliver as well is searching, while IchSing has great searching, but the original Bookshelf does not. I still have alot of work to do with our search engine in the Hutterite Bookshelf app to match that of IchSing. 
  - From a design aspect, both apps look really similar, mainly because they were developed in Kotlin, and/or Java using Android Studio. The Hutterite Bookshelf was made using a Game Engine and written in C# which is basicly C's younger brother, being from same family of programming languages, but C# has been more modernized. Is that better? No. But this gives me ALOT more control on the most important aspect of an app. The User Experience and User Interface. I'm not limited by the tools Android gives you with their native UI elements. I designed my own UI from the ground up, giving it a more relaxing/refresing and new look.
  - The lack of customizability in both apps for me personaly is a no no. 
  - One final issue that really dissapointed me from both apps, is the bookmark system, both of them have no bookmarking. Being able to bookmark a song, and returning right where you left off, is a necessity in for any digital book app. This feature is one that both apps do not have.
- This may seem like just a rant about me complaining about the other song books. But it's not. Im comparing diffrences. I took things I didn't like about either app and tried my best to make my own version of how I think a song book app should be made.

### Will you be adding playbacks for each song? 
- Short answer.
  - No.
- Reason
  - This is where IchSing is way better, because it is probably more community driven *(this is just a guess)*. The Hutterite Bookshelf was developed by only one person (me). Other support such as testing and constructive criticism was provided by family. This means, I don't have tools/equipment/time/resources to sing every song and record it. The app is optimized and setup for such a feature, but until I am capable of singing and recording all the songs to superb quality, this sadly won't be added anytime soon.

### Will you be adding more books?
- Short answer.
  - YES!
- Explanation.
  - The Hutterite Bookshelf has a "code" system. Meaning you can [Request](https://github.com/JareBear12418/Hutterite-Bookshelf#request-a-custom-book-arrangment) to have a song book or anything added just for you, only you can know the code. Who ever uses the code, has that book. An example being: A song book that is unique to your community only, you can have that book added to our app, and used freely by entering special code to be used by anyone in your community.
  - We also are working on a large collection of Hutterite Stories/Books to soon be added to the app. These have been provided to us to freely use in our app.

### Will you add support for diffrent OS's?
- Yes! Once the app is in a stable version, Support will be added for Windows and soon IOS!
    
### Why is the app so big in size?
- Due to the nature of being built in a Game Engine it makes it harder to optimize the size of the app. We are working very hard and are making headways to get the app under 15mb. Alot of the size is the Game Engines code itself. Because it does not use Android's native support, it needs alot more space to add its own Native support.

### Why is the app laggy when viewing long songs?
- Simple answer:
  - This is a limitation of the Game Engine we used to develop the app. 
- Nerd and technical answer:
  - Due to how text is being rendered in the game engine. Each letter is a whats called a 'mesh'. What's a mesh? A mesh is basicly a shape, like a circle, square. Just like a 2d square has 4 vertexes (2d triangle has 3), and a circle has MANY vertexes. This is exactly how text is being rendered, each letter has many vertexes (depending on the text size). Rendering 1000s of *'shapes'(letters)* with many vertexes is bound to have a critcal impact on performace. To cut it simply, this Game Engine, isn't primarily optimized for "Text rendering". 
  - Can't you just lower the vertex count per letter?
    - No. We want the text to be as crisp as possible and easy to read, and it's not something we can just change.
  - Why did we stick with the Game Engine if the primary feature is to look at text?
    - Let's back up a bit to when I started developing the app. This was the first feature I tested, and the first problem I encountered. **This wasn't the issue with 97% of the songs.** But mainly with books. We are still working on a concrete way to optimize text rendering for these large text files. This is just an issue that I have to work around and just live with.

### Why does the app need permission for my Mic and Device storage?
- Mic.
  - In order to use the built in recording feature that you can enable as you please to record what your singing, the app needs permission to use your mic. 
- Storage
  - Bookmarking and History is saved with external files, this needs permission to read and write data from your storage.
- Please view our [Privacy Policy](https://hutterite-bookshelf.flycricket.io/privacy.html) if you have further concerns.

### Have further questions?
Contact me either by Opening an issue on this repository, or emailing me at jaredgrozz@gmail.com.

## Technical Information
### Development tools
The app is developed in the Unity game engine version [2018.3.0f2](https://unity3d.com/get-unity/download/archive) using the C-Sharp (C#) programming language. 
Why I chose a game engine to develop this app is mentioned [here]().
