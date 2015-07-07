#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

# Functions #

def run(upperbound):
    size  = 0; #How many digits the element has.
    index = 0; #Index of the target number in the fibonacci sequence.

    for n in eulermath.fibonacci(1, 1):
        size   = len(str(n));  
        index += 1;

        if(size == upperbound):
            break;

    #Report completion.
    eulersupport.write_output(index);
    

def run_full():
    eulersupport.name = "euler25";
    run(1000);

def run_test():
    eulersupport.name = "euler25-Test";
    run(3);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
