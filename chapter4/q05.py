def func(n):
    try:
        return float(n)
    except ValueError:
        print("ValueError: could not convert string to float:", n)
	
	

print(func("123.33"))
print(func("123.33s"))