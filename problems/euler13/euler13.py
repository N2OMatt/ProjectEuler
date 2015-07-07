#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python");
import eulersupport;

# Functions #
def run():
    lines  = eulersupport.get_input_file().readlines();  #List of numbers as Strings.
    m      = map(int, lines); #Map the numbers into ints.
    nstr   = str(sum(m));     #Sum them and transform it into a string.
    snstr  = nstr[:10];       #Get the first 10 digits.
    
    #Report completion.
    eulersupport.write_output(snstr);
    
def run_full():
    eulersupport.name = "euler13";
    run();

def run_test():
    eulersupport.name = "euler13-Test";
    eulersupport.write_output("I'd no test :(");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
