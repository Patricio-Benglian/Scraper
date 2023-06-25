## WIP Scraper.

Creates files from intranet, both main file and and working file. Currently only considers the most generic tasks and thus will not work sometimes.
Currently does not get content from website automatically, you have to download it manually.

## How to use it
- Right click intranet page, click 'save as'. 
- Drag file to same location as scraper.py (or have scraper.py in your /user/local/bin).
- Run scraper.py

## ARGUMENTS
- Do NOT create -main files: <code>-nm</code>
- Overwrite files: <code>-ow</code>

If it fails to grab a prototype, it will apologize.
Any other failures, I'm still not sure what it will do.

### Uses Beautiful Soup for parsing html efficiently. 
Installation: 

`sudo pip3 install beautifulsoup4`

## Progress:
I've managed to:

- Create Working File with prototyp
- Give permissions to files
- Create main file with content
- Check if files already exist so as to not overwrite them
- Optional Main file creation (per Mateo's request)
- Add documentation to file

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
