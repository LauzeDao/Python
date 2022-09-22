#Datei einlesen
# https://www.python-lernen.de/dateien-auslesen.htm

# w für write, a für append, r für read, r+ für lesen und schreiben, b in Binär lesen und schreiben

fobj = open('text.txt', 'r')
print(fobj.read())

fobj.close()
