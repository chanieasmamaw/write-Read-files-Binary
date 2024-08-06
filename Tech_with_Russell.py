import math
"""
def is_positive_number(num):
    assert num >= 0, "num must be positive"
    print("YAY!")

# Test the function
is_positive_number(-2)


def find_max(numbers):
    assert numbers, "Numbers must not be empty"
    assert all(isinstance(num, (int, float)) for num in numbers), "All elements must be numbers"
    
    max_number = max(numbers)
    return max_number

# Example usage
nums = [3, 7, 1, 9, 4]
max_num = find_max(nums)
print(f"The maximum number is: {max_num}")

# Test with an empty list (this will raise an AssertionError)


empty_nums = []
max_num_empty = find_max(empty_nums)

    #the first element should be list of 3 the power
    #the first element shuld be the power
    #2nd the type or laser (1,2,3)
    #3rd should be direction(x,y)

"""


def fire_laser(power, laser_type, direction):
    assert 0 <= power <= 100, "Power should be between 0 and 100"
    assert laser_type in [1, 2, 3], "Laser type must be either 1, 2, or 3"
    assert len(direction) == 3, "Direction must be a list/tuple with exactly three elements"
    assert all(0 <= coord <= 100 for coord in direction), "All direction coordinates should be within the range 0-100"
    
    # Code to fire laser goes here
    print(f"Firing laser of type {laser_type} in direction {direction} with power {power}")


# Test case with 3D direction
fire_laser(90, 2, [1, 2, 3])  # Example of a valid 3D direction

# Test case with invalid inputs
fire_laser(101, None, [1, 2])  # This will raise AssertionError due to invalid power
fire_laser(80, 4, [101, 50, 70])  # This will raise AssertionError due to invalid laser type and direction coordinates


