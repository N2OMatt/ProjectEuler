#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import math;

def sq_of_digits(n):
    return int(sum(map(math.pow, map(int, str(n)), [2] * len(str(n)))));

def find_chain(n):
    chain = [n];
    while(True):
        i = chain[len(chain) -1];
        if(i == 89):
            return [89, chain];
        elif(i == 1):
            return [1, chain];
        elif(chain.count(i) > 1):
            return [i, chain];

        chain += [sq_of_digits(i)];

# Problem Description:
# A number chain is created by continuously adding the square of the digits
# in a number to form a new number until it has been seen before.
# For example,
#   44 -> 32 -> 13 -> 10 -> 1 -> 1
#   85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an
# endless loop. What is most amazing is that EVERY starting number will
# eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?
def run(upperbound):
    count_89    = 0;
    count_1     = 0;
    count_other = 0;

    for i in xrange(0, upperbound):
        chain = find_chain(i);

        if  (chain[0] == 89): count_89 += 1;
        elif(chain[0] ==  1): count_1  += 1;

    #Report Completion.
    eulersupport.write_output(count_89);

def run_full():
    eulersupport.name = "euler92";
    run(10 * (10 ** 6));

def run_test():
    eulersupport.name = "euler92-Test";
    run(10 * (10 ** 2));

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
