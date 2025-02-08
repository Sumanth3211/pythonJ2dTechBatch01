lst = [1, 2, 3, 4, 4]
lst1 = [1, 2, 3, 4, 5, 6]

# Finding duplicates in lst
duplicates_lst = set([x for x in lst if lst.count(x) > 1])
s1=set(lst) ^set(lst1)

# Finding common elements (duplicates across lists)
duplicates_across = set(lst) & set(lst1)

print("Duplicates in lst:", duplicates_lst)
print("Common elements in both lists:", duplicates_across)

print(s1)