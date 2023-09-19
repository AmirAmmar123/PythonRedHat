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
   
    def __lt__(self, other):
        return len(self.members) < len(other.members)
    def __bt__(self, other):
        return len(self.members) > len(other.members)