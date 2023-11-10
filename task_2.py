def find_common_participants(first_group, second_group, separator=','): # TODO Напишите функцию find_common_participants
    lst_1 = first_group.split(separator)
    lst_2 = second_group.split(separator)
    common_participants = list(set(lst_1).intersection(lst_2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group) # TODO Провеьте работу функции с разделителем отличным от запятой

print(common_participants)

