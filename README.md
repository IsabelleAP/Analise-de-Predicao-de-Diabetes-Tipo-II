# Analise-de-Predicao-de-Diabetes-Tipo-II
Este repositório contém um projeto de ciência de dados sobre predição de diabetes tipo II. Foram utilizadas técnicas de análise exploratória, clusterização e aprendizado de máquina supervisionado (Redes Neurais, Árvore de decisão e Random Forest). O projeto faz parte de uma disciplina sobre Inteligência Artificial no programa de Pós-Graduação e a escolha do banco de dados foi livre.

**Participantes**: Giselda Ferreira, Isabelle Pereira, Layla Rodrigues e Yolanda Marcello.

## Objetivo
Este trabalho se trata sobre a predição de Diabetes Mellitus tipo 2, em que foi utilizada a base de dados “Diabetes Health Indicators Dataset” para extração de dados para  o estudo de diferentes fatores na predição de diabetes.

## Conjunto de Dados
O conjunto de dados utilizado neste relatório é derivado do "Behavioral Risk Factor Surveillance System (BRFSS)", pesquisa nacional de saúde conduzida anualmente pelo _Centers for Disease Control and Prevention_ _(CDC)_ nos Estados Unidos.
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
- **Bibliotecas**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn e Tensorflow.
- **Ferramentas**: Jupyter Notebook
