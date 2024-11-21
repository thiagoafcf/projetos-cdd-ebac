import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Transformação logarítmica
# A transformação logarítmica é usada para reduzir a influência de discrepâncias extremas em dados numéricos.
# Ela é especialmente útil quando há uma grande variação entre os valores, pois diminui a diferença entre eles.
# Interessante para evitar outliers e cadastros errados.
df['salario_log'] = np.log1p(df['salario'])  # log1p é usado para evitar problemas com valores zero

print("\nDataFrame após transformação logarítmica no 'salario': \n ", df.head())

# Transformação Box-Cox
# Essa técnica ajusta os dados a uma distribuição normal,
# eliminando outliers e transformando os dados para que sigam uma distribuição mais próxima da normalidade.
# A transformação Box-Cox requer ajustes para dados negativos, como a adição de constantes.
# A transformação Box-Cox é aplicada em dados que não estão normalizados para transformá-los em
# uma distribuição normal.
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)  # O + 1 é para não termos valores negativos.

print("\nDataFrame após transformação Box-Cox no 'salario': \n ", df.head())

# Codificação de Frequência para 'estado'
# Utilizada quando queremos misturar campos
# Essa técnica transforma variáveis categóricas em números com base na frequência de suas ocorrências.
# É uma boa opção para atribuir valores numéricos a categorias de forma proporcional
# à sua relevância no conjunto de dados.
estado_freq = df['estado'].value_counts() / len(df)  # .value_counts() conta quantos valores únicos tem
df['estado_freq'] = df['estado'].map(estado_freq)

print("\nDataFrame após codificação de frequência para 'estado': \n ", df.head())

# Interações
# Uma forma de gerar prioridades no seu algoritmo
# Essa técnica cria novas variáveis combinando duas ou mais variáveis existentes. Ela é útil para identificar
# interações entre variáveis que podem não ser evidentes ao analisá-las separadamente,
# e pode ajudar a melhorar a performance dos modelos ao incorporar novas informações ao dataset.
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']

print("\nDataFrame após criação da interação entre 'idade' e 'numero_filhos': \n ", df.head())
