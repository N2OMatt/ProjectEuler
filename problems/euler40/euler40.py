#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;

# Problem Description:
# An irrational decimal fraction is created by concatenating the positive
# integers:
#     0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the
# following expression.
#     d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
def run():
    m = map(str, range(1, 1000001)); #Create the fraction.
    s = str().join(m);               #Turn it into one string.

    prod = 1;
    for pwr in xrange(0,7):       #iterate for the power
        index = pow(10, pwr);     #Calculate the index.
        digit = int(s[index -1]); #Get the digit.
        print index, digit
        prod *= digit ;

    #Print the result.
    eulersupport.write_output(prod);

def run_full():
    eulersupport.name = "euler40";
    run();

def run_test():
    eulersupport.name = "euler40-Test";
    run();

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
