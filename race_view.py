# pip install kagglehub pandas
import kagglehub
import pandas as pd
import os

# Baixar o dataset e obter o caminho local
dataset_path = kagglehub.dataset_download("jtrotman/formula-1-race-data")

# Listar todos os arquivos disponíveis
print("Arquivos disponíveis no dataset:")
for file in os.listdir(dataset_path):
    print(file)

# Escolher um arquivo para carregar (por exemplo, races.csv)
file_name = "races.csv"  # troque para o arquivo que você quiser
file_path = os.path.join(dataset_path, file_name)

# Carregar com pandas
df = pd.read_csv(file_path)

print("\nPrimeiros registros:")
print(df.head())
