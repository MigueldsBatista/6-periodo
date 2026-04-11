![image 1]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile4.png)

# Aprendizado de Máquina

###### Árvores de Decisão

2026 | Fevereiro

### Relembrando...

## Entropia e Ganho de informação

![image 5]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile5.png)

![image 6]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile6.png)

![image 7]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile7.png)

![image 8]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile8.png)

![image 9]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile9.png)

![image 10]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile10.png)

![image 11]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile11.png)

![image 12]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile12.png)

![image 13]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile13.png)

![image 14]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile14.png)

## A melhor decisão

![image 15]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile15.png)

- ● A melhor decisão a ser tomada será a que nos der um valor maior de Ganho de Informação
- ● Aplicar esse algoritmo de forma recursiva, construindo assim as próximas ramiﬁcações da mesma forma sobre os subconjuntos de dados


Não contém Contém

Não Sim Antigo Novo

## Coeﬁciente de Gini

- ● Mede o grau de mistura de classes em um nó
- ● Quanto mais puro (ou homogêneo) for um nó, menor será o Gini
- ● Durante a construção da árvore:


![image 16]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile16.png)

![image 17]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile17.png)

![image 18]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile18.png)

- ○ Calculamos o Gini antes da divisão e depois de cada divisão (ﬁlhos)
- ○ A diferença entre eles permite avaliar a redução da impureza


![image 19]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile19.png)

- ● Calcular a proporção de classes e Gini para o conjunto (todo o conjunto palavras chave), antes da divisão
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém, após a divisão


![image 20]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile20.png)

![image 23]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile23.png)

- ● Calcular a proporção de classes e Gini para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 24]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile24.png)

![image 25]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile25.png)

Antes da divisão…

![image 26]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile26.png)

![image 27]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile27.png)

![image 28]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile28.png)

![image 29]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile29.png)

- ● Calcular a proporção de classes e Gini para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 30]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile30.png)

- ● Calcular a proporção de classes e Gini para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 33]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile33.png)

![image 34]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile34.png)

Entropia vs Gini

###### ● Entropia

- ○ Baseada na teoria da informação
- ○ Mais sensível a mudanças próximas de 0.5


###### ● Gini

- ○ Mede probabilidade de erro de classiﬁcação aleatória
- ○ Computacionalmente mais simples


###### ● Qual usar?

###### ○ Geralmente a árvore construída com Entropia ou Gini é muito parecida

### Se deixarmos a árvore crescer até classiﬁcar 100% corretamente os dados de treino… ela ﬁcou perfeita?

## Overﬁtting e underﬁtting

- ● Em overﬁtting se aprende os padrões reais, mas também aprende o ruído

- ○ Fica excelente no treino, mas ﬁca ruim em dados novos
- ○ Árvores de Decisão são propensas porque…


- ■ Podem dividir inﬁnitamente
- ■ Criam nós até que:


- ● cada folha tenha 1 exemplo
- ● ou todos os exemplos sejam puros


- ● E o underﬁtting?


## Como controlar overﬁtting?

![image 37]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile37.png)

- ● Profundidade máxima (max_depth)
- ● Número mínimo de amostras para dividir (min_samples_split)

○ Impede divisão quando há poucos dados

- ● Número mínimo de amostras na folha (min_samples_leaf)

○ Evita folhas com 1 exemplo só

- ● E o underﬁtting?


### E quando o problema for regressão?

###### ● A árvore escolhe a divisão que minimiza o erro quadrático dentro dos nós

![image 38]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile38.png)

- ○ Cada folha prevê a média dos valores no nó
- ○ Queremos que os valores dentro do nó sejam o mais próximos possível da média


###### ● Isso é equivalente a minimizar a variância

###### x₁ x₂ x₃ y

70 2 5 300 80 3 10 350 120 4 2 600 60 2 20 250

- ● Divide os valores dos atributos
- ● Para cada divisão candidata:

- ○ Divide os dados em dois grupos
- ○ Calcula a média do y em cada grupo
- ○ Calcula o erro quadrático total


- ● A melhor divisão é aquela que:


○ Minimiza o erro quadrático total após a divisão

## Overﬁtting em regressão

#### ● Se deixar crescer muito:

- ○ Cada folha pode conter 1 exemplo
- ○ A previsão vira exatamente o valor observado


- ■ Erro de treino = 0
- ■ Generalização = ruim


![image 39]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile39.png)

## Questões (Página 186)

- ● Qual é a profundidade aproximada de uma Árvore de Decisão treinada (sem restrições) em um conjunto de treinamento com um milhão de instâncias?
- ● A impureza Gini de um nó é geralmente menor ou maior que a de seu nó pai? Ela é geralmente menor/maior ou sempre menor/maior?
- ● Se uma Árvore de Decisão estiver sofrendo overﬁtting no conjunto de treino, é uma boa ideia diminuir o max_depth?
- ● Se uma Árvore de Decisão estiver sofrendo underﬁtting no conjunto de treino, é uma boa ideia escalar os atributos de entrada?


### Respirem fundo: para a prática de hoje a única coisa que vai sofrer para calcular logaritmo é a CPU, não o pulso de vocês!

Mas só por hoje. ;)

## Prática

- ● Leia o conjunto de dados Iris
- ● Deﬁna os conjuntos de treino e teste de forma estratiﬁcada
- ● Avalie variações de hiperparametros


- ○ Entropia vs coeﬁciente de Gini
- ○ Profundidade máxima (max_depth)
- ○ Número mínimo de amostras para dividir (min_samples_split)
- ○ Número mínimo de amostras na folha (min_samples_leaf)


## Lista de exercícios

● Google Classroom

## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

○ Capítulo 6

![image 40]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile40.png)

![image 41]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile41.png)

##### Diego Bezerra

![image 42]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile42.png)

dfb2@cesar.school in/diegodefb

![image 43]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile43.png)

![image 44]([CESAR School] - AM - Aula 05 - Coeficiente de Gini e Prática.pptx_images/imageFile44.png)

