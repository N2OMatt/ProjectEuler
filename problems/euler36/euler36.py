#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;

#Check if n is palindrome at base 2.
def is_palindrome_2(n):
    b = bin(n)[2::];
    return str(b) == str(b)[::-1];

# Problem Description:
# The decimal number, 585 = 1001001001(2) (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are
# palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not
# include leading zeros.)=
def run():
    result = 0;
    for i in range(0, 1000000):
        if(is_palindrome_2(i) and eulermath.is_palindrome(i)):
            print i;
            result += i;

    #Print the result.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler36";
    run();

def run_test():
    eulersupport.name = "euler36-Test";
    eulersupport.write_output("I'd no test :/");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
