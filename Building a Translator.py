#giraffe Translator
#vowels -> g
#--------------
#dog -> dgg
#cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter  in "supriyaSUPRIYA":
            translation = translation + "gadhi"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
