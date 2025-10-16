# Analise-de-Predicao-de-Diabetes-Tipo-II
Este repositório contém um projeto de ciência de dados sobre predição de diabetes tipo II. Foram utilizadas técnicas de análise exploratória, clusterização e aprendizado de máquina supervisionado (Redes Neurais, Árvore de decisão e Random Forest).

## Objetivo
Este trabalho trata da Diabetes Mellitus tipo 2, em que foi utilizada a base de dados “Diabetes Health Indicators Dataset” para extração de dados  para  o estudo de diferentes fatores na predição de diabetes. A análise foi realizada utilizando bibliotecas de Python, como Pandas, Matplotlib, Scikit-learn, entre outras.

## Conjunto de Dados
O conjunto de dados utilizado neste relatório é derivado do Behavioral Risk Factor Surveillance System (BRFSS), pesquisa nacional de saúde conduzida anualmente pelo Centers for Disease Control and Prevention (CDC) nos Estados Unidos.
- **Fonte dos dados**: [CDC Diabetes](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators)
- **Dados**: Arquivo CSV (0 - não diabetes e 1 - diabetes)

## Metodologia

1. **Análise Exploratória de Dados (EDA)**:
   - Limpeza e transformação dos dados.
   - Balanceamento das classes.
   - Separação das classes.

2. **Modelos**:
   - Clusterização utilizando o Kmeans.
   - Redes Neurais (hold-out, cross-validation e random subsampling).
   - Árvore de decisão (hold-out, cross-validation e random subsampling).
   - Random Forest (hold-out, cross-validation e random subsampling).

## Tecnologias e Bibliotecas Utilizadas
- **Linguagem**: Python
- **Bibliotecas**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Tensorflow, 
- **Ferramentas**: Jupyter Notebook
