![image 1]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile4.png)

# Aprendizado de Máquina

![image 5]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile5.png)

###### Random Forest

2026 | Março

### Enquanto uma árvore decide, a ﬂoresta vota.

## Já sabemos que…

● Bagging: comitê que treina os modelos em subconjuntos aleatórios do conjunto de dados original e, em seguida, agrega suas previsões individuais por votação ou por média

![image 6]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile6.png)

![image 7]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile7.png)

## Random Forest

- ● Random Forest é um caso particular de bagging. Os subconjunto de dados são gerados a partir de:

- ○ bootstrap do conjunto de treinamento (com reposição) e
- ○ subconjuntos aleatórios de atributos (features)


- ● Devido à seleção aleatória de atributos, as árvores são mais independentes umas das outras quando comparado ao bagging
- ● Importante: A seleção aleatória de features aparece no Random Forest!


## Overﬁtting e underﬁtting

- ● Em uma Decision Tree, árvores profundas podem levar ao overﬁtting
- ● No Random Forest, esse risco é reduzido, porque:

- ○ cada árvore vê apenas uma amostra bootstrap dos dados
- ○ cada divisão usa apenas um subconjunto de features
- ○ a previsão ﬁnal é uma agregação de várias árvores


- ● Random Forest é menos sensível a overﬁtting


## Out-of-bag

- ● Os out-of-bag (OOB) são os exemplos que não foram selecionados no bootstrap para treinar um determinado modelo
- ● Funcionam como conjunto de validação do modelo
- ● Cada árvore é treinada com apenas ~67% dos dados, os ~33% restantes funcionam como um conjunto de teste para aquela árvore


- ● Possível estimar quais variáveis mais contribuíram para as decisões do modelo
- ● O algoritmo calcula a importância de cada feature com base na redução de impureza gerada pelas divisões nas árvores da ﬂoresta

- ○ Identiﬁcar quais variáveis mais inﬂuenciam as previsões
- ○ Ajudar na interpretação do modelo
- ○ Apoiar seleção ou redução de features


- ● Mas… alta importância não signiﬁca causalidade, apenas que a variável foi útil para melhorar as divisões das árvores.


![image 8]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile8.png)

##### ● Classiﬁcação de dígitos manuscritos

- ○ 70k imagens (60k treino/10k teste) de dígitos manuscritos (0-9) em tons de cinza
- ○ São normalizados e centralizados
- ○ Medindo pixels 28x28


![image 9]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile9.png)

##### ● Classiﬁcação de peças de roupas

- ○ 70k imagens (60k treino/10k teste) de peças de roupas em tons de cinza
- ○ São normalizados e centralizados
- ○ Medindo pixels 28x28


![image 10]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile10.png)

## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

###### ○ Capítulo 7

![image 11]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile11.png)

![image 12]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile12.png)

#### Diego Bezerra

![image 13]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile13.png)

dfb2@cesar.school in/diegodefb

![image 14]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile14.png)

![image 15]([CESAR School] - AM - Aula 08 - Random Forest.pptx (1)_images/imageFile15.png)

