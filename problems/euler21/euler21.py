#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python");
import eulersupport;
import eulermath;

# Functions #

# Problem Description:
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
# which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 
#     1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 
#     1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
def run(upperbound):
    s = 0;  #Sum of all amicable numbers.
    for i in xrange(1, upperbound +1):
        # print i;
        if(eulermath.is_amicable(i)):
            eulersupport.log(i, "is amicable.");
            s += i;
    
    #Report completion.
    eulersupport.write_output(s);
    

def run_full():
    eulersupport.name = "euler21";
    run(10000);

def run_test():
    eulersupport.name = "euler21";
    # eulersupport.write_output("I'd no test :(");
    eulermath.is_amicable(220);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
