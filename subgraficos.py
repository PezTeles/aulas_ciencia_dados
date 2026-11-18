import pandas as pd #biblioteca de tratamento de dados
import matplotlib.pyplot as plt #produção de elementos visuais como graficos

base = pd.read_csv('trees.csv')
# print(base.head())

# #circunferencia com volume
# plt.scatter(base.Girth, base.Volume)
# # plt.show()

# #altura com circunferencia
# plt.scatter(base.Girth, base.Height)
# # plt.show()

# plt.scatter(base.Height, base.Volume, marker = '*')
# # plt.show()

# #histograma de vlume
# plt.hist(base.Volume)
# plt.show()

#imprimindo juntos
#criação de figura onde os gráficos serão posicionados
plt.figure(1)
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume, marker = '*')
plt.subplot(2,2,4)
plt.hist(base.Volume)
plt.show()