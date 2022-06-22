import task_template as tt

def remove_forbidden_character(value):
    analyzed_text = tt.TEXTS[value]

    # odstraní tečky, čárky a pomlčky

    """ Odstraní nechtěné znaky """
    for forbidden_character in analyzed_text:
        if forbidden_character == "." or forbidden_character == ",":
            analyzed_text = str(analyzed_text).replace(
                forbidden_character, "")
        elif forbidden_character == "-" or forbidden_character == "\n":
            analyzed_text = str(analyzed_text).replace(
                forbidden_character, " ")

    analyzed_text = analyzed_text.rsplit(" ")

    return analyzed_text