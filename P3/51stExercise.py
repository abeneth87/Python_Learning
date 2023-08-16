#Exercise
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]
fill = '*'
empty = ' '
def show_pic():
    for row in picture:
        for pixel in row:
            if pixel == 1:
                print(fill, end = '')
            else:
                print(empty, end = '')
        print('') # For empty line after every row

show_pic()
show_pic()
show_pic()
