#Klassen

class Person:

    def __init__(self, name, groesse):
        self.name = name
        self.groesse = groesse
        
    def wachsen(self, cm):
        self.groesse += cm  

    def getGroesse(self):
        return self.groesse



Laurence = Person('Laurence', 176)


Laurence.wachsen(10)
print(Laurence.getGroesse())

