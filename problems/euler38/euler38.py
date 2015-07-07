#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;

def concatenated_product(a, b):
    con_prod = "";
    for i in xrange(1, b + 1):
        con_prod += str(a * i);

    return con_prod;

# Problem Description:
# Take the number 192 and multiply it by each of 1, 2, and 3:
#   192 x 1 = 192
#   192 x 2 = 384
#   192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by
# 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated
# product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
# concatenated product of an integer with (1,2, ... , n) where n > 1?
def run():
    list_of_pandigitals = [];
    upperbound = 999999 + 1;

    for a in xrange(2, upperbound):
        for b in xrange(2, a):
            #Create a concatenated product of a by (1...n)
            con_prod = concatenated_product(a, b);
            #We reach a number that is bigger than 9 digits.
            #has no meaning to keeping searching because it'll not
            #be a pandigital number.
            if(len(con_prod) > 9): break;


            if(eulermath.is_strictly_pandigital(con_prod, 1, 9)):
                list_of_pandigitals += [con_prod];

    list_of_pandigitals.sort();
    result = list_of_pandigitals[len(list_of_pandigitals)-1];

    #Print the result.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler38";
    run();

def run_test():
    eulersupport.name = "euler38-Test";
    eulersupport.write_output("I'd no test :/");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
