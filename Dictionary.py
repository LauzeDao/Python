#Dictionary

'''Erzeugen Sie ein Dictionary mit Namen und Telefonnummern.
Greifen Sie auf die Einträge über den Namen zu.
Testen Sie ob bestimmte Namen eingetragen sind.
Listen Sie alle Telefonnummern auf.
Tun Sie das Gleiche für die Namen.'''

Telefonbuch = {'Tom' : 8413908438, 'Martyna' : 934837817, 'Torben' : 873295474128, 'Laurence' : 218397482}

print(Telefonbuch['Tom'])

print('Martyna' in Telefonbuch)

print(Telefonbuch.values())

print(Telefonbuch.keys())

'''Greifen Sie auf nicht existierende Namen in Ihrem Dictionary aus Übung 1 zu ohne einen Fehler auszulösen. Geben
Sie dabei (a) None und (b) die Zahl Null zurück.
Modifizieren Sie die Lösung und fügen Sie diesen Vorgabewert nun auch in das Dictionary ein. Hinweis: Diese Aufgaben lassen sich jeweils mit einem Methodenaufruf des Dictionarys lösen.'''

'''def Zugriff (x):
    if x in Telefonbuch:
        return Telefonbuch[x]
    else:
        return None

print(Zugriff('Torben'))
print(Zugriff('Alex'))'''

name = 'Paul'

print(Telefonbuch.get(name, None))
print(Telefonbuch.get(name, 0))

if name not in Telefonbuch:
    Telefonbuch[name] = '081542069'

print(Telefonbuch)

'''Aktualisieren Sie Ihre Telefonnummern mit einem zweiten Dictionary, das für eine Person im bestehenden “Telefonbuch” eine neue Telefonnummer und einen ganz neuen Eintrag von Name
und Nummer enthält. Nutzen Sie dazu zwei Methoden:
• (a) eine Schleife und ändern Sie einzelne Elemente und
• (b) eine dafür nützliche Methode des Dictionarys.
Hinweis: Um den Effekt der Änderungen zu zeigen sollten Sie Ihr Telefonnummern-Dictionary vorher kopieren und
die Änderungen an der jeweiligen Kopie vornehmen. Es gibt eine Methode zum Kopieren eines Dictionarys.
'''






neue_nummern = {
    'Tom': 4385230,
    'neuer Name': 23784238
}
'''
Telefonbuch.update(neue_nummern)
print(Telefonbuch)'''

for Telefonbuch['Tom'] in neue_nummern.keys():
    Telefonbuch['Tom'] = neue_nummern['Tom']

print(Telefonbuch)    

'''Entfernen Sie Einträge aus Ihrem Telefon-Dictionary für von Ihnen vorgegebene Namen (a) ohne sich die entfernte
Telefonnummer anzeigen zu lassen und (b) mit Anzeige der entfernten Telefonnummer.
Entfernen Sie eine Telefonnummer ohne den Namen oder die Telefonnummer vorzugeben. Lassen Sie sich dabei den
entfernten Namen und die dazu gehörige Telefonnummer anzeigen'''

loeschen = 'Tom'
print(loeschen + ' ' + str(Telefonbuch[loeschen]))

Telefonbuch.pop(loeschen, None)
print(Telefonbuch)

print(Telefonbuch.popitem())
print(Telefonbuch)

'''Vergleichen sie die Geschwindigkeit der Suche in einem Dictionary und in einer Liste (siehe Tipp unten zur Zeitmessung). Bauen Sie dazu eine lange Liste und ein großes Dictionary (mit je 100, 1000, 10 000 oder mehr Elementen).
Platzieren sie das zu suchende Element in die Mitte der Liste. Im Dictionary wird das zu suchende Element als Schlüssel abgelegt. Prüfen Sie ob das Element in der Liste bzw. dem Dictionary enthalten ist. Nutzen Sie dafür die für die
jeweilige Datenstruktur geeignete Methode. Nehmen sie an, dass Sie die Listenposition des zu prüfenden Elements
nicht kennen.'''

import time

dic = {range(0,10000000):range(0,10000000)}
liste = list(range(0,10000000))


start = time.perf_counter_ns()
dic.get(9000000, None)
end = time.perf_counter_ns()
print('Die Zeit für das Dictionary beträgt ' + str((end - start)))


start = time.perf_counter_ns()
liste[8999999]
end = time.perf_counter_ns()
print('Die Zeit für die Liste beträgt ' + str((end - start)))