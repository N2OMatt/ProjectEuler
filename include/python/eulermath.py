#!/usr/bin/python

# Imports #
import os;
import os.path;
import sys;
import pdb;
import math;
import itertools;
import operator

def prod(factors):
    return reduce(operator.mul, factors, 1);

################################################################################
## Triangle Functions                                                         ##
################################################################################
#Check if the given sides can form a triangle.
def is_triangle(a, b, c):
    # Rule to check if a,b,c can be form a valid triangle.
    # | b - c | < a < b + c
    # | a - c | < b < a + c
    # | a - b | < c < a + b

    #X minus Y
    BmC = abs(b - c);
    AmC = abs(a - c);
    AmB = abs(a - b);

    #X plus Y
    BpC = b + c;
    ApC = a + c;
    ApB = a + b;

    return ((BmC < a) and (a < BpC)) and ((AmC < b) and (b < ApC)) and ((AmB < c) and (c < ApB));

#Check if the give sides can form a right triangle.
def is_right_triangle(a, b, c):
    if(not is_triangle(a, b, c)):
        return False;

    sides = [a, b, c];
    sides.sort();

    return (sides[2]**2) == (sides[0]**2) + (sides[1]**2);


################################################################################
## GDC / LCM Functions                                                        ##
################################################################################
#Calculate the Greater Common Divisor for any given numbers.
def gdc(*args):
    return _gdc(args, None);

#Check if the Greater Common Divisor for any given numbers is equal to n.
def gdc_is_n(args, n):
    return _gdc(args, n);

def euclidian_gdc(a, b, returnSteps = None):
    steps = 0;
    while(b != 0):
        t = b;
        b = a % b;
        a = t;
        steps += 1;
    if(returnSteps):
        return [a, steps];
    return a;

#Calculate the Least Common Multiple for any given numbers.
def fast_lcm(*args):
    a = args[0];
    b = args[1];

    return (a / euclidian_gdc(a, b)) * b;

def lcm(args):
    divisors = [];

    index = 0;
    while(True):
        curr_prime = PrimesHelper().get_prime_at_index(index);

        divided = False;
        for i in xrange(len(args)):
            if(args[i] % curr_prime == 0):
                args[i] /= curr_prime;
                divided = True;

        if(divided):
            divisors.append(curr_prime);
        else:
            index += 1;

        if(set(args) == set([1])):
            break;

    return reduce(lambda x, y: x * y, divisors, 1);

#Private function that calculate the GDC of given numbers.
def _gdc(args, target_gdc):
    #Iterate for all numbers up to the greater number
    #in the arguments.
    result = 0;
    for i in xrange(1, min(args) + 1):
        #Since the arguments can be with any lenght
        #check if all numbers in the arguments can be divided
        #by the current number (i).
        divide_all = True;
        for n in args:
            if(n % i != 0): #Not a proper divisor, go out possible try another.
                divide_all = False;
                break;

        #Ok all numbers in the arguments can be divided, the current number
        #is the current greater common.
        if(divide_all):
            if(target_gdc != None and i > target_gdc):
                    return False;
            result = i;

    if(target_gdc != None and result == target_gdc):
        return True;

    return result;


################################################################################
## Fibonnaci Functions                                                        ##
################################################################################
#Generate a sequence of fibonacci numbers.
def fibonacci(f1, f2):
    a = f1;
    b = f2;
    yield f1;
    yield f2;

    while(True):
        c = a + b;
        yield c;

        a = b;
        b = c;


################################################################################
## Factors Functions                                                          ##
################################################################################
def factors(n):
    #If n is 0 or 1 just return the number.
    if(n == 0 or n == 1):
        yield n;

    #Vars.
    i     = int(n % 2 == 0) + 1;
    step  = 2; #Step 1 by 1 if even. 2 by 2 if odd.

    while(i <= int(n / 2)):
        if(n % i == 0):
            yield i;

        i += step;

    yield n;

#Return a list of all evenly divisors of a given number.
def factors_list(n):
    return list(factors(n));

def factors_count(n):
    pfactors = prime_factors(n);
    l = [];
    for pf in pfactors:
      l.append(pf[1] + 1);

    return reduce(lambda x, y: x * y, l, 1);

def proper_factors(n):
    return factors(n)[:-1];

def prime_factors(n):
    if(n == 0 or n == 1):
        return [];

    fac_l = [];
    ph      = PrimesHelper();
    i       = 0;

    while(n > 1):
        curr_prime = ph.get_prime_at_index(i);
        if(n % curr_prime == 0):
            n /= curr_prime;
            fac_l.append(curr_prime);
        else:
            i += 1;

    factors = [];
    for i in set(fac_l):
        factors.append([i, fac_l.count(i)]);

    return factors;


################################################################################
## Other Functions                                                            ##
################################################################################
#Calculate a n!
def factorial(n):
    return reduce(lambda x, y: x * y, xrange(1, n+1), 1);

