#Ein- und Ausgabe

'''Schreiben Sie ein Programm, dass Sie zur Eingabe Ihres Namens auffordert und diesen am Bildschirm wieder ausgibt.'''

'''Modifizieren Sie das Programm so, dass die Abfrage so lange wiederholt wird, bis mit dem Wort end die Ausführung
des Programms beendet wird.'''

'''
eingabe = input("geben Sie Ihren Namen ein: ")

while eingabe != "end":
    print(eingabe)'''


'''Erzeugen Sie mit Python eine neue Textdatei und schreiben Sie die Zahlen von 1 bis 10, eine Zahl pro Zeile, hinein.'''
'''
with open("test.txt", "a+") as fobj:
    fobj.write('1\n')
    fobj.write('2\n')
    fobj.write('3\n')
    fobj.write('4\n')
    fobj.write('5\n')
    fobj.write('6\n')
    fobj.write('7\n')
    fobj.write('8\n')
    fobj.write('9\n')
    fobj.write('10\n')'''


'''Lesen Sie die gerade erzeugte Datei
(a) in einen String und
(b) in eine Liste.'''

with open('test.txt', "r") as fobj:
    data = fobj.read()
    data = fobj.readlines()

print(data)


'''Verwenden SIe das Modul pickle um eine Liste [1, 2, 3] in eine Datei zu speichern und lesen Sie diese wieder
ein.
'''

import pickle

data = ['1', '2', '3']

with open('data.txt', 'wb') as fobj:
    pickle.dump(data, fobj)

with open('data.txt', 'rb') as fobj:
    loaded_data = pickle.load(fobj)

print(loaded_data)



