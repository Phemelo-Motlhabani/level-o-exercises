def print_vowels(string_input):
    vowels = list()
    for vowel in string_input:
        if(vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o"):
            vowels.append(vowel)
        elif(vowel == "A" or vowel == "E" or vowel == "I" or vowel == "O"):
            vowels.append(vowel.lower())
        elif vowel == "u":
            vowels.append(vowel)
        elif vowel == "U":
            vowels.append(vowel.lower())
    vowels_string = ""
    for vowel in vowels:
        if vowel in vowels_string:
            pass
        else:
            vowels_string += vowel
    sep = ","
    print(f"Vowels: {sep.join(vowels_string)}")
