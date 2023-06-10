import random

# Конвертер слов и букв
input_str = """
Александр Сергеевич Пушкин - один из наиболее известных русских писателей, создавший множество произведений, которые до сих пор пользуются большой популярностью. Вот первые два абзаца из сказки "Золотой петушок", которые захватывают читателей в увлекательное приключение:

"Жил-был царь, и была у него дочь царевна золотая. Царь на свете всех богаче, а дочь-то не простая, а золотая! Она, куда ни посмотрит, всё золото видит: и на деревьях, и на траве, и на водах, и на домах, и на людях - всё одно золото!

Все принцы и короли издалека приезжали, чтобы увидеть золотую царевну, да ведь никто не мог её достать, потому что ей надо было жениха найти, который был бы ей равен, а она желала, чтобы он был еще и красивее неё."
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
