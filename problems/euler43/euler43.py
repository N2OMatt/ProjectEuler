#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;

list_primes = [2, 3, 5, 7, 11, 13, 17];

def f(n):
    str_n = str(n);
    for i in range(1, 8):
        substr_n = str_n[i:(3+i)];
        if(int(substr_n) % list_primes[i-1] != 0):
            return False;

    return True;

# Problem Description:
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:
#     d2d3d4  = 406 is divisible by 2
#     d3d4d5  = 063 is divisible by 3
#     d4d5d6  = 635 is divisible by 5
#     d5d6d7  = 357 is divisible by 7
#     d6d7d8  = 572 is divisible by 11
#     d7d8d9  = 728 is divisible by 13
#     d8d9d10 = 289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
def run():
    result = 0;

    for i in eulermath.permutations(list("1234567890")):
        str_i = eulersupport.list_to_str(i);
        int_i = int(str_i);
        if(eulermath.is_strictly_pandigital(int_i, 0, 9) and f(int_i)):
            print str_i;
            result += 1;

    eulersupport.write_output(result);


def run_full():
    eulersupport.name = "euler43";
    run();

def run_test():
    eulersupport.name = "euler43-Test";
    eulersupport.write_output("I'd no test :/");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();

