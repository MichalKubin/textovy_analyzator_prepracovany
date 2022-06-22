"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie -
přepracovaný pomocí funkcí
author: Michal Kubín
email: kubin.michal@gmail.com
discord: Michal Kubín #0577
"""

import task_template as tt
import users
import functions as fs

separator = "-" * 36

# Vyžádá si od uživatele přihlašovací jméno a heslo

login = input("Please insert your login: ")

# zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,

texts_count = len(tt.TEXTS)

if str(login) in users.logins:
    password = input("Please insert your password: ")

    # pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,

    if str(password) == users.users[str(login)]:
        print(separator)
        print(f"Hi, {login}! Welcome to the Text Analyser!")

        if texts_count == 1:
            chosen_text = 0

            print(f"We have 1 text to be analyzed:")
            print(separator)
            print(tt.TEXTS[chosen_text])
            print(separator)

            # Pro vybraný text spočítá následující statistiky:
            analyzed_text = fs.remove_forbidden_character(chosen_text)

            # odstraní uvozovky na začátku a na konci textu, které po
            # rozdělení vytvoří samostatné znaky
            analyzed_text = fs.remove_forbidden_space(chosen_text)

            # počet slov
            word_count = len(analyzed_text)

            if word_count == 1:
                print("There is 1 word in the selected text.")
            else:
                print(f"There are {word_count} words in the selected text.")

            # počet slov začínajících velkým písmenem,

            fs.get_words_with_capitals(chosen_text)

            # počet slov psaných velkými písmeny,

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

            # počet slov psaných malými písmeny,

            words_lowercase = 0

            for words in analyzed_text:
                if words.islower():
                    words_lowercase += 1

            if words_lowercase == 1:
                print("There is 1 lowercase word.")
            else:
                print(f"There are {words_lowercase} lowercase words.")

            # počet čísel (ne cifer),

            numbers_count = 0

            for words in analyzed_text:
                if words.isnumeric():
                    numbers_count += 1

            if numbers_count == 1:
                print("There is 1 numeric string.")
            else:
                print(f"There are {numbers_count} numeric strings.")

            # sumu všech čísel (ne cifer) v textu.

            numbers_sum = 0
            numbers_sum = int(numbers_sum)

            for words in analyzed_text:
                if words.isnumeric():
                    numbers_sum += int(words)

            print(f"The sum of all the numbers: {numbers_sum}")

            # Program zobrazí jednoduchý sloupcový graf, který bude
            # reprezentovat četnost různých délek slov v textu.

            print(separator)
            print(" LEN |       OCCURENCES       | NR. ")
            print(separator)

            word_length = []

            for words in analyzed_text:
                word_length.append(len(words))

            word_length.sort()
            # print(word_length)

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

        else:
            print(f"We have {texts_count} texts to be analyzed.")
            print(separator)
            print("For a text analysis you can choose from these texts:\n")

            for text_no, text_text in enumerate(tt.TEXTS):
                print(f"No. {text_no + 1}: {tt.TEXTS[text_no]}")

            print(separator)
            chosen_text = input("Please choose one of these texts for"
                                " follow-up "
                                "analysis (use numbers 1/2/3 etc.): ")

            # pokud uživatel zadal špatný vstup nebo číslo mimo hranici,
            # upozorni ho a ukonči program

            if str(chosen_text).isdecimal() is False or int(chosen_text) < 1 \
                    or int(chosen_text) > 3:
                print("Wrong value entered. Terminating the program..")

            # pokud vybral správně, zahaj analýzu textu

            else:
                print(f"Your choice: text No. {chosen_text}. Initiating "
                      f"analysis..")
                print(separator)

            # Pro vybraný text spočítá následující statistiky:

            # odstraní tečky, čárky a pomlčky

                analyzed_text = fs.remove_forbidden_character(
                    int(chosen_text) - 1)
                # odstraní uvozovky na začátku a na konci textu, které po
                # rozdělení vytvoří samostatné znaky

                analyzed_text = fs.remove_forbidden_space(int(chosen_text) - 1)

                # počet slov,

                word_count = len(analyzed_text)

                if word_count == 1:
                    print("There is 1 word in the selected text.")
                else:
                    print(f"There are {word_count} words in the selected "
                          f"text.")

                # počet slov začínajících velkým písmenem,
                fs.get_words_with_capitals(int(chosen_text) - 1)

                # počet slov psaných velkými písmeny,

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

                # počet slov psaných malými písmeny,

                words_lowercase = 0

                for words in analyzed_text:
                    if words.islower():
                        words_lowercase += 1

                if words_lowercase == 1:
                    print("There is 1 lowercase word.")
                else:
                    print(f"There are {words_lowercase} lowercase words.")

                # počet čísel (ne cifer),

                numbers_count = 0

                for words in analyzed_text:
                    if words.isnumeric():
                        numbers_count += 1

                if numbers_count == 1:
                    print("There is 1 numeric string.")
                else:
                    print(f"There are {numbers_count} numeric strings.")

                # sumu všech čísel (ne cifer) v textu.

                numbers_sum = 0
                numbers_sum = int(numbers_sum)

                for words in analyzed_text:
                    if words.isnumeric():
                        numbers_sum += int(words)

                print(f"The sum of all the numbers: {numbers_sum}")

                # Program zobrazí jednoduchý sloupcový graf, který bude
                # reprezentovat četnost různých délek slov v textu.

                print(separator)
                print(" LEN |       OCCURENCES       | NR. ")
                print(separator)

                word_length = []

                for words in analyzed_text:
                    word_length.append(len(words))

                word_length.sort()
                # print(word_length)

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

    # pokud nesedí login a heslo, upozorni uživatele a ukonči program

    else:
        print("Login details do not match. Terminating the program..")

# pokud není registrovaný, upozorni jej a ukonči program.

else:
    print("Unregistered user, terminating the program..")
