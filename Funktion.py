# Funktionen

'''Schreiben Sie eine Funktion, die die Zahlen von 0 bis 9 mit print() ausgib'''
'''
def limit10():
    print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

limit10()

Schreiben Sie eine Funktion, die das Doppelte einer Zahl zurück gibt

x = input('Bitte eine Zahl eingeben')
z = int(x)

def doppelt(z):
    return (z * 2)

print(doppelt(z))'''

'''Schreiben Sie eine Funktion, die zwei Strings zusammenfügt (konkateniert) und übergeben Sie dieser Funktion
Schlüsselwort-Argumente in unterschiedlichen Reihenfolgen.
'''

x = 'Tom'
y= ' stinkt'

def addstr(x, y):
    dic = {x : y}
    return dic

print(addstr(x,y))

'''Schreiben Sie eine Funktion, die das arithmetische Mittel (Summe geteilt durch die Anzahl) von drei ihr als Argumente übergebenen Zahlen berechnet.'''



def arith(a, b, c):
    print((a + b + c) / 3)

arith(3, 5, 4)


'''Nutzen Sie einen voreingestellten Parameter für die Funktion aus Übung 4, so dass diese auch mit zwei Argumenten
aufrufbar ist. Achtung: Die Summe der Argumente muss je nach Fall durch zwei oder drei geteilt werden. Ein sinnvoller Vorgabewert könnte None sein, da dieser sich eindeutig mit var_name is None von Zahlen unterscheiden
lässt.
'''



def arithm(a, b, c):
    if c is None:
        print((a + b) / 2)

    else:
         print((a + b + c) / 3)
        
    
arithm(3, 4, None)

