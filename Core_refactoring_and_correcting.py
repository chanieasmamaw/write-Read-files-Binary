def is_palindrome(number):
	# Convert number to string to easily check palindrome property
	num_str = str(number)
	
	# Compare string with its reverse
	return num_str == num_str[::-1]
# Example usage:
num = 121
if is_palindrome(num):
	print(f"{num} is a palindrome number.")
else:
	print(f"{num} is not a palindrome number.")
	
	
	def find_first_occurence(string1, string2):
		# compare two strings for occurence of first in second
		list_of_given_strings = []
		i = 0
		for letter in string2:
			if string1[i] == string2[i]:
				i += 1
				print(string1[i])
			else:
				string1[i] == string2[i + 1]
				print("second loop")
	
	
	# loop over the second string to find the first
	# return the first index of occurence
	print(find_first_occurence("hello", "hello"))