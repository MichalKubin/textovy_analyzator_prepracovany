import task_template as tt

separator = "-" * 36

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
    """ Vrací počet slov s prvním písmenem velkým """
    analyzed_text = remove_forbidden_space(value)
    words_with_capitals = 0

    for words in analyzed_text:
        if words[0].isupper():
            words_with_capitals += 1

    if words_with_capitals == 1:
        print("There is 1 titlecase word.")
    else:
        print(f"There are {words_with_capitals} titlecase words.")

def get_uppercase_words(value):
    """ Vrací počet slov vypsaných kapitálkami """
    analyzed_text = remove_forbidden_space(value)
    words_uppercase = 0

    for words in analyzed_text:
        if words.isupper() and words.isalpha():
            words_uppercase += 1
        elif words.isupper() and words.isalpha() is False:
            words_uppercase += 0

    if words_uppercase == 1:
        print("There is 1 uppercase word.")
    else:
        print(f"There are {words_uppercase} uppercase words.")

        words_uppercase = 0

def get_lowercase_words(value):
    """ Vrací počet slov vypsaných kompletně malými písmeny """
    analyzed_text = remove_forbidden_space(value)
    words_lowercase = 0

    for words in analyzed_text:
        if words.islower():
            words_lowercase += 1

    if words_lowercase == 1:
        print("There is 1 lowercase word.")
    else:
        print(f"There are {words_lowercase} lowercase words.")

def get_numbers(value):
    """ Vrací počet čísel v textu """
    analyzed_text = remove_forbidden_space(value)

    numbers_count = 0

    for words in analyzed_text:
        if words.isnumeric():
            numbers_count += 1

    if numbers_count == 1:
        print("There is 1 numeric string.")
    else:
        print(f"There are {numbers_count} numeric strings.")

def get_sum(value):
    """ Vrací sumu všech čísel nalezených v textu """
    analyzed_text = remove_forbidden_space(value)

    numbers_sum = 0
    numbers_sum = int(numbers_sum)

    for words in analyzed_text:
        if words.isnumeric():
            numbers_sum += int(words)

    print(f"The sum of all the numbers: {numbers_sum}")

def print_graph(value):
    """ Vytiskne výsledná data v jednoduchém grafu """
    analyzed_text = remove_forbidden_space(value)

    print(separator)
    print(" LEN |       OCCURENCES       | NR. ")
    print(separator)

    word_length = []

    for words in analyzed_text:
        word_length.append(len(words))

    word_length.sort()

    count_length = 1

    while count_length <= word_length[-1]:
        print(str(count_length).rjust(4) +
              str("") * (4 - len(str(count_length))) +
              " |" +
              "*" * (word_length.count(count_length)) +
              " " * (24 - word_length.count(count_length)) +
              "|" +
              str(word_length.count(count_length)).rjust(4))
        count_length += 1