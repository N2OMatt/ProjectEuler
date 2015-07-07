#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;

# Functions #
#Read the huge number from the input file.
def read_number():
    f = eulersupport.get_input_file();
    #Here the "number" is just a list of strings.
    #So transform it into one string.
    s = "";
    for l in f.readlines():
        s += str(l);
    
    #Replace the new lines.
    s = s.replace("\n", "");
    return s;

def f(digits_count):
    number = read_number(); #Get the number.
    max_prod = 0;           #The greatest product.

    for i in xrange(0, len(number) - digits_count + 1):
        #Get a substring with length equal to number of digits
        #starting from i.
        sub_str = number[i : i + digits_count];
        #Mutiply the numbers.        
        prod = reduce(lambda x, y: int(x) * int(y), sub_str);
        #Check if current product is greater than current max_prod.
        if(prod > max_prod):        
            max_prod = prod;
    
    return max_prod;

# Problem description:
# The four adjacent digits in the 1000-digit number that have the greatest
# product are 9 x 9 x 8 x 9 = 5832.
#     >> NUMBER <<
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?
def run(digits_count):
    result = f(digits_count);
    #Report completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler08";
    run(13);

def run_test():        
    eulersupport.name = "euler08-Test";
    run(4);    

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();