import os
import json

date_parties = []
stats_of_game_per_day = {}
for game in os.listdir('./Partie'):
    with open('./Partie/' + game, 'r') as fichier:
        date = json.loads(fichier.read())
        print(date)
        date_parties.append(date)
for date_of_game in date_parties:
    date = date_of_game['Start time'][:8]
    if date in stats_of_game_per_day.keys():
        stats_of_game_per_day[date] += 1
    else:
        stats_of_game_per_day[date] = 1
count = 0
chrono_temp = 0
for time_of_game in date_parties:
    count += 1
    heure_start = time_of_game['Start time'][9:11]
    min_start = time_of_game['Start time'][12:14]
    heure_end = time_of_game['End time'][9:11]
    min_end = time_of_game['End time'][12:14]
    print(heure_start + ":" + min_start + " to " + heure_end + ":" + min_end)
    if heure_start == heure_end:
        chrono = int(min_end) - int(min_start)
        print(chrono)
        chrono_temp += chrono
    elif heure_start != heure_end:
        chrono = (int(min_end) + 60) - int(min_start)
        print(chrono)
        chrono_temp += chrono
average_chrono = chrono_temp / count
stats_of_game_per_day['average_time'] = average_chrono
print(stats_of_game_per_day)
