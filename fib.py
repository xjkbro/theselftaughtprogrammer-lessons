# Dynamic Programming Practice with Fibonacci

def fib(n): 
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


# memo = [0,1] + [None] * 1000

# def fib (n):
# 	if memo[n] is not None:
# 		return memo[n]
# 	else:
# 		memo[n] = fib(n-1) + fib(n-2)
# 		return memo[n]



x = input("Enter a number: ")

for i in range (0, int(x)+1):
	print("Fib (", i, "): " , str(fib(i)) )