# Generate Chapters From Text Files
Automatically generates a working chapterx.xml file from a text file that you can use within MKVToolNix and sets the chapters language to English.

## How To Use? 
- Have Python installed and added to the PATh
- Place the script `gen-chapters.py` in a folder, and create an empty input.txt file. 
- Copy paste the chapters from the mediainfo into input.txt.
- Run the script using `python gen-chapters.py output.xml input.txt`
- If your chapters mediainfo has chapter names and you want to copy them, you can add the argument `-names` to the end of the command. This will tell the script to copy the chapter names as it is.

### Examples 

Picture 1: Chapters copied from mediainfo into the text file. 
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/KzTDjxt5/inputtxt.png' border='0' alt='inputtxt'/></a>

Picture2: The generated output.xml file in MKVToolNix. 
<a href="https://ibb.co/0YTZ6Ms"><img src="https://i.ibb.co/TP6R78W/mkvtoolnixchapters.png" alt="mkvtoolnixchapters" border="0"></a>

