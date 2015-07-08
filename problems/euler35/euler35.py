#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python/");
import eulermath;
import eulersupport;

# Problem description
# The number, 197, is called a circular prime because all rotations of
# the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100:
#     2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
def run(upperbound):
    list_of_primes = [];

    #Find all the primes.
    eulermath.PrimesHelper().find_all_primes_up_to_n(upperbound);
    for prime in eulermath.PrimesHelper().get_primes():
        digits = list(str(prime));

        #Check if all permutations are prime.
        perms = eulermath.all_rotations(digits);
        perms = [int(eulersupport.list_to_str(perm)) for perm in perms];

        all_perms_are_prime = all(eulermath.PrimesHelper().is_prime(x) for x in perms);
        print prime, "-", perms, all_perms_are_prime;

        #Add to list of primes
        if(all_perms_are_prime):
            list_of_primes.append(prime);

    eulersupport.write_output(len(list_of_primes));

def run_full():
    eulersupport.name = "euler35";
    run(10**6);

def run_test():
    eulersupport.name = "euler35-Test";
    eulersupport.write_output("i'd no test :x");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
