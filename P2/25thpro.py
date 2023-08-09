#list unpacking

#a,b,c, *other, d = [1,2,3,4]
a,b,c, *other = range(100)

print(a)
print(b)
print(c)
print(other)

#none return for weapon system during game initialization
weapons = None
game_start = print('currently you have', weapons)