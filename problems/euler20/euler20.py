#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python/");
import eulermath;
import eulersupport;

# Functions #

# Problem Description:
# n! means n x (n - 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
def run(upperbound):
    #calculate the factorial of the number.
    f = eulermath.factorial(upperbound); 
    #First turn the number into a string, next for each char turn it into a 
    #int and return a list of the digits contained at number.
    m = map(int, str(f)); 
    #Sum all digits of number.
    s = sum(m);

    #Report completion.
    eulersupport.write_output(s);

def run_full():
    eulersupport.name = "euler20";
    run(100);

def run_test():
    eulersupport.name = "euler20-Test";
    run(10);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
