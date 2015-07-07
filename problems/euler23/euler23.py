#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

kUpperBound = 28123;
# kUpperBound = 100;
# Functions #
abundants_list = [];

def find_all_abundant_numbers():
    #If the sum of the proper divisors of the number
    #is greater than the number add it to the abuntants list.
    global abundants_list;

    for n in xrange(kUpperBound):
        factors = eulermath.proper_factors(n)
        s = sum(factors);    
        if(n < s):
            print "abundant:", n, s;
            abundants_list.append(n);

def find_sum_cannot_be_written():
    #Create a sieve big enough to all numbers up to kUpperbound.
    cbw = [[False] * (kUpperBound + 1)][0];

    #Populate with all possible sums of two abundant numbers.
    for i in abundants_list:
        for j in abundants_list:
            if(i + j > kUpperBound):
                break;
            cbw[i + j] = True;

    #Check if the index of sieve is false, meaning that 
    #number cannot be written down as sum of two abundant numbers.
    #And add to the sum of all numbers that cannot be written.
    s = 0;
    for i in xrange(0, len(cbw)):
        if(not cbw[i]):
            print i, cbw[i];
            s += i;

    return s;

# Problem Description:
# A perfect number is a number for which the sum of its proper divisors is 
# exactly equal to the number. For example, the sum of the proper divisors of 28 
#would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than 
#n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
# number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. However, this upper limit 
# cannot be reduced any further by analysis even though it is known that the 
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of 
# two abundant numbers.
def run():
    #Find all numbers.
    find_all_abundant_numbers();
    
    #Sum of all numbers that cannot be writton.
    result = find_sum_cannot_be_written();
    
    #Report completion.
    eulersupport.write_output(result);


def run_full():
    eulersupport.name = "euler23";
    run();

def run_test():
    eulersupport.name = "euler23-Test";
    eulersupport.write_output("I'd no test :(");


def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
