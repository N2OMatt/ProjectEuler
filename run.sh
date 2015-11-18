#!/bin/bash

################################################################################
## Vars                                                                       ##
################################################################################
PROBLEMS_DIR=./problems

PROBLEM_NAME=$1;
PROBLEM_DIR=$PROBLEMS_DIR/$PROBLEM_NAME

################################################################################
## Functions                                                                  ##
################################################################################
run_python()
{
    #Python scripts must be run locally.
    cd $PROBLEM_DIR;
    ./$PROBLEM_NAME.py

    #Go back to our first directory.
    cd - 1> /dev/null
}

run_cpp()
{
    #COWTODO: Implement the C++.
    echo "C++ is not support by now."
}

################################################################################
## Script Initialization                                                      ##
################################################################################

#Check if we have enough args.
if [ -z $PROBLEM_NAME ]; then
    echo "Usage: run [problem-name]"
    exit 1
fi;

#Check if the problem exists.
if [ ! -e $PROBLEM_DIR ]; then
    echo "Invalid problem - [$PROBLEM_DIR] not found"
    exit 1
fi;

#Check the language of the probleam and build it if needed.
LANG_EXT=$(ls -1 $PROBLEM_DIR | cut -d \. -f 2);
#Python
if [ $LANG_EXT == "py" ]; then
    run_python 
fi;
#C++
if [ $LANG_EXT == "cpp" ]; then
    run_cpp
fi;
