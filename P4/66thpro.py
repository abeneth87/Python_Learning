#Pure function in coding

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([44,55,66]))

#Rule 1: Produces the same output everytime for the given input
#Rule 2: It should not affect anything in the outside world. 
        # Here, if the new_list was declared outside. 
        #It will affect the programmer's logic and declaration
