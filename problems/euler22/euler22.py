#!/usr/bin/python
# Imports #
import sys;
sys.path.insert(0, "../../include/python");
import eulersupport;

# Functions #

#Get the score of the name based on formula:
#Sum of all characters position on the alphabet.
def get_name_score(s):
    s = s.upper(); #Turn the case to uppercase.
    
    v = 0;
    for c in s:
        v += ord(c) - ord('A') + 1;
    return v;

# Problem description:
# Using names.txt a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical 
# value for each name, multiply this value by its alphabetical position in the 
# list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is 
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?
def run():

    #Support will return a file object that is read the lines, but
    #all names is contained into one string so get the index 0 to retrieve this
    #string.
    names = eulersupport.get_input_file().readlines()[0];
    
    #Replace all double quotes and make a list separating the names.
    names = names.replace("\"","").split(",");
    
    names.sort();

    #Total score of all names.
    result = 0;
    
    for i in xrange(len(names)):
        name = names[i];
        #Score of name is multiplied by its position.
        score = get_name_score(name * (i + 1));
        result += score;

    #Print the result.
    eulersupport.write_output(result); 
     

def run_full():
    eulersupport.name = "euler22";
    run();

def run_test():
    eulersupport.name = "euler22-Test";
    eulersupport.write_output("I'd no test :(");

def main():
    run_mode = eulersupport.get_run_mode();
    if(run_mode == eulersupport.kRunModeFull):
        run_full();
    else:
        run_test();

if __name__ == '__main__':
    main();
