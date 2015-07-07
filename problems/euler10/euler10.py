#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

# Functions #
# Problem description:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
def run(upperbound):
    helper = eulermath.PrimesHelper();
    print "Starting find primes...";
    helper.find_all_primes_up_to_n(upperbound);
    print "Find primes done."
    result = sum(helper.get_primes());
    
    #Report completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler10";
    run(2 * 10**6);

def run_test():
    eulersupport.name = "euler10-Test";
    run(10);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
