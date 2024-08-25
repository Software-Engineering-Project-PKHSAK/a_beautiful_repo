def calculate_factorial(n):
    if n==0 or n==1:
        return 1
    else: 
        return n*calculate_factorial(n-1);

# number = int(input("Enter a number to calculate its factorial: "))
# factorial = calculate_factorial(number)
# print(f"The factorial of {number} is: {factorial}")

# result = factorial / 0
