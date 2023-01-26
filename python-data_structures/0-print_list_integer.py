#!/usr/bin/python3
if __name__ == "__main__":

    def print_list_integer(my_list=[]):
        """prints all integers of a list.
        """
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
