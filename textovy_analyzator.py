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
            fs.get_uppercase_words(chosen_text)

            # počet slov psaných malými písmeny,
            fs.get_lowercase_words(chosen_text)

            # počet čísel (ne cifer),
            fs.get_numbers(chosen_text)

            # sumu všech čísel (ne cifer) v textu.
            fs.get_sum(chosen_text)

            # Program zobrazí jednoduchý sloupcový graf, který bude
            # reprezentovat četnost různých délek slov v textu.
            fs.print_graph(chosen_text)

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

                fs.get_uppercase_words(int(chosen_text) - 1)

                # počet slov psaných malými písmeny,
                fs.get_lowercase_words(int(chosen_text) - 1)

                # počet čísel (ne cifer),
                fs.get_numbers(int(chosen_text) - 1)

                # sumu všech čísel (ne cifer) v textu.
                fs.get_sum(int(chosen_text) - 1)

                # Program zobrazí jednoduchý sloupcový graf, který bude
                # reprezentovat četnost různých délek slov v textu.
                fs.print_graph(int(chosen_text) - 1)

    # pokud nesedí login a heslo, upozorni uživatele a ukonči program

    else:
        print("Login details do not match. Terminating the program..")

# pokud není registrovaný, upozorni jej a ukonči program.

else:
    print("Unregistered user, terminating the program..")
