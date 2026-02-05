Students_name = {
    "R": "Rahul , 25",
    "A": "Anand , 50",
    "S": "Supriya , 10",
    "P": "Priyanshu , 5",
}

print(Students_name.get(input(Students_name) , "Not Found"))

#BETTER CODE
Students = {
    "R": {"name": "Rahul", "marks": 25},
    "A": {"name": "Anand", "marks": 50},
    "S": {"name": "Supriya", "marks": 10},
    "P": {"name": "Priyanshu", "marks": 5},
}

key = input("Enter student key (R/A/S/P): ")

student = Students.get(key)

if student:
    print("Name:", student["name"])
    print("Marks:", student["marks"])
else:
    print("Not Found")
