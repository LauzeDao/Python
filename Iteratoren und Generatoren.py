# Iteratoren und Generatoren

'''Definieren Sie einen Generator mit Hilfe eines Generatorausdrucks, der das Dreifache der Zahlen von 0 bis 20 ausgibt.
'''
'''Modifizieren Ihren Generator aus Übung 1 so, dass dieser nur gerade Zahlen ausgibt. Hinweis: Der Modulo-Operator
% liefert den Rest einer ganzzahligen Division. Mit der Zahl Zwei als Divisor erhalten wir für alle geraden Zahlen
eine Null und für alle ungeraden Zahlen eine Eins:
>>> 10 % 2
0
>>> 9 % 2
1
'''

g = (x * 3 for x in range(20) if not x % 2)

print(list(g))


'''Schreiben Sie eine Generatorfunktion, die beim ersten Aufruf von next() die Zahl 10 und bei allen anderen
Aufrufen von next() die Zahlen 100, 200 … 900 ausgibt'''


def gfunc():
    print(10)
    yield 1
    print(100)
    yield 2
    print(200)
    yield 3
    print(300)
    yield 4
    print(400)
    yield 5
    print(500)
    yield 6
    print(600)
    yield 7
    print(700)
    yield 8
    print(800)
    yield 9
    print(900)
    yield 10

g = gfunc()
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)

