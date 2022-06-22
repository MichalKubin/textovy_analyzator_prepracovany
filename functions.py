import task_template as tt

def remove_forbidden_character(value):
    """ Odstraní nechtěné znaky """
    analyzed_text = tt.TEXTS[value]

    # odstraní tečky, čárky a pomlčky
    for forbidden_character in analyzed_text:
        if forbidden_character == "." or forbidden_character == ",":
            analyzed_text = str(analyzed_text).replace(
                forbidden_character, "")
        elif forbidden_character == "-" or forbidden_character == "\n":
            analyzed_text = str(analyzed_text).replace(
                forbidden_character, " ")

    analyzed_text = analyzed_text.rsplit(" ")

    return analyzed_text

def remove_forbidden_space(value):
    """ Odstraní nechtěné mezery v textu """
    analyzed_text = remove_forbidden_character(value)

    for forbidden_space in analyzed_text:
        if forbidden_space == '':
            analyzed_text.remove('')

    return analyzed_text

def get_words_with_capitals(value):
    analyzed_text = remove_forbidden_space(value)
    words_with_capitals = 0

    for words in analyzed_text:
        if words[0].isupper():
            words_with_capitals += 1

    if words_with_capitals == 1:
        print("There is 1 titlecase word.")
    else:
        print(f"There are {words_with_capitals} titlecase words.")