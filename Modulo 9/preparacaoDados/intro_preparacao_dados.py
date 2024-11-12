import pandas as pd


df = pd.read_csv('clientes-v2.csv')
pd.set_option('display.width', None)

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial:')
print(df.info())

print('Análise de dados nulos:\n', df.isnull().sum())
print('% de dados nulos: \n', df.isnull().mean() * 100)
df.dropna(inplace=True)
print('Confirmar a remoção de dados nulos:\n', df.isnull().sum().sum())

print('Análise de dados duplicados:\n', df.duplicated().sum())

print('Análise de dados únicos:\n', df.nunique())
# Essa análise é interessante para identificarmos dados que se repetem menos,
# que podem significar que podem ser identificadores do usuário, ou dados que se repetem pouco
# e podem ser usados para formar categorias.

print('Estatísticas dos dados:\n', df.describe())
# Já dá uma primeira descrição dos dados, nos mostrando média e mediana, quartis, uma ideia da distribuição

# Criamos um novo df para remover os dados que podem ser identificadores de usuários e proteger os dados conforme a lei
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos',
         'estado_civil', 'anos_experiencia', 'area_atuacao']]
print(df.head().to_string())
print(df.tail().to_string())

df.to_csv('clientes-v2-tratados.csv', index=False)
