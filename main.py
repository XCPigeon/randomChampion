# What we want is a program that picks a random number, then displays that number on an HTML file

import random
import tkinter as tk

champ = 0

def write_HTML(numb):  # this just writes to the html file so OBS can see it.
    file = open("number.html", "w")
    file.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Random Number</title>\n\t\t<meta "
               "charset=\"UTF-8\">\n\t\t<meta name=\"viewport\" content=\"width=device-width, "
               "initial-scale=1.0\">\n\t\t<meta http-equiv=\"refresh\" content=\"2\">\n\t</head>")
    file.write("\n\t<body style=\"font-size:300%;\">\n\t\t<h1 style=\"color:red;\">")
    file.write(str(numb))
    file.write("</h1>\n\t</body>\n</html")
    file.close()


def random_champ():
    global champ
    champ = random.randint(1, 55)  # a random int between 1-55
    return champ

def do_this(): 
    global champ, string                                # pull down the champion and  
    champ = random_champ()                              # make a new random Champion
    write_HTML(champ)                                   # push that to the HTML
    string = "Your random Champion is: " + str(champ)   # the rest is updating the window
    label['text'] = string
    label.pack()


window = tk.Tk() # makes a window with the size below
window.geometry("300x50")
greeting = tk.Button(text="Hello there!", command=lambda: do_this()) # makes a button, then adds text
label = tk.Label(text="Press the button for a Random Champion")
label.pack() # puts it all together and pops up a window
greeting.pack()
window.mainloop() 
