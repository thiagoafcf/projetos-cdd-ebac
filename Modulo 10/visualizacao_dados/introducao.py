import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('clientes-v3-tratados.csv')
print(df.head().to_string())

# Histograma
plt.hist(df['salario'])
plt.show()

# Histograma - Parâmetros
plt.figure(figsize=(10, 6))
plt.hist(df['salario'], bins=100, color='green', alpha=0.8)
# bins é o intervalo das colunas no eixo x.
# Aqui cada coluna está mostrando a quantidade de salários em subdivisões a cada 100.
# alpha é a transparência.
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
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)  # 2 Linha, 2 Colunas, 3º Gráfico
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Salário e Anos de experiência')

plt.tight_layout()  # Ajustar espaçamentos
plt.show()
