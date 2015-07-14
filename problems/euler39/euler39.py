#!/usr/bin/python
import sys;
sys.path.insert(0, "../../include/python");
import eulermath;
import eulersupport;

#Get the list of solutions for a perimeter of right rectangle.
def f(p):
    l = []; #List of solutions.

    for a in range(1, p): #Side 1
        a2 = pow(a,2);

        for b in range(1, a): #Side 2
            b2 = pow(b,2);

            for c in range(1, b): #Side 3
                c2 = pow(c,2);

                #Is right triangle and match the perimeter.
                if(a2 == b2 + c2 and (a + b + c) == p):
                    l += [[a, b, c]];
    return l;


# Problem Description:
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#     {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p <= 1000, is the number of solutions maximised?
def run(upperbound):
    l = [];
    for i in range(1, upperbound + 1):
        list_of_results = f(i); #Get the results for the i.

        if(len(list_of_results) != 0):
            print i, list_of_results;
            l += [[len(list_of_results), i]];

    l.sort();

    #Print the result.
    eulersupport.write_output(l[-1]);


def run_full():
    eulersupport.name = "euler39";
    run(1000);

def run_test():
    eulersupport.name = "euler39-Test";
    run(120);

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
