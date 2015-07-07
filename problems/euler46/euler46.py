#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

def f(n):
    #We treat prime as number that can be written.
    if(eulermath.PrimesHelper().is_prime(n)):
        return True;

    closest_prime  = eulermath.PrimesHelper().find_all_primes_up_to_n(n);
    index_of_prime = eulermath.PrimesHelper().get_index_of_prime(closest_prime);

    #First prime, if we cannot add a sum of prime + 2 * square
    #with this prime (2) we found a number that cannot be written.
    while(closest_prime != 2):
        #Increase the square until the sum be greater than number.
        for i in xrange(1, n):
            current_square = i ** 2;
            s = closest_prime + (2 * current_square);

            #The number of formula p + 2*sq is greater
            #than your target number, go out of square loop.
            #and try to decrease the prime.
            if(s > n): break;

            #We found our number.
            if(s == n):
                print "%d : [ %d + (2 * %d^2) ]" %(n, closest_prime, i);
                return True;

        #Find the previous prime.
        index_of_prime -= 1;
        closest_prime = eulermath.PrimesHelper().get_prime_at_index(index_of_prime);

    return False;

# Functions #
# Problem description:
# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#      9 =  7 + (2 * 1^2)
#     15 =  7 + (2 * 2^2)
#     21 =  3 + (2 * 3^2)
#     25 =  7 + (2 * 3^2)
#     27 = 19 + (2 * 2^2)
#     33 = 31 + (2 * 1^2)
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of
# a prime and twice a square?
def run():
    result = -1;
    for i in eulermath.infinite_range(9, 2):
        if(not f(i)):
            result = i;
            break;

    print result;
    #Report Completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler46";
    run();

def run_test():
    eulersupport.name = "euler46-Test";
    eulersupport.write_output("I'd not test");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
