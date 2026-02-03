print("   /|")
print("  / |")
print(" /  |")
print("/___|")
character_name = "George"
character_age = "70"
print("There once was a man named" + " " + character_name + ",")
print("he was" + " " + character_age + " years old")
print("He really liked the name george")
print("but didn't liked being" + " " + character_age )
phrase = "Giraffe Academy"
print(phrase + " " + "is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(len(phrase))
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name +  "!" + " You are " + age + " years old")

#calculator
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
Sum = num1 + num2
print(Sum)

#MadLibs Game
color = input("Enter your color: ")
plural_noun = input("Enter your plural noun: ")
celebrity = input("Enter your celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

#Tuples
coordinates = (4, 5)
print(coordinates[0])

#Functions
def say_hi():
    print("Hello " + name + "!")

say_hi()

#Return
def cube(num):
    return num*num*num

print(cube(4))
