'''
A biblioteca Seaborn é baseada no matplotlib, mas tem um foco a mais em estatísticas. Ela possui alguns recursos que
facilitam a visualização e o agrupamento de dados. Oferece uma interface de alto nível para a criação de gráficos
estatísticos atraentes e informativos.
'''

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('clientes-v3-tratados.csv')
print(df.head(20).to_string())

# Gráfico de Dispersão
'''
Interessante para ver outliers e concentração dos dados
'''
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')  # ['scatter', 'hist', 'hex', 'reg', 'resid']
plt.show()

# Gráfico de Densidade
'''
É um tipo de histograma, mas faz a suavização das colunas fazendo uma linha contínua. É mais bonito, porém pode gerar 
alguns erros de interpretação, como potencialmente esconder picos acentuados que seriam visíveis em um histograma 
tradicional. São úteis para identificar padrões e tendências em grandes conjuntos de dados.
'''
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
'''
Faz gráficos de dispersão e histograma relacionando todos os campos que informarmos, exceto campos de texto.
É útil para explorar correlações e distribuições.
Tutorial de como usar as cores
https://seaborn.pydata.org/tutorial/color_palettes.html
'''
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

# Gráfico de Regressão
'''
Usado para entender como está a relação entre os dados. Gráficos que mostram a relação entre variáveis e ajudam a 
visualizar tendências e padrões nos dados. São frequentemente usados para prever valores e identificar correlações.
'''
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico countplot com hue
'''Hue é um agrupamento de dados. Nesse tipo de gráfico, fazemos a contagem de valores de uma variável agrupadas de 
acordo com o hue definido.
Aqui o seaborn tem uma vantagem em relação ao matplotlib. Para fazer um gráfico desse tipo no matplotlib seria 
necessário fazer um tratamento prévio dos dados para agrupá-los para só então fazer o gráfico.
'''
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de clientes')
plt.legend(title='Nível de Educação')  # Pode aplicar legenda em qualquer dos gráficos citados
plt.show()
