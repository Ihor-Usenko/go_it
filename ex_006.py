lst1 = [str(x) for x in range(10)]

lst2 = [str(x) for x in range(10, 20)]

# print(lst1)
# print(lst2)

# lst1.extend(lst2)

# print(lst1)
# print(lst1 + lst2)

lst3 = [*lst1, *lst2]

print(lst3)

