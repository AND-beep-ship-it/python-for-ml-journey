#Exponent_Function
#print(2**3)
from unittest import expectedFailure


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2,3))


#2Dlists &Nested Loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[2][1])
for row in number_grid:
    for col in row:
        print (col)



#Try/Except
try:
    number = int(input("Enter a number: "))
    print(number)
except:
     print("invalid Input")


#READING FILES
employee_file = open("Anyfile.txt", "r+")
for employee in employee_file.readline():
    print(employee)
employee_file.close
print(Anyfile_file.readlines()[1])

#Writing and Appending file


