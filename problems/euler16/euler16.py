#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport;

# Functions #

#Problem Description.
#2^15 = 32768 and the sum of its digits is 
#3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?
def run(exp):
    st = str(2**exp);   #Raise 2 to exp power and make a string of the number.
    m  = map(int, st);  #Turn digits into integers.
    s  = sum(m);        #Sum them.

    #Report completion.
    eulersupport.write_output(s);

def run_full():
    eulersupport.name = "euler016";
    run(1000);

def run_test():
    eulersupport.name = "euler016-Test";
    run(15);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
