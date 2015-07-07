#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

# Functions #
# Returns the next term in the Fibonacci sequence.
    
# Problem description:    
# Problem description:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def run(upperbound):    
    result = -1;
    factors = eulermath.prime_factors(upperbound);
    for factor in factors:
        if(factor[0] > result):
            result = factor[0];
     
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler03";
    run(600851475143);

def run_test():        
    eulersupport.name = "euler03-Test";
    run(13195);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();