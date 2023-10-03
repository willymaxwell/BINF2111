#!bin/bash


adding_numbers(){
	num1=$1
	num2=$2
	sum=$(($num1+$num2))


	echo "Add $num1 and $num2 together and you get: $sum"

return 0
}

adding_numbers 3 7
adding_numbers 20 30
adding_numbers 50 50
