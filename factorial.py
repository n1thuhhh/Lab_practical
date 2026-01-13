n=int(input("enter the number"))
fact=1
def factorial(n):
    if(n==0):
        return 1
    else:
        fact=n*factorial(n-1)
        return fact
print("factorial of ",n,"is",factorial(n))