#!/usr/bin/python
import itertools;

def catesian_product(somelists):
    elements = [];
    for element in itertools.product(*somelists):
        elements.append("".join(element));
    return elements;

def f(digits):
    ##
    lists       = [map(str, xrange(1, 10))];
    lists_count = int(round((digits / 2.0))) -1;

    for i in xrange(lists_count):
        lists.append(map(str, xrange(0, 10)));

    result = catesian_product(lists);

    if(lists_count % 2 == 0):
        print "interio";
    else:
        print "half";

    print result[0];

    # print result;
    return len(result);

print f(3);
