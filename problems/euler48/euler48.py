#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python/");
import eulersupport

# Problem description
# The series, 1^1 + 22 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series,
# 1^1 + 2^2 + 3^3 + ... + 1000^1000.
def run(upperbound):
    number = str(sum(map(pow, xrange(1, upperbound +1), xrange(1, upperbound + 1))));
    result = number[-10:];

    #Report Completion.
    eulersupport.write_output(result);

def run_full():
    eulersupport.name = "euler48";
    run(1000);

def run_test():
    eulersupport.name = "euler48-Test";
    run(10);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
