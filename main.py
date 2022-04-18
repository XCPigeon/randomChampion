# What we want is a program that picks a random number, then displays that number on an HTML file

import random


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
    champ = random.randint(1, 55)  # a random int between 1-55
    return champ


# Let's first pick a random number. 1-55 because there is 55 champions in Paladins
champ = random_champ()
# Now lets put names to number
# TO DO
# Now lets write the number
write_HTML(champ)
