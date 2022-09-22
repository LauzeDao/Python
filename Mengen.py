# Mengen

'''Definieren Sie zwei Mengen mit Namen von Personen, sodass zwei Namen sowohl in der einen als auch der anderen
Menge vorkommen. Zum Beispiel könnten Sie eine Menge von Personen, die mit den ÖPNV (Bus, Bahn etc.) und
eine Gruppe, die mit Fahrrad zu Arbeit fahren erstellen. Dabei sollten einige Personen nur mit ÖPNV, einige nur mit
dem Fahrrad und einige manchmal mit dem und manchmal mit dem anderen Verkehrsmittel fahren.
Prüfen sie ob bestimmte Namen in den Mengen vorkommen.
Bilden Sie
• Schnittmenge
• Differenz
• Vereinigung
der beiden Mengen.'''

s1 = set(['Tom', 'Martyna', 'Torben', 'Laurence'])
s2 = set(['Thuerkow', 'Timbuktu', 'Martyna', 'Torben'])

#Schnittmenge
print(s1.intersection(s2))

#Differenz
print(s1 - s2)
print(s2 - s1)

#Vereinigung
print(s1.union(s2))


'''Prüfen Sie ob eine zweite Menge mit Namen eine Untermenge Ihrer Menge aus Übung 1 ist.'''

s3 = set([1, 2, 3, 4, 5, 6, 7])
s4 = set([9, 19, 29, 39 , 43])

print(s3.issubset(set(range(10))))

print(s4.issubset(s3))


'''Definieren Sie eine Menge, die ihrerseits wiederum aus Mengen von Namen besteht. Definieren Sie eine zweite
Menge, die eine Schnittmenge mit dieser Menge hat.
'''
#s5= s1.union(s2)
s5 = set([s1, s2])
s6 = (['Paul', 'Rosi'])


print(s5.intersection(s6))
