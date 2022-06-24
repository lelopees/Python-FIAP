import json

dicionario = {
    "CHAVES": ["CHAVE DO 0", "14/04/2017", "RECEP_01"],
    "QUICO": ["QUICO FLORES", "24/04/2017", "RAIOX_01"],
    "FLORINDA": ["DONA FLORINDA", "10/04/2017", "RECEP_03"]
}

print(dicionario)

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)

