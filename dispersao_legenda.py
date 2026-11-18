import pandas as pd #biblioteca de tratamento de dados
import matplotlib.pyplot as plt #produção de elementos visuais como graficos

base = pd.read_csv('co2.csv')
# print(base.head())

x = base.conc
y = base.uptake


unicos = list(set(base.Treatment))
# print(unicos)

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])

plt.legend(loc = 'lower right')    
plt.show()


