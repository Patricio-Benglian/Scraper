## WIP Scraper.

Creates files from intranet, both main file and and working file. Currently only considers the most generic tasks and thus will not work sometimes.
Currently does not get content from website automatically, you have to download it manually.

## How to use it
- Right click intranet page, click 'save as'. 
- Drag file to same location as scraper.py (or have scraper.py in your /user/local/bin).
- Run scraper.py while in desired directory

## ARGUMENTS
- Do NOT create -main files: <code>-nm</code>
- Overwrite files: <code>-ow</code>

Examples:
- <code>./scraper.py</code> to create all files not already in directory (main and normal)
- <code>./scraper.py -nm</code> to create only the files with no main files
- <code>./scraper.py -ow</code> to overwrite all files (main and normal)
- <code>./scraper.py -ow -nm</code> to overwrite all files without creating main files


If it fails to grab a prototype, it will apologize.
Any other failures, I'm still not sure what it will do.

### Uses Beautiful Soup for parsing html efficiently. 
Installation: 

`sudo pip3 install beautifulsoup4`

## Progress:
I've managed to:

- Create Working File with prototype and documentation
- Create main file with content (most of the time)
- Give permissions to all files
- Check if files already exist so as to not overwrite them
- Optional Main file creation (per Mateo's request)

## Still haven't managed to:
- Consider exceptions
- Add option for C files too
- Confirm prototype before copying it to file (check if text = "Prototype: " basically)
- if multiple filenames, assume first?
- if directory, create directory?
- utilize cookies to get page data without download
- utilize input to get cookie, then overwrite itself to save cookie permanently into script? lol
- create all files in the terminal examples (ex: main file, json file, etc) instead of just the first

## Probably easy to do but not done yet:
- Clean up code some more
- Remove spaghetti code
- Add sauce to spaghetti code
- Apologize in terminal instead of in prototype area on failure
- make it not spam the terminal if it fails several times (for example, a lot of tasks that do not utilize prototypes)
