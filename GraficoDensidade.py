import pandas as pd #biblioteca de tratamento de dados
import seaborn as sns #criação de gráficos estatísticos com uma linha de densidade
import matplotlib.pyplot as plt #produção de elementos visuais como graficos

base = pd.read_csv('trees.csv')

plt.hist(base.iloc[:,1], bins = 6 )
#plt.show()

#gera um histograma comum
sns.histplot(base.iloc[:,1], kde = False, bins = 6, color ='blue').set(title='Árvores')
#plt.show()

#gera apenas a linha de densidade
sns.kdeplot(base.iloc[:,1], color='blue').set(title='Árvores')
#plt.show()

#kde = True, gera o histograma com uma linha de densidade
sns.histplot(base.iloc[:,1], kde = True, bins = 6, color ='blue').set(title='Árvores')
plt.show()