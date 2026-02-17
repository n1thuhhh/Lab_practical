# def fibonacci(n):
#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             return fibonacci(n-1)+fibonacci(n-2)
# n=int(input("enter the number"))
# for i in range(1,n+1):
#     print(fibonacci(i),end=" ")
#


# power set

def powerset(a,lst):
    if len(a)==0:
        print(lst)
    else:
        powerset(a[1:],lst)
        powerset(a[1:],lst+[a[0]])
a=[1,2,6,4,7]
powerset(a,[])