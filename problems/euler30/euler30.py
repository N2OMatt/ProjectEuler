#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport;
import time;


# Problem description:
# Surprisingly there are only three numbers that can be 
# written as the sum of fourth powers of their digits:
#    1634 = 1^4 + 6^4 + 3^4 + 4^4
#    8208 = 8^4 + 2^4 + 0^4 + 8^4
#    9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as 
# the sum of fifth powers of their digits.
def f(n, p): 
    strN   = str(n); #Get the string reprentation of the number.
    intMap = map(int, strN); #Get all digits of the number as ints.
    m      = map(pow, intMap, [p]*len(strN)); #Power all digits of the number to n.
    s      = sum(m);  #Sum all the powers of the all digits of the number.
    
    return s == n;

def run(p):
    result 	= 0; 
    index  	= 2;    
    upper_bound = int("9" * (p+1));

    while(index < upper_bound):        
        if(f(index, p)):
            result += index;	                    
        index += 1;

    #Print the result.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler30";
    run(5);

def run_test():        
    eulersupport.name = "euler30-Test";
    run(4);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
