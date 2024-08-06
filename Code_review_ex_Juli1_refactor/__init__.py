def calculateSum(num1,num2):
    result=num1+num2
    if result>=10:   # if result is bigger or equal to 10
        print("Result is greater than or equal to 10")
    else:
        print( "Result is less than 10" )
    return (result)   # return result

def calculateMul(num1,num2):
"""" Calculates result of multiplication""""
    a = num1 * num2
    return a

def main():
    print(calculateSum(5,6))
    print(calculateMul(3,4))

if __name__ == "__main__":
    main()