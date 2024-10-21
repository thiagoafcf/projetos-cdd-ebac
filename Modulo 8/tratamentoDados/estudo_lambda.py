import pandas as pd


# Função para calcular o cubo de um número
def eleva_cubo(x):
    return x ** 3


# Expressão lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3  # "Recebe um valor de x. Vai com esse valor tal expressão simples"

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]})

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_lambda'] = df['numeros'].apply(lambda x: x ** 3)
print(df)
