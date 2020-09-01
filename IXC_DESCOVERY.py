#!/usr/bin/python3
import requests
import json

cont = 0


services = []
interface =[]

header = {
    'User-Agent': '*',
    'Accept': '*'
}
r = requests.post('http://168.228.163.28/teste/login_off.php', headers=header)
dados = (r.json()['registros'])


for i in dados:
    cont += 1
    y = (i['login'])
    services.append(y)

total = cont
cont = 0

print ("{\n\t\"data\":[\n")

for i in services:
 cont +=1
 if cont < total:
     print(json.dumps(({'{#NAME}': i}), indent=4) + ",")
 else:
     print(json.dumps(({'{#NAME}': i}), indent=4))

print("]")
print("}")
