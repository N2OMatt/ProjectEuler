#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import math;

# Problem Description:
# The first known prime found to exceed one million digits was discovered 
# in 1999, and is a Mersenne prime of the form 2^(6972593)-1; it contains 
# exactly 2,098,960 digits. Subsequently other Mersenne primes, of the 
# form 2^(p)-1, have been found which contain more digits.
# However, in 2004 there was found a massive non-Mersenne prime which 
# contains 2,357,207 digits: 28433x2^(7830457)+1.
# Find the last ten digits of this prime number.
def run():
    prime = (28433) * (2**7830457) + 1
    #Extract the last 10 digits of the number.
    prime_str = str(prime);
    last_ten  = prime_str[len(prime_str)-10 : len(prime_str)];
    
    #Report Completion.
    eulersupport.write_output(last_ten);

def run_full():
    eulersupport.name = "euler97";
    run();
def run_test():
    eulersupport.name = "euler97-Test";

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
