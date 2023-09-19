#!/usr/bin/env python3

class Worker:
    def __init__(self, worker_name, salary, years):
        self.worker_name = worker_name  # Rename the instance variable
        self.salary = salary
        self.years = years

    @property
    def name(self):
        return self.worker_name  # Return the renamed instance variable

    def pension(self):
        return self.years * self.salary * 0.1
