n=int(input("enter the number"))
def fibonacci(n):
    n1=0
    n2=1
    print(n1)
    print(n2)
    for i in range(n-2):
        sum=n1+n2
        print(sum)
        n1=n2
        n2=sum
fibonacci(n)


