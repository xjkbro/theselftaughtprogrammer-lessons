# Q01: Write a function that takes a number as an input and returns that number squared.
def squared ( n ):
	"""
	Returns the square of a number
	"""
	return n * n

print("5^2:", squared(5))

# =======================
# Q02: Create a function that accepts a string as a parameter and prints it.
def printString(str):
    """
    Prints string that was passed
	"""
    print("Printing string...",str)
    
printString("Hello World")
printString("My name is Jason")
printString("Python is fun!")

# =======================
# Q03: Write a function that takes three required parameters and two optional parameters.

def sum(x, y = 2, z = 4):
	"""
	Prints the sum of three numbers, two of which are optional
	"""
	print("The sum is: ", x+y+z)

sum(1)
sum(1,4)
sum(3)


# =======================
# Q04: Write a program with two functions. The first function should take an integer as a parameter and return the result of the integer divided by 2. The second function should take an integer as a parameter and return the result of the integer multiplied by 4. Call the first function, save the result as a variable, and pass it as a parameter to the second function.
def func1(n):
    """
	Divides the number by 2
	"""
    return n/2
def func2(n):
	"""
	Multiplies the number by 4
	"""
	return n*4

x = func1(4) #returns 2
y = func2(x) #returns 8

print(x)
print(y)

print(func2(func1(4)))

# =======================
# Q05: Write a function that converts a string to a float and returns the result. Use exception handling to catch the exception that could occur.	

def func(n):
    """
	Converts a string to a float
	Handles exceptions
    """
    try:
        return float(n)
    except ValueError:
        print("ValueError: could not convert string to float:", n)

print(func("123.33"))
print(func("123.33s"))

# =======================
# Q06: Add a docstring to all the functions you wrote in challenges 1-5.
