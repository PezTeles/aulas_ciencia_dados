import pandas as pd #biblioteca de tratamento de dados
import matplotlib.pyplot as plt #produção de elementos visuais como graficos

base = pd.read_csv('trees.csv')

#gerando bxplot
#patch_artist = TRue preenche, showfliers outliers
# plt.boxplot(base.Volume, vert = False, showfliers = False, notch = True, patch_artist = True)
# plt.title('Árvores')
# plt.xlabel('Volume')
# # plt.show()


#dados por linha
# plt.boxplot(base)
# plt.title('Árvores')
# plt.xlabel('Dados')
# plt.show()

#3 boxplots com dados diferentes cada
plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)
plt.title('Árvores')
plt.xlabel('Dados')
plt.show()