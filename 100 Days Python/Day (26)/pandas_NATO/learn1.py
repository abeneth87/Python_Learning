
student_dict = {
    "student": ["Abeneth", "Rama", "Chandran"],
    "score": [56, 78, 98]
}

#Looping through dictionary
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data_frame

# for (key, value) in student_data_frame.items():
#     print(value)


#     loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    print(row.student)
