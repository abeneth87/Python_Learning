def add(*args):
    result = sum(args)
    return result


numbers = input("Enter numbers separated by commas: ")
number_list = [int(num.strip()) for num in numbers.split(',')]
total = add(*number_list)
print("Result:", total)
