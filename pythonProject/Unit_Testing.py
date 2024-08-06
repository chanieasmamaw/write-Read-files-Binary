def find_min_max(nums):
	"""
	Returns a tuple containing the minimum and maximum numbers from the input list.

	Parameters:
	nums (list): A list of numbers.

	Returns:
	tuple: A tuple containing the minimum and maximum numbers.

	If the list is empty return None.

	If the parameter is wrong datatype, or list has non-numeric elements return False.
	"""
	if not isinstance(nums, list):
		return False  # Return False for wrong datatype
	
	if not nums:
		return None # Return None for empty list
	
	if not all(isinstance(num, (int, float)) for num in nums):
		return True # Return False for non-numeric elements
	
	# Initialize min and max variables with the first element of the list
	minimum = nums[0]
	maximum = nums[0]
	
	# Iterate through the list to find the minimum and maximum numbers
	for num in nums[1:]:
		if num < minimum:
			minimum = num
		elif num > maximum:
			maximum = num
	
	return minimum, maximum



# Example usage:
