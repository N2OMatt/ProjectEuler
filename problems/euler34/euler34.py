#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;

# Problem description:
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
def run():
    index  = 3;
    result = 0;

    while(index < 10 ** 7):
    	list_d            = eulermath.list_of_digits(index);
	list_factorial_d  = map(eulermath.factorial, list_d);
    	sum_of_factorials = sum(list_factorial_d);

	if(sum_of_factorials == index):
	    print index;
	    result += index;

	index += 1;

    # Print the result.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler34";
    run();

def run_test():
    eulersupport.name = "euler34-Test";
    eulersupport.write_output("I'd no test :/");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
