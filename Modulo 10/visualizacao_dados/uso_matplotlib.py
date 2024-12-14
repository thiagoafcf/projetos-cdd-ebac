import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('clientes-v3-tratados.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize=(10, 6))
# Com a linha a seguir é possível plotar os dados do dataframe a partir de uma função do próprio pandas
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
'''
Nesse link são explicados outros tipos de gráfico:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
'''
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)  # Define a rotação das legendas do eixo x
# Mas para poder mostrar o gráfico, inevitavelmente será preciso usar o matplotlib
plt.show()

'''
O código a seguir cria o mesmo tipo de gráfico, mas de maneira diferente. Para funcionar, entretanto, precisamos definir
quem são x e y antes.
'''
x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolaridade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')

# Gráfico de pizza
'''
Gráfico mais utilizado para saber a proporção entre os elementos dentro do todo.
'''
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)  # X e Y estão invertidos em relação ao tipo anterior
# startangle define em qual ângulo o gráfico inicia. Se mudar pra 0, ele começa na horizontal, por exemplo.
plt.title('Distribuição de Nível de Educação')
plt.show()

# Gráfico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
'''
Referência de cmap:
https://matplotlib.org/stable/users/explain/colors/colormaps.html
'''
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()
