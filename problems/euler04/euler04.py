#!/usr/bin/python

# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;
      
# Problem description:     
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
def run(exp):
    max_value = (10 ** exp) -1;  #Inclusive upper bound of values.
    max_palin = 0;               #Greater palindrome found.
    
    #Search backwards.
    for i in range(max_value, 1, -1):
        for j in range(i, 1, -1):                    
            #The number is palindrome and is greater that 
            #current max palindrome?
            if((i * j) > max_palin and eulermath.is_palindrome(i * j)):
                max_palin = (i * j);

    #Print the result.
    eulersupport.write_output(max_palin);
    
def run_full():
    eulersupport.name = "euler04";
    run(3);

def run_test():        
    eulersupport.name = "euler04-Test";
    run(2);    

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
