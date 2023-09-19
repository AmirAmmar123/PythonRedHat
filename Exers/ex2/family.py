from person import Person 

class Family():
    def __init__(self, *args:Person):
        self.members = []
        for person in args:
            self.members.append(person)
    
    def __str__(self):
        if len(self.members) > 0:
            return  "".join(str(person)+'\n' for person in self.members)
        
    def add(self, person:Person):
        self.members.append(person) 