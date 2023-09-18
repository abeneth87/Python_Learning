
with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
    list1 = [int(line.strip()) for line in file1]
    list2 = [int(line.strip()) for line in file2]


result = [num for num in list1 if num in list2]
# Write your code above 👆

print(result)
