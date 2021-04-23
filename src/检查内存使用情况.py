import sys

num = 21

print(sys.getsizeof(num))
nnum = num+1
print(sys.getsizeof(num))
print(sys.getsizeof(nnum))
