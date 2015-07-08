#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python/");
import eulermath;
import eulersupport;


def fl(n):
    digits = list(str(n));
    while(len(digits) > 1):
        digits = digits[1:];
        number = int(eulersupport.list_to_str(digits));
        if(not eulermath.PrimesHelper().is_prime(number)):
            return False;
    return True;

def fr(n):
    digits = list(str(n));
    while(len(digits) > 1):
        digits = digits[:-1:];
        number = int(eulersupport.list_to_str(digits));
        if(not eulermath.PrimesHelper().is_prime(number)):
            return False;
    return True;

# Problem description
# The number 3797 has an interesting property. Being prime itself, it is
# possible to continuously remove digits from left to right, and remain
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
# right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
def run():
    eulermath.PrimesHelper().find_all_primes_up_to_n(7);

    list_of_primes = [];
    while(len(list_of_primes) != 11):
        prime = eulermath.PrimesHelper().find_next_prime();
        if(fr(prime) and fl(prime)):
            list_of_primes.append(prime);
            print list_of_primes;

    result = sum(list_of_primes);
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler37";
    run();

def run_test():
    eulersupport.name = "euler37-Test";
    eulersupport.write_output("i'd no test :x");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
