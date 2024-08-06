def get_grade(subject):
	"""
    Collects grades for a given subject from user input, calculates the average grade,
    and returns the average grade and the list of grades.

    Args:
    subject (str): The name of the subject.

    Returns:
    tuple: A tuple containing the average grade (float) and the list of grades (list of floats).
    """
	try:
		subject_list = []
		while True:
			grade = input(f"Enter the grade for {subject} (press Enter to finish): ")
			if grade.strip() == '':
				break
			try:
				subject_list.append(float(grade))
			except ValueError:
				print("Please enter a valid grade.")
		
		average_grade = sum(subject_list) / len(subject_list) if subject_list else 0.0
		return average_grade, subject_list
	except Exception as e:
		print(f"An error occurred: {e}")
		return 0.0, []


def main():
	"""
    Collects the number of students and their grades for various subjects from user input.
    Returns a dictionary where keys are student names and values are dictionaries of subjects with their average grades.

    Returns:
    dict: A dictionary containing student names as keys and their grades as values.
    """
	try:
		num_students = int(input("Enter the number of students: "))
	except ValueError:
		print("Please enter a valid number.")
		return {}
	
	student_data = {}
	
	for _ in range(num_students):
		student_name = input("Enter the student's name: ")
		all_grades = {}
		empty_input_count = 0
		
		while True:
			if empty_input_count == 2:
				print("Moving to the next student.")
				break
			
			subject = input("Enter the subject (or press Enter again to finish): ")
			if subject.strip() == '':
				empty_input_count += 1
				continue
			else:
				empty_input_count = 0
			
			average_grade, grades = get_grade(subject)
			if grades:
				all_grades[subject] = average_grade
			print(f"\nAverage grade for {subject}: {average_grade:.1f}")
		
		student_data[student_name] = all_grades
	
	return student_data


def calculate_average_grades(student_data):
	"""
    Calculates the overall average grade for each student across all subjects.

    Args:
    student_data (dict): A dictionary where keys are student names and values are dictionaries of subjects with their average grades.

    Returns:
    dict: A dictionary containing student names as keys and their overall average grade as values.
    """
	average_grades = {}
	for student_name, grades in student_data.items():
		total_sum = sum(grades.values())
		count = len(grades)
		average_grades[student_name] = total_sum / count if count != 0 else 0.0
	return average_grades


if __name__ == '__main__':
	student_data = main()
	
	# Print all student information
	print("\nAll Student Information:")
	for student_name, grades in student_data.items():
		print(f"\nName: {student_name}")
		for subject, average_grade in grades.items():
			print(f"{subject}: {average_grade:.1f}")
	
	# Print the final dictionary in the specified format
	print("\nFinal student data:")
	for student_name, grades in student_data.items():
		student_info = {"Name": student_name}
		student_info.update(grades)
		print(student_info)
	
	# Calculate and print overall average grades
	average_grades = calculate_average_grades(student_data)
	print("\nOverall average grade across all subjects:")
	for student_name, average_grade in average_grades.items():
		print(f"{student_name}: {average_grade:.1f}")
