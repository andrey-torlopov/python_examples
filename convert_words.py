import random

# Конвертер слов и букв
input_str = """

"""

def switch(letter):
    if letter == "А":
        return "4"
    elif letter == "О":
        return "0"
    elif letter == "Д":
        return "9"
    elif letter == "Е":
        return "3"
    elif letter == "З":
        return "3"
    elif letter == "И":
        return "N"
    elif letter == "Я":
        return "R"
    elif letter == "B":
        return "8"
    elif letter == "T":
        return "7"
    elif letter == "Б":
        return "6"
    else:
        return letter


def change_random_letter(word):
    arr = list(word)
    for i in range(len(arr)):
        pass

    return word


def shuffle_word(word):
    arr = list(word)
    random.shuffle(arr)
    result = "".join(arr)
    result = change_random_letter(result)

    return result


def is_plan_a():
    if random.randint(1, 100) >= 50:
        return True
    else:
        return False


def convertText(text, is_force_a):
    if is_force_a == True:
        return "".join(list(map(switch, list(text.upper()))))
    else:
        words = text.split()
        for i in range(len(words)):
            word = words[i]
            words[i] = word[0] + shuffle_word(word[1:-1]) + word[-1]
    return " ".join(words)


print(convertText(input_str, False))
