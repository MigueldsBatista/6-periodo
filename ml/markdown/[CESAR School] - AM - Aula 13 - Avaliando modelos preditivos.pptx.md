![image 1]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile4.png)

# Aprendizado de Máquina

###### Avaliando modelos preditivos

2026 | Março

### A Ilusão do Placar: Por que 99% de acerto pode ser um desastre no mundo real?

- ● Permite visualizar os erros de classiﬁcação do modelo durante os testes
- ● Possível veriﬁcar se o modelo tende a favorecer uma classe especíﬁca e quais ele tem mais problemas para classiﬁcar


quais ele tem mais problemas para classiﬁcar

- ○ Verdadeiro Positivo: Quando o modelo classiﬁca corretamente a classe Positiva como Positiva
- ○ Verdadeiro Negativo: Quando o modelo classiﬁca corretamente a classe Negativa como Negativa


quais ele tem mais problemas para classiﬁcar

- ○ Falso Positivo: Quando o modelo classiﬁca incorretamente a classe Negativa como Positiva

■ O alarme toca, mas não há fogo. (Custo: Irritação e perda de tempo)

- ○ Falso Negativo: Quando classiﬁca incorretamente a classe Positiva como Negativa


■ Há fogo, mas o alarme não toca. (Custo: Desastre total)

![image 5]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile5.png)

## Matriz de confusão: implementação

![image 6]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile6.png)

|from sklearn.metrics import confusion_matrix from sklearn.metrics import ConfusionMatrixDisplay<br><br>cm = confusion_matrix(y_val, y_val_predicted) disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[‘bad’, ‘good’])|
|---|


- ● Com acurácia em torno de 71%


- ○ Boa parte dos exemplos são da classe good, fazendo com que o modelo chute exemplos bad para a mesma classe
- ○ O que pode ter causado?


![image 7]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile7.png)

- ● Com acurácia em torno de 96,31%


- ○ Na base de dados breast cancer os resultados são bem melhores e o modelo parece conseguir classiﬁcar muito bem as classes
- ○ O que pode ter causado?


![image 8]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile8.png)

### Acurácia: A métrica que mais engana noob.

- ● A acurácia da classiﬁcação é a razão entre o número de acertos e o total de previsões feitas


○ Porcentagem de acertos do modelo

![image 9]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile9.png)

| |Previsto Positivo|Previsto Negativo|
|---|---|---|
|Real Positivo|40|10|
|Real Negativo|20|30|


- ● Identiﬁque os valores de TP, FP, TN, FN.
- ● Explique o impacto de ter muitos falsos positivos neste contexto


![image 10]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile10.png)

##### ● Não é uma boa métrica em conjuntos de dados desbalanceados

○ Ex.: Se tivermos um modelo com 700 exemplos de teste, sendo 679 para classe A e 21 para classe B, o resultado seria 97% mesmo que erre todas da classe B

## Precisão

##### ● Avalia o quão preciso é o modelo com verdadeiros positivos em relação a

##### falsos positivos

- ○ Boa métrica para avaliar quando os falsos positivos são perigosos para a solução
- ○ Ex.: Filtro de SPAM. É melhor um spam chegar na caixa de entrada (Falso Negativo) do que um e-mail importante do chefe ir para o lixo (Falso Positivo).
- ○ Precisão permite analisar: Qual a conﬁança de que 'Sim' é realmente 'Sim'?


![image 11]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile11.png)

## Recall

##### ● Recall (ou sensibilidade) avalia a capacidade do modelo de identiﬁcar os

##### verdadeiros positivos

- ○ Falsos negativos diminuem o recall e podemos priorizar essa métrica quando falsos negativos geram um impacto grande na solução
- ○ Ex.: Diagnóstico de Câncer ou Fraude Bancária. Você prefere investigar um alarme falso (FP) do que deixar um paciente doente ir para casa sem tratameto (FN)


![image 12]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile12.png)

## Especiﬁcidade

- ● Especiﬁcidade avalia a capacidade do modelo de identiﬁcar corretamente os Verdadeiros Negativos
- ● O princípio é que é melhor soltar um culpado (Falso Negativo) do que condenar um inocente (Falso Positivo)
- ● Modelo "cético": ele só marca como positivo se tiver muita certeza, para não rotular erroneamente quem é "saudável" ou "inocente"


