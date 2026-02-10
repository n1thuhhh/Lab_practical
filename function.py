# copy Function

a=[12,3,4,5,2,3,7,9,3,6,3]
b=a.copy()
print(a)
print(b)

# count Function
c=a.count(3)
print(c)

# split function
str1= "hello everyone"
s=str1.split("e")
print(s)

# join Function
tup=("My","name","is","Nitesh","Gupta")
str2="#".join(tup)
print(str2)






# 1
a=[12,3,4,5,2,3,7,9,3,6,3]
b=a
c=a.copy()
b.append(4)
c.append(4)
print(a)
print(b)
print(c)

# 2
import copy
a = [[1, 2, 3], [4, 5, 6]]
b = copy.deepcopy(a)
b[0].append(7)
print("b: ", b)
print("a: ", a)

# 3
s = "I am busy rn"
words = s.split()
words1=words[::-1]
reverse_words = " ".join(words1)

print(reverse_words)

# 4
z=[2,5,4,10,1,5,3]
print(z[-2:-6:-1])

# 5
b=([2,3],[4,5,10])
b[0].append(8)
print(b)
b[0][0]=9
print(b)
