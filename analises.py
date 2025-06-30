import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

df = pd.read_csv('wdbc.data', header=None)
df

colunas = [
    'ID', 'Diagnosis',
    'radius1', 'texture1', 'perimeter1', 'area1', 'smoothness1', 'compactness1',
    'concavity1', 'concave_points1', 'symmetry1', 'fractal_dimension1',
    'radius2', 'texture2', 'perimeter2', 'area2', 'smoothness2', 'compactness2',
    'concavity2', 'concave_points2', 'symmetry2', 'fractal_dimension2',
    'radius3', 'texture3', 'perimeter3', 'area3', 'smoothness3', 'compactness3',
    'concavity3', 'concave_points3', 'symmetry3', 'fractal_dimension3'
]

df.columns = colunas

df = pd.read_csv('wdbc.data', header=None, names=colunas)
df

df.isnull().sum()

df.describe()

###BOXPLOT DE TODAS AS COLUNAS
#fig, ax = plt.subplots(figsize=(8, 6))

#ax.boxplot(df[''], patch_artist=True, boxprops=dict(facecolor='green'))
#ax.set_title('Boxplot')

#ax.grid(False)

#plt.tight_layout()

#plt.show()



###VERIFICAR SE TEM DADOS DUPLICADOS
### DELETAR OS DADOS DUPLICADOS
#df = df.drop_duplicates()