list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

number_of_players = len(list_players)

half_of_number = round(number_of_players/2)

team_1 = list_players[:half_of_number]
team_2 = list_players[half_of_number:]

print(team_1)
print(team_2)
