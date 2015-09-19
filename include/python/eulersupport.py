#!/usr/bin/python

# Imports #
import os;
import os.path;
import sys;
import getopt;

# Constants #
#Run mode.
kRunModeTest = "test";
kRunModeFull = "full";
#File paths.
_kInputPath = "../../inputs";
_kOutputPath = "../../outputs";

# Vars #
name = "";

# Functions #
def get_input_file():
    path = os.path.join(_kInputPath, name + "_input.txt");
    return file(path);

def get_run_mode():
    #Get the command line options.
    options = getopt.gnu_getopt(sys.argv[1:], "", [kRunModeTest, kRunModeFull]);

    #Parse the options.
    for key, value in options[0]:
        key = key.lstrip("-");

        if  (key == kRunModeTest): return kRunModeTest;
        elif(key == kRunModeFull): return kRunModeFull;

    #If no flags were given.
    return kRunModeFull;

def log(*msg):
    print name + ":",
    for s in msg:
        print s,;
    print;

def write_output(result):
    completion_string = "%s was completed with result: %s" %(name, str(result));

    #Print to console.
    print completion_string;
    #Print to file.
    f = file(os.path.abspath(os.path.join(_kOutputPath, name + ".txt")), "w");
    f.write(completion_string);
    f.close();

def list_to_str(l, sep = ""):
    return sep.join(map(str, l));
