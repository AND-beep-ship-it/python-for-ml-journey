from turtledemo.clock import hand

is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a long Female")
else:
    print("You are neither male nor tall")

#CalxulatorBUTBETTER
    Num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    Num2 = float(input("Enter first number: "))

    if op == "+":
        print(Num1 + Num2)
    elif op == "-":
        print(Num1 - Num2)
    elif op == "/":
        print(Num1 / Num2)
    elif op == "*":
        print(Num1 * Num2)
    else:
        print("INVALID OPERATION")


#Dictionaries
month_conversions = {
    "jan" : "JANUARY",
    "feb" : "FEBRUARY",
    "mar" : "MARCH",
    "apr" : "APRIL",
    "may" : "MAY",
    "jun" : "JUNE",
    "jul" : "JULY",
    "aug" : "AUGUST",
    "sep" : "SEPTEMBER",
    "oct" : "OCTOBER",
    "nov" : "NOVEMBER",
    "dec" : "DECEMBER"
}

print(month_conversions.get("jan", "NOT A VALID KEY"))


#While
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with Loop")

#GUESSING GAME
secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOu Loose")
else:
    print("YOU Win!")
