#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;

# Problem description.
# The sum of the squares of the first ten natural numbers is,
#   12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
def run(upperbound):
    numbers = xrange(1, upperbound + 1); #All numbers up to upperbound.

    sum_of_squares = sum(map(pow, numbers, [2] * (upperbound)));
    square_of_sums = sum(numbers) ** 2;

    result = (square_of_sums - sum_of_squares);

    #Report completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler06";
    run(100);

def run_test():
    eulersupport.name = "euler06-Test";
    run(10);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
