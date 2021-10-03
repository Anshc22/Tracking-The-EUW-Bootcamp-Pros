import requests
import time
import json
from bs4 import BeautifulSoup as bs

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    while True:
        url = "https://www.trackingthepros.com/d/list_bootcamp"

        querystring = {"existing": "no", "_": "1633176671549"}

        payload = ""
        headers = {
            "cookie": "PHPSESSID=36eg62iovtfrk7mc8k04i5p09o",
            "Connection": "keep-alive",
            "X-KL-Ajax-Request": "Ajax_Request",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?1",
            "User-Agent": "User-Agent",
            "sec-ch-ua": "^\^Chromium^^;v=^\^94^^, ^\^Google"
        }

        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)

        raw = response.text
        Pros = json.loads(raw)['data']
        players = dict()
        for pro in Pros:
            if pro['online'] != '':
                # print(pro['plug'],pro['gameID'],pro['online'])
                if pro['gameID'] in players:
                    # print(players[pro['gameID']])
                    players[pro['gameID']].append((pro['plug'], pro['summoner'][pro['summoner'].find(
                        ']')+2:-4], pro['role'], pro['team_plug'], pro['rankHigh'], pro['rankHighLPNum'], pro['online'][:3]))
                else:
                    players[pro['gameID']] = list()
                    players[pro['gameID']].append((pro['plug'], pro['summoner'][pro['summoner'].find(
                        ']')+2:-4], pro['role'], pro['team_plug'], pro['rankHigh'], pro['rankHighLPNum'], pro['online'][:2]))

        clear()
        if len(players) == 0:
            print(f'\n---No Players Online----')
        else:
            players = {k: v for k, v in sorted(players.items(), key=lambda item: (
                item[1][0][3], int(item[1][0][5])), reverse=True)}
            for k, v in players.items():
                print(f'Game Time:- {v[0][6]} Min\n')
                for player in v:
                    print(
                        f'{player[3]} | {player[2]} | {player[0]}  :- {player[1]} ({player[4]} {player[5]}LP)')
                print(f'\n-------******-------\n')

        time.sleep(30)


main()
