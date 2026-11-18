import pandas as pd #biblioteca de tratamento de dados
import numpy as np #biblioteca cientifica
import matplotlib.pyplot as plt #produção de elementos visuais como graficos

base = pd.read_csv('trees.csv')
#o .shape mostra o tamanho da tabela que estamos tratando
#print(base.shape)

#mostra as primeiros dados da tabela
#print(base.head) 

h = np.histogram(base.iloc[:,1], bins = 6)
#print(h)

plt.hist(base.iloc[:,1], bins = 6)
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')

plt.show()