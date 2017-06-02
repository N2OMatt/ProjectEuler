#!/usr/bin/python
f1=1;
f2=1;
check_set = set(["1","2","3","4","5","6","7","8","9"]);
index = 2;

def next_fib():
    global f1;
    global f2;
    global index;
    result = f1 + f2;
    f1 = f2;
    f2 = result;

    index += 1;
    return result;


def is_pandigital(str_n):
    if(len(str_n) < 9):
        return False;

    set_n = set();
    for c in str_n:
        set_n.add(c);

    return len(set_n) == 9 and set_n == check_set;

def get_last_digits(str_n):
    return str_n[-9::];

def get_first_digits(str_n):
    return str_n[0:9];

while(True):
    curr_fib     = next_fib();
    str_curr_fib = str(curr_fib);

    if(len(str_curr_fib) < 20):
        continue;

    f_digits = get_first_digits(str_curr_fib);
    l_digits = get_last_digits (str_curr_fib);

    f_pandigital = is_pandigital(f_digits);
    l_pandigital = is_pandigital(l_digits);

    if(f_pandigital):
        print "Front pandigital :", index, "digits count:", len(str_curr_fib);
    if(l_pandigital):
        print "Last pandigital :", index, "digits count:", len(str_curr_fib)

    if(f_pandigital and l_pandigital):
        print "FRONT LAST pandigital :", index, "digits count:", len(str_curr_fib)
        raw_input();
