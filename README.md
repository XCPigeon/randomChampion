# randomChampion
This program is ment to pick a random champion from the hit game Palidins, then output the result to an HTML file, that is used for OBS streaming

I'm not very clever with installing things, but all you need is the main.py file and run it once.

OBS USE:
To show the "Champion" on OBS, youll need to create a browser source. Choose local file, then select the HTML file that *should* be in the same as the main.py. Make sure to run main.py first to get the HTML file.
After you add the HTML file, run main.py again to choose a new champion. The HTML file will refresh every 2 seconds to show the change. 

HOW IT WORKS:
when you run the python program, it'll thow a new random number into the HTML file. The HTML file is set to refresh every 2 seconds. 

It's not the most elegant solution, but it works kinda sorta. 
