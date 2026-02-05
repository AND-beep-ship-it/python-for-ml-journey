alphabets = [ "a", "b", "a", "c", "b", "a" ]

freq = {}

for letter in alphabets:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

print(freq)