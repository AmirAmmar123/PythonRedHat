class Person:
    def __init__(self, name, age, gender ):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return f"name: is {self.name}, age is {self.age}, gender is {self.gender}"
    
