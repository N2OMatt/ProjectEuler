#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

# Problem description.
# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?
def run(upperbound):
    result = eulermath.lcm(xrange(1, upperbound + 1));
    #Report Completion
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler05";
    run(20);

def run_test():
    eulersupport.name = "euler05-Test";
    run(10);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
