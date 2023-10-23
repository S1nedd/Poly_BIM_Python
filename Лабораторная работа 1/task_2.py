# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44 # Мб
number_of_sheets = 100
number_of_strings = 50
number_of_symbols = 25
weight_of_symbol = 4 # б

number_of_books = round((volume * 1024 ** 2) // (number_of_sheets * number_of_strings * number_of_symbols * weight_of_symbol))

print("Количество книг, помещающихся на дискету:", number_of_books)
