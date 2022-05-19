def common_characters(string_1, string_2):
    common_letters = ""
    for letter in string_1:
        if letter in string_2:
            common_letters += letter + ","
        else:
            continue
    print(f"Common characters: {common_letters}")
