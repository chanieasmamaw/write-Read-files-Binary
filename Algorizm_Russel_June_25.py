
import math
from itertools import permutations
from collections import Counter
#+++++++++++++++++++++++++++++++++Q1++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Q1. A function that findes the LCM of two numbers
def is_divisors(num):  # To find the LCM, we first need to compute the GCD using the Euclidean algorithm.
	divisors = []
	for i in range(1, num + 1):
		if num % i == 0:
			divisors.append(i)
	return divisors

def is_least_common_multiplayer(num1, num2):
	# Generate divisors for num1 and num2
	num1_divisors =  is_divisors(num1)
	num2_divisors = is_divisors(num2)
	
	# Print the lists of divisors
	print(f"Divisors of {num1}: {num1_divisors}")
	print(f"Divisors of {num2}: {num2_divisors}")
	
	# Calculate LCM using the gcd function from the math module
	lcm = abs(num1 * num2) // math.gcd(num1, num2)
	
	print(f"Least common multiple (LCM) of {num1} and {num2}: {lcm}")
	return lcm

is_least_common_multiplayer(50, 100)
#+++++++++++++++++++++++++++++++++Q2++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# A function that gets str1, str2(strings) and check if srt1 is a string of permutation of str2.
#Check if the lengths of the two strings are the same. If not, they cannot be permutations of each other.
str1 = 'usa'             # False since len(srt1) != len(str2)
str2 = 'asua'
#str1 = 'usa'
#str2 = 'asu'            # is True
def is_permutation(str1, str2):
	if len(str1) == len(str2):
		return True
	return Counter(str1) == Counter(str2)
print(f"Is '{str1}' a permutation of '{str2}'? ")
print(is_permutation(str1, str2))

#+++++++++++++++++++++++++++++++++Q3++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Q3. A function that checks if a number (integer) is a palindrome one (e.g 3223)

def is_num_palindrome(num):
	num_str = str(num)
	
	# Check if the string is equal to its reverse
	if num_str == num_str[::-1]:
		return "num is palindrome"
	else:
		return 'num is not palindrome'
print(is_num_palindrome(int(input("Enter number: "))))
#+++++++++++++++++++++++++++++++++Q3++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



