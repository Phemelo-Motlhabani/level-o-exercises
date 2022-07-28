def common_characters(string_1, string_2):
    common_letters = ""
    for letter in string_1.lower():
        if letter in common_letters:
            continue
        elif letter in string_2.lower():
            common_letters += letter
        else:
            continue
    sep = ", "
    print(f"Common letters: {sep.join(common_letters)}")


common_characters("HOUSES", "computers")
