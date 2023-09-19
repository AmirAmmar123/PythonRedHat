#!/usr/bin/env python3
from worker import Worker
from manager import Manager
from executive import Executive

def main():
    workers = [Manager("Hosen",20000,15),Manager("Waleed", 20000, 3),Manager("Annan", 14000, 3),Executive("Amir",450000, 3)]

    for x  in workers:
        print(x.pension())
    



if __name__ == '__main__':
    main()