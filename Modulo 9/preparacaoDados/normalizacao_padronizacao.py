import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())
print(df.tail())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])  # Normaliza os valores para uma escala entre 0 e 1
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))  # Se quiser mudar o tamanho da escala, esse é o comando
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()  # Nessa escala, os valores tenderão à média 0 e desvio padrão 1
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()  # Essa escala usa a mediana e o IQR. Útil para remover outliers.
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

# Nessa forma de fazer o print, com string literal, é possível alterar onde temos o 4f("Float com 4 casas decimais".)
# É possível usar também strings (str), inteiros (int), etc.
print('MinMaxScaler (De 0 a 1):')
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.4f} Desvio Padrão: {:.4f}".format((df['idadeMinMaxScaler']).min(),
                                                                                   df['idadeMinMaxScaler'].max(),
                                                                                   df['idadeMinMaxScaler'].mean(),
                                                                                   df['idadeMinMaxScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Média: {:.4f} Desvio Padrão: {:.4f}".format((df['salarioMinMaxScaler']).min(),
                                                                                     df['salarioMinMaxScaler'].max(),
                                                                                     df['salarioMinMaxScaler'].mean(),
                                                                                     df['salarioMinMaxScaler'].std()))
# Aqui podemos tirar como conclusão que como a média dos salários ficou mais próxima do 0 que de 1,
# temos um número maior de salários baixos do que salários altos.

print('\nMinMaxScaler (De -1 a 1):')
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.4f} Desvio Padrão: {:.4f}".format((df['idadeMinMaxScaler_mm']).min(),
                                                                                   df['idadeMinMaxScaler_mm'].max(),
                                                                                   df['idadeMinMaxScaler_mm'].mean(),
                                                                                   df['idadeMinMaxScaler_mm'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Média: {:.4f} Desvio Padrão: {:.4f}".format((df['salarioMinMaxScaler_mm']).min(),
                                                                                     df['salarioMinMaxScaler_mm'].max(),
                                                                                     df['salarioMinMaxScaler_mm'].mean(),
                                                                                     df['salarioMinMaxScaler_mm'].std()))
# Esse é útil para quando temos que tratar de valores positivos e negativos. E a média central se torna o 0.
# Ambas as MinMax são utilizadas quando queremos analisar a distância entre os números.
# A normalização é importante para poder comparar dados diferentes, como nesse caso.
# Ao colocá-los em uma mesma escala, a comparação se torna possível.


print('\nStandardScaler (Ajuste a média  a 0 e desvio padrão a 1):')
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.18f} Desvio Padrão: {:.4f}".format((df['idadeStandardScaler']).min(),
                                                                                    df['idadeStandardScaler'].max(),
                                                                                    df['idadeStandardScaler'].mean(),
                                                                                    df['idadeStandardScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Média: {:.18f} Desvio Padrão: {:.4f}".format((df['salarioStandardScaler']).min(),
                                                                                      df['salarioStandardScaler'].max(),
                                                                                      df['salarioStandardScaler'].mean(),
                                                                                      df['salarioStandardScaler'].std()))
# Aqui analisamos o min e o max. Vemos que o intervalo entre o min e o max da idade é menor do que do salário.
# Ou seja, os valores de idade variam menos do que os de salário.
# Essa informação pode ser usada em algoritmos de Machine Learning em que você precisa da distribuição dos valores

print('\nRobustScaler (Ajuste a mediana e IQR):')
print("Idade - Min: {:.4f} Max: {:.4f} Média: {:.4f} Desvio Padrão: {:.4f}".format((df['idadeRobustScaler']).min(),
                                                                                   df['idadeRobustScaler'].max(),
                                                                                   df['idadeRobustScaler'].mean(),
                                                                                   df['idadeRobustScaler'].std()))
print("Salário - Min: {:.4f} Max: {:.4f} Média: {:.4f} Desvio Padrão: {:.4f}".format((df['salarioRobustScaler']).min(),
                                                                                     df['salarioRobustScaler'].max(),
                                                                                     df['salarioRobustScaler'].mean(),
                                                                                     df['salarioRobustScaler'].std()))
# Nesse metodo, o intervalo é menor porque ele desconsidera os outliers. É uma boa opção quando temos muitos outliers.