![image 13]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile13.png)

## Especiﬁcidade vs Sensibilidade

###### ● Recall (Sensibilidade)

○ É o caçador e não quer deixar passar nenhum positivo

###### ● Especiﬁcidade

○ É o juri que não deseja condenar nenhum inocente (negativo) por engano

- ● Avalia precisão e recall, permitindo encontrar um equilíbrio entre elas


##### ○ Quando falsos positivos e falsos negativos são igualmente importantes

![image 14]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile14.png)

- ● Avalia precisão e recall, permitindo encontrar um equilíbrio entre elas


##### ○ Quando falsos positivos e falsos negativos são igualmente importantes

![image 15]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile15.png)

## E em casos multiclasses?

- ● A acurácia é a soma da diagonal principal (total de acertos) dividida pelo total de amostras
- ● Para calcular a Precisão e o Recall de cada classe, isolamos uma por uma como sendo a classe positiva. Ex:


- ○ Recall Macro: É a média aritmética simples dos recalls de cada classe
- ○ Recall Micro: Agrega todos os acertos globais


![image 16]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile16.png)

## Exercício

- ● Um determinado modelo de um sistema de previsão do tempo, apresentou o desempenho descrito pela matriz de confusão.


○ Calcule a acurácia, precisão, recall e F1-score do modelo

![image 17]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile17.png)

Predito

| |Choveu|Não-choveu|
|---|---|---|
|Choveu|40|15|
|Não-choveu|10|35|


![image 18]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile18.png)

Real

![image 19]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile19.png)

![image 20]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile20.png)

- ● A Curva ROC (Receiver Operating Characteristic) avalia o desempenho do modelo em todos os limiares (thresholds) de classiﬁcação possíveis
- ● Trade-off entre a Sensibilidade e a Taxa de Falsos Positivos (1−Especiﬁcidade)


- ○ Ajuste de um Detector de Metais. Se aumentar a sensibilidade para garantir que nenhuma arma passe (Recall alto), o alarme tocará para chaves e ﬁvelas de cinto (Falso Positivo alto/Especiﬁcidade baixa)
- ○ A curva ROC mostra exatamente esse cabo de guerra entre as métricas (sensibilidade) (1-especiﬁcidade)


![image 21]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile21.png)

![image 22]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile22.png)

![image 23]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile23.png)

![image 24]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile24.png)

(sensibilidade)

![image 25]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile25.png)

(1-especiﬁcidade)

|Cliente|Real (Classe)|Probabilidade da Árvore (Score)|
|---|---|---|
|1|Sim|0.90 (Folha A: 90% são 'Sim')|
|2|Sim|0.80 (Folha B: 80% são 'Sim')|
|3|Não|0.70 (Folha C: 70% são 'Sim')|
|4|Sim|0.40 (Folha D: 40% são 'Sim')|
|5|Não|0.20 (Folha E: 20% são 'Sim')|
|6|Não|0.10 (Folha F: 10% são 'Sim')|


- ● Imagine que sua árvore classiﬁcou 6 clientes (se vão cancelar ou não a assinatura)
- ● Em vez de olhar apenas o "Sim/Não", olhamos a probabilidade (score) da folha


|Cliente|Real (Classe)|Probabilidade da Árvore (Score)|
|---|---|---|
|1|Sim|0.90 (Folha A: 90% são 'Sim')|
|2|Sim|0.80 (Folha B: 80% são 'Sim')|
|3|Não|0.70 (Folha C: 70% são 'Sim')|
|4|Sim|0.40 (Folha D: 40% são 'Sim')|
|5|Não|0.20 (Folha E: 20% são 'Sim')|
|6|Não|0.10 (Folha F: 10% são 'Sim')|


###### ● Para cada probabilidade, podemosdeﬁnir limiares

- ○ Ponto 1 (Limiar > 0.85)
- ○ Ponto 2 (Limiar > 0.50)
- ○ Ponto 3 (Limiar > 0.15)


###### ● Posso usar mais?

|Cliente|Real (Classe)|Probabilidade da Árvore (Score)|
|---|---|---|
|1|Sim|0.90 (Folha A: 90% são 'Sim')|
|2|Sim|0.80 (Folha B: 80% são 'Sim')|
|3|Não|0.70 (Folha C: 70% são 'Sim')|
|4|Sim|0.40 (Folha D: 40% são 'Sim')|
|5|Não|0.20 (Folha E: 20% são 'Sim')|
|6|Não|0.10 (Folha F: 10% são 'Sim')|


