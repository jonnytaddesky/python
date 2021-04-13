class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def first_name(self):
        return self.firstname.title()

    def last_name(self):
        return self.lastname.title()

    def full_name(self):
        return self.firstname.title() + ' ' + self.lastname.title()

    def initials(self):
        return self.firstname[0].upper() + '.' + self.lastname[0].upper()

a1 = Name('JOHN', 'SMITH')
print(a1.first_name())
print(a1.last_name())
print(a1.full_name())
print(a1.initials())

        
    

