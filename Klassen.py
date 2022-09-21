#Klassen

'''Schreiben Sie eine Klasse Person, die die Attribute name und standort hat.'''

'''Fügen Sie eine Methode gehezu hinzu, die einen neuen standort setzt.'''

class Person:

    def __init__(self, name, standort):
        self.name = name
        self.standort = standort
        
    def gehezu(self, standort):
        self.standort = standort    

    def getStandort(self):
        return self.standort

'''Machen Sie mehrere Instanzen dieser Person und lassen Sie diese Personen zu verschiedenen Standorten gehen.'''

Tom = Person('Tom', 'Halle')
Martyna = Person('Martyna', 'Meißen')
Torben = Person('Torben', 'Leipzig')

Tom.gehezu('Berlin')
print(Tom.getStandort())

'''Schreiben Sie eine Klasse EingeschraenktePerson, die von Person erbt.'''

'''Überschreiben Sie in der Klasse EingeschraenktePerson die Methode gehezu und verbieten Sie der Person zu bestimmten Ort zu gehen. So können Sie z.B. auf dem Bildschirm 
Der Zugang zu Ort xxx ist verboten. ausgeben und behalten Sie den alten Ort bei, wenn der Zielort in der Liste Ihrer verbotenen Orte ist.'''

class EingeschraenktePerson(Person):

    excluded_locations = ['Berufsakademie', 'Puff', 'Peißen']

    def __init__(self, name, standort):
        self.name = name
        self.standort = standort
        
    def gehezu(self, standort):
        if standort in self.excluded_locations:
            print(' Der Standort ist verboten')
        else:    
            self.standort = standort

    def __rshift__(self, standort):
        self.gehezu(standort)

Tommyboy = EingeschraenktePerson('Tommyboy', 'Halle')
Tommyboy.gehezu('Puff')


'''Überladen Sie den Operator >> (Hinweis: Nutzen Sie die spezielle Methode __rshift__) mit der gleichen Funktionalität wie gehezu.'''

Tommyboy >> 'Amsterdam'
print(Tommyboy.getStandort())