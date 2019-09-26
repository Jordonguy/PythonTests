lst = ["a", "b", "a", "c", "c", "a", "c"]
temp = set(lst)
result = {}
for i in temp:
    result[i] = lst.count(i)
print(result)
