## WIP Scraper.

Creates files from intranet, both main file and and working file. Currently only considers the most generic tasks and thus will not work sometimes.
Currently does not get content from website automatically, you have to download it manually.

## How to use it
- Right click intranet page, click 'save as' and save it as 'test.txt'. 
- Drag file to same location as scraper.py.
- Run scraper.py

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

## Still haven't managed to:
- If for some reason you exec the script from /usr/bin it doesnt work for filenames with lists?
- Consider exceptions
- Add usage for C files too
- Check if files already exist so as to not overwrite them
- Ask for confirmation before making main files (per Mateo's request)
- Confirm prototype before copying it to file (check if text = "Prototype: " basically)
- if multiple filenames, assume first?
- if directory, create directory?

## Probably easy to do but not done yet:
- Clean up code some more
- Remove spaghetti code
- Add sauce to spaghetti code
- Apologize in terminal instead of in prototype area on failure
- make it not spam the terminal if it fails several times (for example, a lot of tasks that do not utilize prototypes)
