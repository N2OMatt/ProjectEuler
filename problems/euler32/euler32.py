#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python/");
import eulermath;
import eulersupport;    
    
# Problem description
# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once; for example, the 5-digit number, 15234, 
# is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only 
# include it once in your sum.
def run():
    multiplicand = 1;
    products_set = set();
    while(True):    
        for multiplier in range(1, multiplicand):
            product = multiplicand * multiplier;
            
            #Build the whole number.
            n_concat = str(multiplicand) + str(multiplier) + str(product);
            
            #Check if the number is pandigital.
            if(eulermath.is_strictly_pandigital(n_concat, 1, 9)):
                products_set.add(product);
                print str(multiplicand) + " * " + str(multiplier) + " = " + str(product);
                print products_set;
            
            if(product > 987654321): #Max number that can be pandigital 1, 9
                #Print the result.
                eulersupport.write_output(sum(products_set));
                return;

        multiplicand += 1;

def run_full():
    eulersupport.name = "euler32";
    run();

def run_test():        
    eulersupport.name = "euler32-Test";
    eulersupport.write_output("i'd no test :x");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
