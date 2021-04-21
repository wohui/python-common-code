
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))    # 根据字典键排序

print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}.values()))    # 根据字典值排序

src_dict ={1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}
print({k:src_dict[k] for k  in sorted(src_dict)})