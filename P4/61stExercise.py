def highest_even(li):
    even_numbers = []
    for item in li:
        if item % 2 == 0:
            even_numbers.append(item)
    return max(even_numbers)
print(highest_even([2,8,10,2,3,4,8,11]))


