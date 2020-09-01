#!/usr/bin/python3
import requests
import json
import sys

header = {
    'User-Agent': '*',
    'Accept': '*'
}
r = requests.post('http://ipdoservidor/teste/login_off.php', headers=header)
dados = (r.json()['registros'])

for i in dados:
    cliente = sys.argv[1]
    if i['login'] == '{}'.format(cliente):
        print(i['ultima_conexao_final'])