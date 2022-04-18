# What we want is a program that picks a random number, then displays that number on an HTML file

import random
import tkinter as tk

champ_array = []
champ = 0

def write_HTML(numb):  # this just writes to the html file so OBS can see it.
    file = open("number.html", "w")
    file.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>Random Number</title>\n\t\t<meta "
               "charset=\"UTF-8\">\n\t\t<meta http-equiv=\"refresh\" content=\"2\">\n\t</head>")
    file.write("\n\t<body style=\"font-size:300%;\">\n\t\t<h1 style=\"color:red;\">")
    file.write(str(numb))
    file.write("</h1>\n\t</body>\n</html")
    file.close()


def random_champ():
    global champ
    champ = random.randint(1, 54)  # a random int between 1-55
    return champ

def do_this():
    global champ, string                                # pull down the champion and
    champ = random_champ()                              # make a new random Champion
    champ_name = read_champ(champ)
    write_HTML(champ_name)                                   # push that to the HTML
    string = "Your random Champion is: " + str(champ_name)   # the rest is updating the window
    label['text'] = string
    label.pack()

def read_champ(num): # reads what champion is what number
    # added a file called 'array.txt' that lists all the champions.
    texts = open("array.txt", "r") # open the file as read only
    while (num != 0):              # go through each line until we hit the line we want
        name = texts.readline()
        num = num-1
    if (name[-1] == "\n"):         # if the line has a break at the end, take it off
        name = name[:-1]
    return name                    # return the name



window = tk.Tk() # makes a window with the size below
window.geometry("300x100")
greeting = tk.Button(text="New Champion!", command=lambda: do_this()) # makes a button, then adds text
label = tk.Label(text="Press the button for a Random Champion")
label.pack() # puts it all together and pops up a window
greeting.pack()
window.mainloop()
