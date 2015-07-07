#!/usr/bin/python
# Imports #
import sys
sys.path.insert(0, "../../include/python/");
import eulersupport;

# Functions #
# Problem description:
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 2^5 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
def run(upperbound):
    for m in xrange(1, 1000):
        for n in xrange(1, m):
            a = 2*m*n;
            b = m**2 - n**2;
            c = m**2 + n**2;
            #Is the triplet the we wants?
            if(a + b + c == upperbound): 
                #Report Completion
                eulersupport.write_output(a * b * c);
                return; #Go out we are done.

def run_full():
    eulersupport.name = "euler09";
    run(1000);

def run_test():
    eulersupport.name = "euler09-Test";
    eulersupport.write_output("I'd no test :(");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();