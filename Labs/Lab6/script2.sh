#!/bin/bash

# Initialize counter variable
counter=0

# Initialize quote variable
quote="This script will run again"

until [ "$counter" -ge 10 ]; do

    # Print the current quote
    echo "$quote"
    
    quote="$quote and again"
   
    counter=$((counter + 1))
done

# Print "Until it is done"
echo "Until it is done"