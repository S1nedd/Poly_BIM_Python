numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

correct_lst = []
for number in numbers:
    if number is None:
        continue
    else:
        correct_lst.append(number)

sum_of_numbers = sum(correct_lst)
count_of_numbers = len(numbers)
average = sum_of_numbers/count_of_numbers

numbers[4] = average


print("Измененный список:", numbers)
