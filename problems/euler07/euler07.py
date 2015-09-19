#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

# Problem description:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10 001st prime number?
def run(index):
    result = eulermath.PrimesHelper().find_all_primes_up_to_index(index-1);
    #Report completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler07";
    run(10001);

def run_test():
    eulersupport.name = "euler07-Test";
    run(6);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
