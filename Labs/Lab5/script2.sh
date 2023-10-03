#!/bin/bash

# Define the three strings
string1="This is a string"
string2="Hello"
string3="Strings are very cool"

# Get the lengths of the strings
length1=${#string1}
length2=${#string2}
length3=${#string3}

# Initialize variables to track the longest string and its number
longest=""
number=""

# Compare the lengths of the strings
if [ $length1 -gt $length2 ] && [ $length1 -gt $length3 ]; then
    longest="$string1"
    number="1"
elif [ $length2 -gt $length1 ] && [ $length2 -gt $length3 ]; then
    longest="$string2"
    number="2"
else
    longest="$string3"
    number="3"
fi

# Print the result
echo "The longest string is string $number: '$longest'"