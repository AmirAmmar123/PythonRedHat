#!/usr/bin/env python3
from person import Person
from family import Family

def main():
    mom = Person("Mom", 45, "F")
    dad = Person("Dad", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")
    myFamily = Family(mom, dad, kid1, kid2)
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)
    print(myFamily)

    myFamily = Family(mom, dad, kid1, kid2)
    smiths = Family(mom, dad, kid1)
    if (myFamily > smiths):
        print("we have more kids than smiths")
    if (myFamily == smiths):
        print("families have same # of kids")
    if (myFamily < smiths):
        print("we have fewer kids than smiths")
if __name__ == "__main__":
    main()
