#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

# Functions #
def f(size):
    moves  = ["d"] * size;
    moves += ["r"] * size;

    count = 0;
    for _ in eulermath.unique_permutations(moves):
        count += 1;

    return count;

# Problem Description:
# Starting in the top left corner of a 2x2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
def run(size):
    result = f(size);
    #Print the result.
    eulersupport.write_output(result);


def run_full():
    eulersupport.name = "euler15";
    run(20);

def run_test():
    eulersupport.name = "euler15-Test";
    # for i in xrange(2, 21):
    #     print i, "------"
    run(2);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
