
lst = [1, 2, 3, 4, 4]
lst1 = [1, 2, 3, 4, 5, 6]

set1=set(lst)
set2=set(lst1)


# Convert the list to a set to remove duplicates
duplicates = set1 ^ set2

# Convert back to a list if needed


print(duplicates)



