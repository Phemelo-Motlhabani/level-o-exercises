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
    vowel_string = ""
    for vowel in vowels:
        vowels_string += vowel + ","
    print(f"Vowels: {vowels_string}")
