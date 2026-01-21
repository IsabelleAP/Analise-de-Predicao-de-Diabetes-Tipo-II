# Analise-de-Predicao-de-Diabetes-Tipo-II
O projeto foi desenvolvido como parte de uma disciplina de Inteligência Artificial no programa de Pós-Graduação da UFABC. O meu grupo utilizou um conjunto de dados de livre escolha, baseando-se em algo que todas do grupo pudesse conseguir trabalhar, para aplicar análise exploratória, clusterização e modelos supervisionados (Redes Neurais, Árvore de Decisão e Random Forest) com o objetivo de prever Diabetes Tipo II. Optou-se por trabalhar apenas com as classes "diabetes" e "não diabetes", considerando que o conjunto de dados não fornecia informações suficientes para diferenciar pré-diabetes, como dados de exames clínicos, por exemplo. Em estudos com maior tempo, poderia vir a ser estudado uma ampliação de atributos ou mudança de dados que permitissem a inclusão dessa terceira classe.

**Participantes**: Giselda Ferreira, Isabelle Pereira, Layla Rodrigues e Yolanda Marcello.

## Objetivo
Este trabalho se trata sobre a predição de Diabetes Mellitus tipo 2, em que foi utilizada a base de dados “Diabetes Health Indicators Dataset” para extração de dados para  o estudo de diferentes fatores na predição de diabetes.

### Resultados
A partir das métricas obtidas pelos diferentes algoritmos e estratégias de validação, foram levantadas hipóteses sobre o comportamento dos modelos. Um dos principais resultados foi o baixo número de falsos negativos (aspecto crítico em predições de DM2). Além disso, a análise de importância dos atributos indicou que os fatores mais relevantes para o modelo foram: presença ou ausência de pressãp arterial alta, autopercepção do estado de saúde, índice de massa corporal e idade.

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
