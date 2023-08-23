def squared ( n ):
	"""
	Returns the square of a number
	"""
	return n * n

print("5^2:", squared(5))

# =======================
def printString(str):
    """
    Prints string that was passed
	"""
    print("Printing string...",str)
    
printString("Hello World")
printString("My name is Jason")
printString("Python is fun!")

# =======================

def sum(x, y = 2, z = 4):
	"""
	Prints the sum of three numbers, two of which are optional
	"""
	print("The sum is: ", x+y+z)

sum(1)
sum(1,4)
sum(3)

# =======================

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