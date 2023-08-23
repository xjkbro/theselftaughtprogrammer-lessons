def func1(n):
    return n/2
def func2(n):
	return n*4


x = func1(4) #returns 2
y = func2(x) #returns 8


print(x)
print(y)


print(func2(func1(4)))