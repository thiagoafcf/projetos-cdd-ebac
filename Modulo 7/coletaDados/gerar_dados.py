import pandas as pd
import random
from faker import Faker

# Define que o Faker vai usar dados BR. Ver na documentação do faker sobre Locales
faker = Faker('pt_BR')

# Cria lista vazia para receber os dados
dados_pessoas = []

# Cria os dados falsos
for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y")
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }
    dados_pessoas.append(pessoa)

# Cria um DataFrame com o pandas com os dados gerados
df_pessoas = pd.DataFrame(dados_pessoas)

# O professor recomenda essa opção para printar o df para apenas um uso
print(df_pessoas.to_string())  # head()  tail()

# Já essa opção ele recomenda se for utilizar o df outras vezes
pd.set_option('display.max_columns', None)  # Número de colunas. Colocando o atributo None, dizemos que não tem limite
pd.set_option('display.max_rows', None)  # Número de linhas
pd.set_option('display.max_colwidth', None)  # Largura da coluna
pd.set_option('display.width', None)  # Largura do display

print(df_pessoas)

# Exporta os dados criados para .csv. Precisa definir o nome do arquivo.
df_pessoas.to_csv('clientes.csv')
