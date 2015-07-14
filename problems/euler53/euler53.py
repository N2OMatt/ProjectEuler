#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;
import math;

#Problem Description:
# There are exactly ten ways of selecting three from five, 12345:
#   123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5C3 = 10.
# In general,
#     nCr = n! / (r!(n-r)!) where r M= n, n! = n*(n-1)*...*3*2*1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100,
# are greater than one-million?
def nCr(n, r):
    f = math.factorial(n) / ((math.factorial(r) * math.factorial(n-r)));
    return f;

def run():
    count = 0;
    for n in xrange(1, 100 + 1):
        for r in range(1, n+1):
            a = nCr(n,r);
            if(a > 1000000):
                count += 1;

    #Print the result.
    eulersupport.write_output(count);


def run_full():
    eulersupport.name = "euler53";
    run();

def run_test():
    eulersupport.name = "euler53-Test";
    eulersupport.write_output("I'd no test :/");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();


