#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import eulermath;

def run():
    factors_count     = 4;
    consecutive_count = 4;
    consecutive_list  = [];
    result            = None;

    for i in eulermath.infinite_range(0):
        print i;
        factors = eulermath.prime_factors(i);
        
        if(len(factors) == factors_count):
            consecutive_list.append(i);
        else:
            consecutive_list = [];

        if(len(consecutive_list) == consecutive_count):
            result = consecutive_list[0];
            break;

    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler47";
    run();

def run_test():
    eulersupport.name = "euler47-Test";
    eulersupport.write_output("I'd not test");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
