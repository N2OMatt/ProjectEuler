#!/usr/bin/python
# coding=utf8
# Imports #
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

##Functions
def countPrimes(a, b):
    count = 0;
    for n in eulermath.infinite_range(0):

        possible_prime = (n * n) + (a * n) + b;
        if(eulermath.PrimesHelper().is_prime(possible_prime)):
            count += 1;
        else:
            return count;
    
# Problem description:
# Euler discovered the remarkable quadratic formula:
#     n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive 
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41
# is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly 
# divisible by 41.
# 
# The incredible formula  n^2 − 79n + 1601 was discovered, which produces 80 
# primes for the consecutive values n = 0 to 79. The product of the 
# coefficients, −79 and 1601, is −126479.
# 
# Considering quadratics of the form:
#     n^2 + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
#     e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.
def run(lowerbound, upperbound):

    result = {"a" : 0,
              "b" : 0,
              "count" : 0};

    #Try all formulas.
    for a in xrange(lowerbound+1, upperbound):
        for b in xrange(lowerbound+1, upperbound):
            count = countPrimes(a, b);
            if(count != 0):
                if(count > result["count"]):
                    result["a"] = a;
                    result["b"] = b;
                    result["count"] = count;
                    print result;

    eulersupport.write_output(result["a"] * result["b"]);
    
def run_full():
    eulersupport.name = "euler27";
    n = 1000;
    run(-n, n);

def run_test():
    eulersupport.name = "euler27-Test";

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
