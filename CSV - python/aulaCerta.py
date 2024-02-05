import  csv 
import json

with open ('./cliente.csv','r') as arquivoCsv:
    clientes = []
    leitor = csv.DictReader(arquivoCsv , delimiter = ";")
    for linha in leitor:
       cliente = (dict(linha))
       clientes.append(cliente)
    print(clientes)
        
with open ('./cliente.json', 'w') as arquivoJson:
 json.dump(clientes, arquivoJson, indent=4)
        







    



