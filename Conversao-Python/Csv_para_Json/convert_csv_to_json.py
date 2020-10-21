import json, csv

csvFilePath = "/Users/Edgar/Desktop/Conversão/Csv_para_Json/shopping.csv" # Local do arquivo csv na minha máquina
jsonFilePath = "Csv_Convertido.json" # Nome que virá após solicitarmos nosso arquivo já convertido em Json

data = {} #Conversão
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        ID_csv = csvRow["ID"]
        data[ID_csv] = csvRow


with open(jsonFilePath , "w") as jsonFile: #Criando nosso arquivo Json
    jsonFile.write(json.dumps(data, indent=4))
    
