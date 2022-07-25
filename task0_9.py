def print_vowels(string_input):
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_str = []
    for vowel in vowels:
        if vowel in string_input.lower():
            vowels_in_str = vowels_in_str + list(vowel)
    print("Vowels: ", ", ".join(vowels_in_str))


print_vowels("Umuzi")

