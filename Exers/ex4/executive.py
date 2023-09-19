
from worker import Worker

class Executive(Worker):
    def __init__(self, name, salary, years):
        super().__init__(name,salary, years)
    
    
    def pension(self):
        return self.years * self.salary * 0.3 
        