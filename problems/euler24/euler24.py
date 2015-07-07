#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulermath;
import eulersupport;

# Functions #
# Problem description:
# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of
# 0, 1 and 2 are:
#     012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
def run(seq, upperbound):
    print seq, upperbound;
    result = eulermath.permutation_at_index(seq, upperbound);
    result = eulersupport.list_to_str(result);
    #Report Completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler24";
    run(xrange(0, 10), (10 ** 6) -1);

def run_test():
    eulersupport.name = "euler24-Test";
    eulersupport.write_output("I'd no test");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
