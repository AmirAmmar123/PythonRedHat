#!/usr/bin/env python3
from operator import itemgetter, attrgetter
from customer_functions import get_customers as getlist01
from tertiary_sort2 import get_customers as getlist02



"""
    Python provides the operator module as part of the standard library that contains convenience functions to make it easier and faster to do both basic and specialized sorts.

    The operator module has an itemgetter() function and an attrgetter() function that can be used as the value of the key parameter to both the sort() method of a list and the sorted() function.

    The following example uses the operator.itemgetter() and operator.attrgetter() functions to sort customers
"""    


def main():
    nestedlist = getlist01()
    # get items 4, 1 and 0 as the sort keys from the list
    nestedlist.sort(key=itemgetter(4, 1, 0))
    for alist in nestedlist[:3]:
        print(alist)
    print()
    customerlist = getlist02()
    # get the address.state, last_name, and first_name
    # attributes from each Customer object being sorted
    customerlist.sort(key=attrgetter('address.state', 'last_name',
                                     'first_name'))
    for customer in customerlist[:3]:
        print(customer, end=2*"\n")


if __name__ == "__main__":
    main()