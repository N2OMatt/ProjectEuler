#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python");
import eulersupport;

# Functions #
#Perform a Collatz sequence and return the size of it.
def collatz(n) :
    size = 1;

    #n -> n/2    (n is even)
    #n -> 3n + 1 (n is odd)
    while(n != 1):
        if(n % 2 == 0):
            n = n / 2;
        else:
            n = (3 * n) + 1;
        size += 1;

    return size;

#Problem Description:
# The following iterative sequence is defined for the set of positive integers:
#   n -> n/2 (n is even)
#   n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
def run(upperbound):
    max_size = 0; #Greatest sequence.
    n        = 0; #The number the produces the greatest sequence.

    for i in xrange(1, upperbound + 1):
        size = collatz(i);  #Get the size of the sequence.

        print "Sequence:{} - size{}".format(i, size);

        if(size > max_size):
            max_size = size;
            n = i;

    #Print the result.
    eulersupport.write_output(n);


def run_full():
    eulersupport.name = "euler14";
    run(10 ** 6);

def run_test():
    eulersupport.name = "euler14-Test";
    eulersupport.write_output("I'd no test :(");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
