#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;


# Functions #
# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?
def run():
    upper_bound = 10000;     
    count       = 0;    
    for i in xrange(1, upper_bound):
        for exp in xrange(1, upper_bound):
            n      = i ** exp;
            digits = len(str(n));
            print "exp:    " + str(exp);
            print "digits: " + str(digits);
        
            if(digits == exp):
                print str(i) + "**" + str(exp) + " = " + str(n);
                count += 1;        
            elif(digits > exp):
                break;

    #Report Completion.
    eulersupport.write_output(count);

def run_full():
    eulersupport.name = "euler63";
    run();

def run_test():
    eulersupport.name = "euler63-Test";
    eulersupport.write_output("I'd not test");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
