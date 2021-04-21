src_list =[1,2,3,4,4,3,2,1]

# 元组去重
print(list(set(src_list)))

# 字典的fromkey
src_list =[1,2,3,4,4,3,2,1]
# 先将重复的list转换成字典的key 这一步会去重得到最后的key返回字典类型
# 然后通过.keys 获取全部的keys,得到dict_keys列表
# 最后转换
dict_list = {}.fromkeys(src_list).keys()
print(list(dict_list))

# 普通方法去重
src_list =[1,2,3,4,4,3,2,1]
dst_list=[]
for item in src_list:
    if item not in dst_list:
        dst_list.append(item)
print(dst_list)

# 改成列表推导式
src_list =[3,2,1,4,4,3,2,1]
dst_list=[]
[dst_list.append(item) for item in src_list if item not in dst_list]
print(dst_list)

# sort
src_list =[3,2,1,4,4,3,2,1]
dst_list.sort(key=src_list.index)
print(dst_list)