- ● Calcular TPR e FPR para cada Ponto

- ○ Ponto 1 (Limiar > 0.85): Só o Cliente 1 é "Sim"
- ○ VP = 1, FN = 2, FP = 0, VN = 3
- ○ TPR (Recall) = 1 + 21 = 0,33
- ○ FPR (1−Esp.) = 0 + 30 = 0,00.
- ○ Coordenada: (0.00, 0.33)


- ● Ponto 2 (Limiar > 0.50)?
- ● Ponto 3 (Limiar > 0.15)?


- ● Eixo X (FPR): O quanto estamos "mentindo" (Falsos Positivos)
- ● Eixo Y (TPR): O quanto estamos "achando" (Verdadeiros Positivos)


- ● Eixo X (FPR): O quanto estamos "mentindo" (Falsos Positivos)
- ● Eixo Y (TPR): O quanto estamos "achando" (Verdadeiros Positivos)


![image 26]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile26.png)

![image 27]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile27.png)

## AUC

- ● AUC (Area Under the Curve) = área sob a curva ROC
- ● Mede a área total sob a curva ROC, resumindo a performance do modelo em um único número de 0 a 1


|AUC|Qualidade|
|---|---|
|0.9 – 1.0|Excelente|
|0.8 – 0.9|Muito bom|
|0.7 – 0.8|Ok|
|0.5|Aleatório|


## Calculando AUC

![image 28]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile28.png)

![image 29]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile29.png)

### Calma, calma… não criemos pânico. Tem uma forma mais fácil de calcular. Explico na próxima aula.

Vai que cai na prova.

|Cliente|Real|Previsto|
|---|---|---|
|1|Sim|Sim|
|2|Sim|Não|
|3|Não|Não|
|4|Sim|Sim|
|5|Não|Sim|
|6|Não|Não|
|7|Não|Não|
|8|Sim|Não|
|9|Sim|Sim|
|10|Não|Não|


## Exercício

- ● Um classiﬁcador foi treinado para prever se um cliente irá cancelar a assinatura (Sim ou Não). Foram avaliados 10 clientes com os seguintes resultados.
- ● Monte a matriz de confusão (2x2).
- ● Calcule acurácia, precisão, recall e F1-score.


![image 30]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile30.png)

![image 31]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile31.png)

![image 32]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile32.png)

![image 33]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile33.png)

|Amostra|Real|Previsto|
|---|---|---|
|1|Maçã|Maçã|
|2|Banana|Banana|
|3|Laranja|Banana|
|4|Maçã|Laranja|
|5|Laranja|Laranja|
|6|Banana|Maçã|
|7|Maçã|Maçã|
|8|Laranja|Banana|
|9|Banana|Banana|
|10|Maçã|Maçã|
|11|Laranja|Laranja|
|12|Banana|Laranja|


## Exercício

- ● Um modelo classiﬁca frutas em Maçã, Banana ou Laranja. Os resultados para 12 amostras são apresentados na tabela.
- ● Construa a matriz de confusão (3x3).
- ● Calcule a acurácia geral.
- ● Compare o recall macro e o recall micro.


●

![image 34]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile34.png)

![image 35]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile35.png)

![image 36]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile36.png)

![image 37]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile37.png)

## Exercício: Wine dataset

###### ● A partir dos resultados obtidos com o kNN, apresente:

- ○ Matriz de confusão
- ○ Acurácia, precisão, sensibilidade e f1-score.


![image 38]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile38.png)

Predito

![image 39]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile39.png)

| |Postivio|Negativo|
|---|---|---|
|Positivo|VP|FN|
|Negativo|FP|VN|


![image 40]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile40.png)

Real

![image 41]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile41.png)

## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

###### ○ Capítulo 3

![image 42]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile42.png)

![image 43]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile43.png)

#### Diego Bezerra

![image 44]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile44.png)

dfb2@cesar.school in/diegodefb

![image 45]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile45.png)

![image 46]([CESAR School] - AM - Aula 13 - Avaliando modelos preditivos.pptx_images/imageFile46.png)

