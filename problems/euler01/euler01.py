#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;

# Functions #
# Problem description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def run(upperbound):
    result  = 0;    #Sum of all values evenly divisible by 5 and 3.
    for i in range(1, upperbound):
        #Is evenly divisible by the two numbers?
        if((i % 3 == 0) or (i % 5 == 0)):
            result += i;

    #Report Completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler01";
    run(1000);

def run_test():
    eulersupport.name = "euler01-Test";
    run(10);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
