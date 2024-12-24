import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('clientes-v3-tratados.csv')
print(df.head().to_string())

# Histograma
'''
Um tipo de gráfico que representa a distribuição de um conjunto de dados, mostrando a frequência de valores em 
intervalos específicos. É útil para entender a distribuição e a dispersão dos dados.
'''
plt.hist(df['salario'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
'''
bins é o intervalo das colunas no eixo x.
Aqui cada coluna está mostrando a quantidade de salários em subdivisões a cada 100.
alpha é a transparência.
'''
plt.title('Histograma - Distribuição de Salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000, 2000))  # Definição do intervalo no eixo X
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Múltiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)  # Ocupa 2 Linhas, 2 Colunas, 1º Gráfico
# Gráfico de dispersão
plt.scatter(df['salario'], df['salario'])
plt.title('Dispersão - Salário e Salário')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(1, 2, 2)  # Ocupa 1 Linha, 2 Colunas, 2º Gráfico
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883e8', alpha=0.8, s=30)
# Dá para achar a cor hexadecimal online. Em inglês também funciona.
# O s é o tamanho da bolinha
plt.title('Dispersão - Idade e Anos de Experiência')
plt.xlabel('Salario')
plt.ylabel('Anos de Experiência')


# Mapa de Calor
'''
Visualizações que utilizam cores para representar a intensidade dos valores em uma matriz de dados. São eficazes para 
identificar padrões e correlações em grandes conjuntos de dados.
'''
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)  # 2 Linha, 2 Colunas, 3º Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Anos de experiência')

plt.tight_layout()  # Ajustar espaçamentos
plt.show()

'''
Para salvar os gráficos gerados, podemos também usar o seguinte comando:
plt.savefig('nome_do_arquivo.png')

Atentar-se para fazer isso somente após terminar de configurar o gráfico
'''
