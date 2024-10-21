import pandas as pd
import random
from faker import Faker


faker = Faker('pt_BR')
Faker.seed(0)


def gerar_dados_nulos_outliers(num_linhas, num_outliers):
    # Cria lista vazia para receber os dados
    dados_pessoas = []

    # Cria os dados falsos
    for _ in range(num_linhas):
        nome = random.choice([faker.name(), None])
        cpf = random.choice([faker.cpf(), 'cpf_invalido', None])
        idade = random.choice([faker.random_int(min=18, max=90), None])
        data = faker.date_of_birth(minimum_age=idade if idade else 18, maximum_age=idade if idade else 90).strftime(
            "%d/%m/%Y")
        endereco = random.choice([faker.address(), 'endereco_invalido', None])
        estado = random.choice([faker.state(), None])
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

    df_pessoas = pd.DataFrame(dados_pessoas)

    for _ in range(num_outliers):
        idade_outlier = random.choice([150, 200])
        df_pessoas.loc[random.randint(0, num_linhas - 1), 'idade'] = idade_outlier

    return df_pessoas


df = gerar_dados_nulos_outliers(5000, 100)

print(df.head())
print(df.tail())

df.to_csv('clientes_bruto.csv', index=None)
