import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar primeiros registros
print(df.head().to_string())  # Mostra o início do DF
print(df.tail().to_string())  # Mostra o final do DF
# Importante para ver se os dados se mantém coerentes até o final do DF

# Verificar quantidade de linhas e colunas
print('Quantidade: ', df.shape)  # (linhas, volunas)

# Verificar tipos de dados
print('Tipagem:\n', df.dtypes)

# Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())
