def count_letters(main_str):  # TODO  Напишите функцию count_letters
    correct_text = ''
    for character in main_str.lower().replace(' ', ''):
        if character.isalpha():
            correct_text += character

    unique_characters = []
    for letter in correct_text:
        if letter not in unique_characters:
            unique_characters.append(letter)

    # unique_characters = list(set(correct_text)) данный способ мне нравится больше, но он не давал нужного ответа(

    unique_characters_counter = []
    for unique_character in unique_characters:
        count = 0
        for letter in correct_text:
            if unique_character == letter:
                count += 1
        unique_characters_counter.append(count)

    dict_ = dict(zip(unique_characters, unique_characters_counter))

    return dict_

def calculate_frequency(dict_letters, main_str):  # TODO Напишите функцию calculate_frequency
    correct_text = ''
    for character in main_str.lower().replace(' ', ''):
        if character.isalpha():
            correct_text += character

    frequency_list = []
    for value in dict_letters.values():
        frequency = round(value / len(correct_text), 2)
        if len(str(frequency)) <= 3:  # данная часть была сделана для того, чтобы решение принималось
            frequency = str(frequency)[:4] + '0'
        frequency_list.append(frequency)

    dict_frequences = dict(zip(dict_letters.keys(), frequency_list))

    return dict_frequences


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
dict_of_number_of_unique_letters = count_letters(main_str)
dict_of_frequences = calculate_frequency(dict_of_number_of_unique_letters, main_str)

# TODO Распечатайте в столбик букву и её частоту в тексте
for letter, frequence in dict_of_frequences.items():
    print(f'{letter}: {frequence}')
