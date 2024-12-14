import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('clientes-v3-tratados.csv')
print(df.head(20).to_string())

df_corr = df[['salario', 'idade', 'anos_experiencia', 'numero_filhos']].corr()
# Heatmap de correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de calor da Correlação entre Variáveis')
plt.show()
'''
Esse tipo de gráfico ajuda a visualizarmos quais variáveis têm mais relação entre si e, com isso, focarmos mais em 
utilizar aquelas que têm mais relação na nossa análise e avaliar se compensa usar as que tem baixa relação.
'''

# Já usei
# Countplot
sns.countplot(x='estado_civil', data=df)
plt.title('Distribuição do Estado')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.show()

# Countplot com legenda
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
plt.title('Distribuição do Estado Civil')
plt.xlabel('Estado Civil')
plt.ylabel('Contagem')
plt.legend(title='Nível de Educação')
plt.show()
