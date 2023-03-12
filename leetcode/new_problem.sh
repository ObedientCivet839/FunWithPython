#!/bin/bash
if [ -z "$1" ]; then
    echo "ERROR: Please provide the difficulty of the problem"
    echo "Example usage: ./new_problem easy two-sum"
    echo "Exit."
    exit 1
fi

if [ -z "$2" ]; then
    echo "ERROR: Please provide the name of the problem"
    echo "Example usage: ./new_problem easy two-sum"
    echo "Exit."
    exit 1
fi

arr=("easy" "medium" "hard" "misc")
if [[ " ${arr[@]} " =~ " ${1} " ]]; then
    echo "Creating file for \"$1\"..."
    DIR=$1
    # Get number of files (and remove spaces)
    NUM_FILES=$(ls $DIR | wc -l | sed 's/ //g')
    # Get next index
    NEXT=$(( ${NUM_FILES#0} +1 ))
    # Append prefix, e.g. P1_rotate-list.py
    FILE="P${NEXT}_${2}.py"
    echo "New file: $FILE"
    # Copy template to new file
    cp ./.template.py ./$DIR/$FILE
    echo "Done."
else
    echo "ERROR: Difficulty must be either easy, medium or hard"
    echo "Example usage: ./new_problem easy two-sum"
    echo "Exit."
fi