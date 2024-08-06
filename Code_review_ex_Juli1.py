



def is_divisible_by_numb(numb,by):
	return numb %by == 0


def is_prim_numb(numb):
	for i in range(2, numb):
		if is_divisible_by_numb(numb, i):
			return False
		else:
			return True
		
		
def find_prim_num(start, end):
	for i in range(start, end):
		if is_prim_numb(i):
			print(f" is 2 Prime number{i}")
			
def main():
	range_start = int(input("Enter the integer number: "))
	range_end = int(input("Enter the integer number"))
	find_prim_num(range_start, range_end)


if __name__ == '__main__':
	main()
 

















