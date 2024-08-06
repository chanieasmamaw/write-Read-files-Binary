def find_min_max(nums):
	"""
    Returns a tuple containing the minimum and maximum numbers from the input list.

    Parameters:
    nums (list): A list of numbers.

    Returns:
    tuple: A tuple containing the minimum and maximum numbers.

    If the list is empty return None.

    If the parameter is wrong datatype, or list has non-numeric elementsreturn False.
    """
    if not isinstance(nums, list):
        return False
    if not nums:
        return None
    if not all(isinstance(num, (int, float)) for num in nums):
        return False
        
        # Initialize min and max variables with the first element of the list
    minimum = nums[0]
    maximum = nums[0]
    
    # Iterate through the list to find the minimum and maximum numbers
    for num in nums[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num


    assert find_min_max([7, 7, 7, 7]) == (7, 7)
	return minimum, maximum

