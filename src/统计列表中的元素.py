from collections import Counter

my_list = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']
count = Counter(my_list)  # defining a counter object

print(count)  # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})
# 算出b出现的次数
print(count['b'])  # of individual element
# 3
# 统计出现最多的元素和次数
print(count.most_common(1))  # most frequent element
for item, index in count.most_common(1):
    print(index)
    print(item)
# [('d', 5)]