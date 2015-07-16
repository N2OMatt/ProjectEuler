#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import math;

# Problem Description:
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what 
# is the maximum digital sum?
def run():
    maximum = 0;
    for a in xrange(1, 100):
        for b in xrange(1, 100):
            print a, b;
            curr_sum = sum(map(int, str(pow(a,b))));        
            if(curr_sum > maximum):
                maximum = curr_sum;
    
    #Report Completion.
    eulersupport.write_output(maximum);

def run_full():
    eulersupport.name = "euler56";
    run();
def run_test():
    eulersupport.name = "euler56-Test";

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
