#Recursive Exercise 3
def factorial_recursive(n):
    #Base Case: 1! = 1
    if n == 1:
        return 1
    #Recursive Case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
#Call Factorial Recursive Function

print('factorial recursive'.title())
print(factorial_recursive(int(input("n! = "))))