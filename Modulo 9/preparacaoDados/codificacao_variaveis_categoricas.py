# Transformar dados de texto em números é importante para conseguir utilizá-los em algoritmos de IA e Machine Learning
# Com isso também podemos alterar o peso que cada dado pode ter para nossa análise
# ou mesmo fazer operações com outros campos numéricos do DataFrame.


import pandas as pd
from sklearn.preprocessing import LabelEncoder


pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Codificação one-hot para 'estado_civil'
# O .concat está unindo o DataFrame original (df) com o novo DataFrame gerado pelas variáveis dummies,
# adicionando as novas colunas ao final do original.
# O .get_dummies está criando colunas binárias (0 ou 1) para cada categoria única da variável estado_civil
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil',)], axis=1)
print('\nNovo DataFrame após codificação one-hot para "estado_civil":\n', df.head())

# Codificação ordinal para 'nivel_educacao'
# Criamos um dicionário com os valores únicos da coluna em questão e os associamos a um número
# O .map vai buscar na coluna original esses valores, compará-los com o dicionário
# e preencher a coluna nova que estamos criando com os valores referentes.
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)
print('\nDataFrame após codificação ordinal para "nivel_educacao":\n', df.head())

# Transformar 'area_atuacao' em categorias codificadas usando o metodo .cat.codes
# Diferentemente do metodo anterior, aqui não precisamos criar um dicionário.
# Isso é útil quando temos numerosos valores únicos na nossa coluna (não é tanto o caso desse exemplo).
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes
print('\nDataFrame após transformar "area_atuacao" em códigos numéricos:\n', df.head())
# A desvantagem é não saber quais são os valores associados a qual número.
# Seria necessário imprimir uma lista para saber. Pode-se usar o seguinte código:
df['area_atuacao'] = df['area_atuacao'].astype('category')
print("\nAssociações entre os valores e os códigos:")
for codigo, valor in enumerate(df['area_atuacao'].cat.categories):
    print(f"{codigo} -> {valor}")
# Além disso, só funciona com objetos do pandas que já foram transformados previamente em tipo categórico.
# É mais útil quando você precisa de uma conversão mais rápida quando já está trabalhando com pandas.

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em números de 0 a n_classes-1
# É parecido com o anterior, mas pode ser utilizado em Dataframes mesmo fora do pandas, além de arrays e listas,
# sendo, portanto, mais adequado para montar pipelines de machine learning.
# Também pode ser integrado em outras transformações do sklearn.
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])
print('\nNovo DataFrame após aplicar o LabelEncoder em "estado":\n', df.head())
