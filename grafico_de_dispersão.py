import pandas as pd #biblioteca de tratamento de dados
import numpy as np #biblioteca cientifica
import matplotlib.pyplot as plt #produção de elementos visuais como graficos
import seaborn as sns

base = pd.read_csv('trees.csv')
print(base.head())

#gráfico de dispersão considerando o volume e a dispersão
plt.scatter(x=base.Girth, y=base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Árvores')
plt.xlabel('Circunferência')
plt.ylabel('Volume')
# plt.show

#ggráfico de linha considerando o volume atribuido "girth" - sem marker
plt.plot(base.Girth, base.Volume)
plt.title('Árvores')
plt.xlabel('Circunferência')
plt.ylabel('Volume')
# plt.show()

#gráfico de dispersão com afastamento dos dados usando o método (jitter)
#fit_reg linha de tendência
sns.regplot(x=base.Girth, y=base.Volume, data = base, x_jitter = 0.3, fit_reg = False)
plt.show()