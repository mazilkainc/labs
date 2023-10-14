list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
len_players = len(list_players)
team_1 = list_players[0:int(len_players/2):1]
team_2 = list_players[int(len_players/2)::]
print(team_1)
print(team_2)