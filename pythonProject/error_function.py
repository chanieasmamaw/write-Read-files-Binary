
"""try:
    dict_students = {
        485: "George Stan",
        159: "Jan Inno",
        867: "Harry Alli",
        787: "Anne Son"
    }
    # Accessing a non-existent key to trigger KeyError
    student = dict_students.append('new_key','new_value')
    print(student)
    
except IndexError as e:
    print(f"KeyError: {e.__class__.__name__} - {e}")
    program_survived = False  # If False, it means we caught an exception
except Exception as e:
    print(f"An unexpected exception occurred: {e.__class__.__name__} - {e}")
    program_survived = False  # If False, it means we caught an unexpected exception
    program_survived = True  # If True, it means no exception was caught
finally:
       print(f"The program {program_survived}")
"""


"""
case-> a: The user enter the non existing key
case -> b: The user inter string rather than key(values)

"""

"""try:
    dict_students = {
        485: "George Stan",
        159: "Jan Inno",
        867: "Harry Alli",
        787: "Anne Son"
    }
    # Accessing a non-existent key to trigger KeyError
    student = dict_students.append('new_key','new_value')
    print(student)

except IndexError as e:
    print(f"KeyError: {e.__class__.__name__} - {e}")
    program_survived = False  # If False, it means we caught an exception
except Exception as e:
    print(f"An unexpected exception occurred: {e.__class__.__name__} - {e}")
    program_survived = False  # If False, it means we caught an unexpected exception
    program_survived = True  # If True, it means no exception was caught
finally:
       print(f"The program {program_survived}")
"""

"""
case-> a: The user enter the non existing key
case -> b: The user inter string rather than key(values)

"""

try:
	dict_students = {485: "Geroge Stan",
	                 159: "Jan Inno",
	                 867: "Harry Alli",
	                 787: "Anne Son"
	                 }
	student_id = int(input("Please enter a student ID:"))
	if student_id in dict_students:
		print(f"Student name {dict_students[student_id]}")
	else:
        print(f"Students id is not found in dictionary")
	    program_survived = False
    program_survived = True
except ValueError as e:
    print(f"Invalid input: {e}. Please enter a valid integer ID.")
    program_survived = False

finally:
	print(f"program is: {program_survived}")





























