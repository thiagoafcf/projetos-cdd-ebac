import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico \n', df_filtro_basico[['nome', 'idade']])

# identificar outliers com Z-score
z_scores = stats.zscore(df['idade'].dropna())  # Se os dados já forem tratados, não tem necessidade do dropna
# Somente a linha de cima já faria o código funcionar, mas para visualização, foram feitas as linhas seguintes
outliers_z = df[z_scores >= 3]
print('\nOutliers pelo Z-score:\n', outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]  # 3 é uma primeira opção-padrão para se testar

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR
# 1.5 também é um valor padrão para exploração básica, mas pode alterar, assim como os valores das linhas 22 e 23

print('\nLimites IQR: ', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
# Não esquecer de colocar parênteses em cada condição quando se usa operador condicional
print('\nOutliers pelo IQR: \n', outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

limite_baixo = 1
limite_alto = 100
# Como estamos trabalhando com idade, às vezes pode ser melhor já definir valores com os quais queremos trabalhar
df = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'endereço inválido' if len(x.split('\n')) < 3 else x)
print('\nQuantidade de registros com endereço inválido:', (df['endereco'] == 'endereço inválido').sum())

# Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome Inválido' if isinstance(x, str) and len(x) > 50 else x)
# isinstance: "Se o campo x for string" se não for, provavelmente é campo nulo.
print('\nQuantidade de registros com nomes grandes:', (df['nome'] == 'Nome Inválido').sum())
print('\nQuantidade de registros com nomes não informados:', (df['nome'] == 'Não Informado').sum())

print('\nDados com Outliers tratados:\n', df)

# Salvar o DataFrame
df.to_csv('clientes_remove_outliers.csv', index=False)
