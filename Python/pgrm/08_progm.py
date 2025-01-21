x = [1, 2, 2, 3, 4, 4, 5]

unique_list = []

for item in x:
    if item not in unique_list:
        unique_list.append(item)

unique = tuple(unique_list)
print(unique)
