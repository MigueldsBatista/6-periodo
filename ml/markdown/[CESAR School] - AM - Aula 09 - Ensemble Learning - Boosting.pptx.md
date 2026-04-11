![image 1]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile4.png)

# Aprendizado de Máquina

###### Boosting

2026 | Março

### Boosting = aprender com os erros anteriores.

![image 5]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile5.png)

### Boosting transforma vários modelos fracos em um modelo forte.

- ● Técnica de comitê em que um classiﬁcador base aprende com os erros anteriores dos classiﬁcadores bases
- ● Um strong learner é melhor em regiões (do espaço de atributos) nas quais os modelos anteriormente adicionados ao comitê erraram (weak learner).
- ● A geração de um novo modelo base depende do resultado do anterior (sequencial)
- ● Existem vários exemplos de Boosting


○ AdaBoost, XGBoost, Gradient Boosting

## Weak e strong learner

- ● Um aprendiz fraco (weak learner) é deﬁnido como um classiﬁcador que é ligeiramente correlacionado com a classiﬁcação verdadeira

○ Acurácia ligeiramente maior que 50% em problemas de classiﬁcação binária

- ● Um aprendiz forte (strong learner) é um classiﬁcador que possui uma precisão signiﬁcativamente maior


![image 6]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile6.png)

## Limitações

- ○ Custo computacional alto, especialmente com muitos hiperparâmetros ou valores
- ○ Pode testar combinações irrelevantes, que não fazem sentido (ex: max_depth=10 com n_estimators=10 pode ser subótimo)


## MNIST database of handwritten digits

![image 7]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile7.png)

- ● 70k imagens (60k treino/10k teste)

- ○ Dígitos manuscritos (0-9) em tons de cinza
- ○ São normalizados e centralizados
- ○ Medindo pixels 28x28


- ● Tarefa: Dada uma imagem de um dígito, prever corretamente qual número ela representa


## Fashion-MNIST

![image 8]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile8.png)

##### ● 70k imagens (60k treino/10k teste)

- ○ Imagens em escala de cinza
- ○ Dimensão: 28 × 28 pixels (784 atributos)
- ○ Dados normalizados e centralizados


##### ● Tarefa: Classiﬁcar cada imagem em uma categoria de vestuário (ex: camiseta, sapato, bolsa, etc.)

## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

###### ○ Capítulos 10, 11 e 14

![image 9]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile9.png)

![image 10]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile10.png)

#### Diego Bezerra

![image 11]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile11.png)

dfb2@cesar.school in/diegodefb

![image 12]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile12.png)

![image 13]([CESAR School] - AM - Aula 09 - Ensemble Learning - Boosting.pptx_images/imageFile13.png)

