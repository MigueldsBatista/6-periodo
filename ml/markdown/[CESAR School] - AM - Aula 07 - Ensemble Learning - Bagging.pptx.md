![image 1]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile4.png)

# Aprendizado de Máquina

###### Ensemble Learning

2026 | Fevereiro

### Vox populi, vox Dei

## Ensembles ou comitês

- ● Durante o treinamento de um comitê, o objetivo é construir uma coleção de preditores que, juntos, produzem uma predição melhor do que cada um separadamente
- ● A fronteira de decisão correspondente a um modelo de comitê pode ser aproximada por meio de uma combinação apropriada dos diferentes preditores (classiﬁcadores ou regressores)


![image 5]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile5.png)

## Ensemble: Superfície de decisão

![image 6]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile6.png)

## Ensemble: Funcionamento

- ● Modelos diferentes são treinados em conjuntos de dados variados
- ● As previsões dos modelos são combinadas (por votação, média, entre outros) para obter uma resposta ﬁnal
- ● A combinação ajuda a mitigar fraquezas de cada modelo isolado, criando uma solução mais conﬁável
- ● Destacam-se dois tipos clássicos de comitês: Bagging e Boosting


##### ● Bagging: é um comitê que treina (ﬁt) os modelos em subconjuntosaleatórios do conjunto de dados original e, em seguida, agrega suasprevisões individuais por votação ou por média para formar uma previsãoﬁnal

![image 7]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile7.png)

- ● O Bagging pode normalmente ser usado como uma forma de reduzir a variância de um estimador (por exemplo, uma árvore de decisão), introduzindo aleatoriedade por meio do procedimento na construção dos datasets
- ● Cria um efeito de suavização nas previsões, onde erros extremos de modelos individuais são compensados pelos acertos de outros
- ● Para a classiﬁcação, aplica-se uma votação entre as predições dos modelos individuais. Para regressão, usa-se a média


![image 8]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile8.png)

- ● Random Forest é um classiﬁcador que é um um caso particular de bagging. Os subconjunto de dados são gerados a partir de:

- ○ bootstrap do conjunto de treinamento (com reposição) e
- ○ subconjuntos aleatórios de atributos (features)


- ● Devido à seleção aleatória de atributos, as árvores são mais independentes (i.e., diferentes) umas das outras quando comparado ao bagging
- ● Importante: A seleção aleatória de features aparece no Random Forest, não no bootstrapping


## Prática

- ● Leia o conjunto de dados Iris
- ● Deﬁna os conjuntos de treino e teste de forma estratiﬁcada
- ● Avalie variações de ensembles (voting)
- ● Avalie variações para o Random Forest


## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

###### ○ Capítulo 7

![image 9]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile9.png)

![image 10]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile10.png)

#### Diego Bezerra

![image 11]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile11.png)

dfb2@cesar.school in/diegodefb

![image 12]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile12.png)

![image 13]([CESAR School] - AM - Aula 07 - Ensemble Learning - Bagging.pptx_images/imageFile13.png)