#Check if n is an Amicable number. If (d(a) = b) && (d(b) = a) && (a != b);
def is_amicable(a):
    b = sum(proper_factors(a));
    if(a != b and sum(proper_factors(b)) == a):
        return True;
    return False;

def permutations(seq):
    for p in itertools.permutations(seq):
        yield p;
def all_permutations(seq):
    l = [];
    for p in permutations(seq):
        l.append(p);
    return l;
def permutation_at_index(seq, index):
    i = 0;
    for p in permutations(seq):
        if(i == index):
            return p;
        i += 1;
def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in itertools.permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

def rotation(seq):
    original_seq = seq;
    while(True):
        elem = seq[0];
        seq  = seq[1:];
        seq.append(elem);
        yield seq;
        if(seq == original_seq):
            return;
def all_rotations(seq):
    return list(rotation(seq));

def infinite_range(start, inc = 1):
    i = start;
    while(True):
        yield i;
        i += inc;


################################################################################
## Digits Functions                                                           ##
################################################################################
def list_of_digits(n):
    return map(int, str(n));

def sum_of_digits(n):
    return sum(list_of_digits(n));

def is_palindrome(n):
    return str(n) == str(n)[::-1];

def palindromes(start, end = None):
    while(not is_palindrome(start)):
        start += 1;

    while(end == None or start < end):
        while(not is_palindrome(start)):
            start += 1;
        yield start;
        start += 1;

def palindromes_fast(start, end=None):
    pass;

def is_pandigital(n, start = 0, end = 9):
    str_n = str(n);
    for i in xrange(start, end + 1):
        if(str_n.count(str(i)) != 1):
            return False;
    return True;

def is_strictly_pandigital(n, start = 0, end = 9):
    if(len(str(n)) != ((end - start) + 1)):
        return False;
    return is_pandigital(n, start, end);


################################################################################
## Progressions Functions                                                     ##
################################################################################
def triangle_number(n):
    return (n*(n + 1)) / 2;

def pentagonal_number(n):
    return (n * (3*n -1)) / 2;

def is_pentagonal_number(n):
    x = (math.sqrt(24*n + 1) + 1) / 6;
    if(x == int(x) and x > 0):
        return True;
    return False;

def index_of_pentagonal_number(n):
    x = (math.sqrt(24*n + 1) + 1) / 6;
    if(x == int(x) and x > 0):
        return int(x);
    return -1;


################################################################################
# Prime Functions                                                             ##
################################################################################
class PrimesHelper(object):
    ## iVars ##
    _primes = [2,3];

    ## Singleton ##
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PrimesHelper, cls).__new__(cls)
        return cls.instance;

    ## CTOR ##
    def __init__(self):
        super(PrimesHelper, self).__init__()

    ## Methods ##
    #Return if a given number is prime or not.
    def is_prime(self, n):
        if(self._primes[-1] < n):
            self.find_all_primes_up_to_n(n);

        return n in self._primes;

    #Return the next prime found.
    def find_next_prime(self):
        n = self._primes[-1] + 2;
        while(True):
            if(self.check_primality(n)):
                self._primes.append(n);
                return n;
            n += 2;

    #Find all primes less or equal than n and
    #return the last one. If the set of primes is
    #already found just return the prime.
    def find_all_primes_up_to_n(self, n):
        #We already have found a prime, just return it.
        if(self._primes[-1] > n):
            return self._primes[-1];

        #Keep searching...
        curr_prime = self._primes[-1];
        while(curr_prime < n):
            curr_prime = self.find_next_prime();

        #We may found a prime greater than N. If is the case
        #remove it. So the greater prime is less or equal N.
        if(self._primes[-1] > n):
            self._primes.pop();

        return self._primes[-1];

    def find_all_primes_up_to_index(self, index):
        while(len(self._primes) - 1 < index):
            self.find_next_prime();
        return self._primes[-1];

    def get_primes(self):
        return self._primes;

    def get_prime_at_index(self, index):
        self.find_all_primes_up_to_index(index);
        return self._primes[index];

    def get_index_of_prime(self, prime):
        #The prime is greater than the last
        #prime found. Search all primes up to the given
        #prime and return its index.
        if(prime > self._primes[-1]):
            self.find_all_primes_up_to_n(prime);

        return self._primes.index(prime);

    def check_primality(self, n):
        #Check most basic cases.
        if(n == 2):
            return True;
        if(n % 2 == 0):
            return False;

        sqrt_n = (n ** 0.5) + 1;  #SQRT(n)

        #Iterate for all known primes.
        for curr_prime in self._primes[1:]:
            #Is a composite number.
            if(n % curr_prime == 0):
                return False;

            #We'd test all primes needed.
            if(curr_prime > sqrt_n):
                return True;

        return True;
