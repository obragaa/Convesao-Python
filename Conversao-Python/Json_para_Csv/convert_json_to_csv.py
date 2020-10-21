import json, csv

csvFilePath = "json_convertido.csv" # Nome do nosso arquivo csv
jsonFilePath = "/Users/Edgar/Desktop/Conversão/Json_para_Csv/shopping.json" # Local do nosso arquivo Json segundo os diretórios da minha máquina

with open (jsonFilePath) as file: # Buscando nosso arquivo Json
    data = json.load(file)

with open(csvFilePath, "w") as file: # Conversão + criação do arquivo já convertido
    csv_arquivo = csv.writer(file)
    csv_arquivo.writerow(["id", "name", "description", "quantity", "value"])
    for item in data["order"]:
        csv_arquivo.writerow([item["id"], item["name"], item["description"], item["quantity"], item["value"]])
        