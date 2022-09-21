#Ausnahmen und Fehlerbehandlung

'''Lösen Sie einen AttributeError aus, indem Sie ein nicht definiertes Attribute eines Objektes zugreifen. (Hinweis: myobject.attribute)
'''

class MyException(Exception):
    pass

Exc = MyException()

'''Fangen Sie diesen Fehler ab und geben Sie eine Nachricht aus, dass das Attribut nicht definiert ist.'''

try:
    Exc.attribute

except AttributeError:
    print('Das Attribut ist nicht definiert')

    '''Gben Sie Sie auf dem Bildschirm Fertig! aus, unabhängig davon ob der AttributeError auftritt oder nicht'''
finally:
    print('Fertig !')



'''Legen Sie eine Liste mit fünf Elementen an. Greifen Sie auf das achte Element zu. Fangen Sie diesen Fehler ab und
geben Sie eine entsprechende Nachricht auf dem Bildschirm aus.'''


liste = list([1, 2, 3, 4, 5])

try:
    liste[8]

except Exception as err:
    print(f'Fehlermeldung: {err}')

'''Schreiben Sie eine Funktion, die als Parameter ein Dictionary, einen Schlüssel und einen Vorgabewert (default) hat.
Implementieren Sie mit Hilfe von try und except mit dieser Funktion das Verhalten der Methode get eines
Dictionarys.
'''

d = {'Eins': 1,'Zwei': 2,'Drei': 3,'Vier': 4,'Fuenf': 5}

def function(d, key, default):
    try:
        default = d[key]
    
    except KeyError:
        print('Error')
    
    finally:
        return default


print(d.get('Eins'))

