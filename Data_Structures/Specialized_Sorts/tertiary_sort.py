#!/usr/bin/env python3
from customer_functions import get_customers


def main():
    customer_list = get_customers()
    customer_list.sort(key=lambda x: (x[4], x[1], x[0]))
    for customer in customer_list:
        print(customer)


if __name__ == "__main__":
    main()
    
    """
    
    The second and third lines of the preceding output show how the customers were sorted by their first names because the state and last name were the same for both entries.

    A more object-oriented approach to the previous examples dealing with the customers.txt file, would be to start by defining classes to represent the data as an Address class and a Customer class to represent all the data as objects.

    These two data types are defined in the following module.
    """