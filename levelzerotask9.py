def print_vowels(string_input):
    vowels = set()
    for vowel in string_input:
        if(vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o"):
            vowels.add(vowel)
        elif(vowel == "A" or vowel == "E" or vowel == "I" or vowel == "O"):
            vowels.add(vowel.lower())
        elif vowel == "u":
            vowels.add(vowel)
        elif vowel == "U":
            vowels.add(vowel.lower())
    print(f"Vowels: {vowels}", sep=",")
