#lists & list slicing

li1 = [1,2,3,4,5]
li2 = ['a','b','c']
li3 = [1,2,'a',True]


array_list = ['Alarm clock', 'Antenna', 'Calculator', 'Computer', 'Digital camera', 'DVD player', 'Earbuds', 'Ebook', 'Floppy disc', 'Game console', 'Hard drive', 'Headphones', 'Laptop', 'Memory card', 'Memory stick', 'Microphone', 'Mouse', 'Mp3 player', 'Pda Phone', 'Photo camera', 'Printer', 'Projector', 'Remote control', 'Router', 'Scanner', 'Smart Board', 'Tablet PC', 'Usb stick', 'Video Camera', 'Webcam']
#print(array_list[0::2])
new_array_list1 = array_list [:]
#new_array_list2 = array_list [10:19]
#new_array_list3 = array_list [20:29]
new_array_list1 [0] = 'Alarm Only'

print(new_array_list1)
# print(new_array_list2)
# print(new_array_list3)
print(array_list)