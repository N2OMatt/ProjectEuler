#!/usr/bin/python
import itertools;

def is_upper(data):
    return all(b >= a for a, b in itertools.izip(data, itertools.islice(data, 1, None)))

def is_lower(data):
        return all(b <= a for a, b in itertools.izip(data, itertools.islice(data, 1, None)))

def is_bouncy(data):
    return not is_upper(data) and not is_lower(data);


bouncy_numbers = 0;
bouncy_ratio   = 0;

i = 1;
while(True):
    if(is_bouncy(str(i))):
        bouncy_numbers += 1;

    bouncy_ratio = bouncy_numbers / float(i);


    print "I       :", i;
    print "Bouncy  :", bouncy_numbers;
    print "!Bouncy :", i - bouncy_numbers;
    print "Ratio   :", bouncy_ratio;
    print;

    if(bouncy_ratio == 0.99):
        raw_input();

    i += 1;
