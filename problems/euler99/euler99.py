#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;
import math;

# Problem Description:

def run():
    greater      = -1;
    greater_line = -1;
    line_no      = 0;

    lines = eulersupport.get_input_file().readlines();
    for line in lines:
        l = line.split(",");
        b = int(l[0]);
        e = int(l[1]);
        number = int(b) ** int(e);

        if(number > greater):
            greater      = number;
            greater_line = line_no;
            print greater_line;

        # print line_no;
        line_no += 1;

    #Report Completion.
    eulersupport.write_output("zero based: %d, one based %d" %(greater_line, greater_line +1));

def run_full():
    eulersupport.name = "euler99";
    run();
def run_test():
    eulersupport.name = "euler99-Test";

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
