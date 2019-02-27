import os
import json


def main():
    table_parties = []
    for partie in os.listdir('./Partie'):
        with open('./Partie/' + partie, 'r') as fichier:
            stats = json.loads(fichier.read())
            print(stats)
            table_parties.append(stats)
    print(table_parties)


def stats_jour():
    compteur = 0
    

main()

