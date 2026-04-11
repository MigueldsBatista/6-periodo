![image 1]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile4.png)

# Aprendizado de Máquina

###### Árvores de Decisão

2026 | Fevereiro

### Vimos que podemos aprender medindo distância

### E se aprender fosse apenas fazer as perguntas certas?

![image 5]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile5.png)

![image 6]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile6.png)

- ● Técnica de aprendizado supervisionado usada tanto para classiﬁcação quanto para regressão
- ● Estrutura em formato de árvore, onde cada nó interno representa uma decisão baseada em um atributo e cada folha representa uma classe ou resultado
- ● Não requer muita preparação de dados (ex.: normalização)
- ● Você provavelmente já usa e nem percebeu ainda


![image 7]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile7.png)

![image 8]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile8.png)

## Vantagens

- ● Árvores de decisão transformam esse processo humano de perguntas em um modelo matemático


- ○ Fáceis de interpretar
- ○ Explicáveis para não técnicos
- ○ Funcionam para classiﬁcação e regressão
- ○ Base para modelos mais avançados (Random Forest, Boosting)


## Relembrando…

- ● O primeiro nó de decisão é chamado de nó raiz (Root Node)
- ● Todos os nós que se dividem em “nós ﬁlhos”, são chamados de nó de decisão (Decision Node)
- ● Os nós ﬁnais, que não se dividem mais, são chamados de nó folha (Leaf Node)
- ● Cada seta representando uma divisão é chamada de galho/ramo (Branch)
- ● A profundidade indica quantas decisões consecutivas são necessárias para chegar a uma predição ﬁnal.


![image 9]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile9.png)

![image 10]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile10.png)

###### True False

![image 11]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile11.png)

![image 12]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile12.png)

True False

Profundidade: 2

Profundidade: 5

### Em vez de memorizar exemplos, podemos derivar uma estrutura que explique os dados

##### ● Atributos: tempo (ensolarado, nublado, chuvoso), umidade (alta, baixa), vento(fraco, forte)

|Tempo|Umidade|Vento|Praticar Esporte|
|---|---|---|---|
|Ensolarado|Alta|Fraco|Não|
|Ensolarado|Alta|Forte|Não|
|Nublado|Alta|Fraco|Sim|
|Chuvoso|Baixa|Fraco|Sim|
|Chuvoso|Alta|Forte|Não|


- ● Passo 1: Qual atributo parece separar melhor ‘Sim’ e ‘Não’?
- ● Passo 2: Qual categoria já ﬁcou pura?
- ● Passo 3: Escolhemos o atributo que deixa os grupos mais organizados?
- ● Passo 4: Para cada folha


- ○ Se todos os exemplos são da mesma classe, associar essa classe à folha
- ○ Senão repetir os passos 1 a 4


- ● Passo 1: Qual atributo parece separar melhor ‘Sim’ e ‘Não’?
- ● Passo 2: Qual categoria já ﬁcou pura?
- ● Passo 3: Escolhemos o atributo que deixa os grupos mais organizados?
- ● Passo 4: Para cada folha


|Tempo|Umidade|Vento|Praticar Esporte|
|---|---|---|---|
|Ensolarado|Alta|Fraco|Não|
|Ensolarado|Alta|Forte|Não|
|Nublado|Alta|Fraco|Sim|
|Chuvoso|Baixa|Fraco|Sim|
|Chuvoso|Alta|Forte|Não|


- ○ Se todos os exemplos são da mesma classe, associar essa classe à folha
- ○ Senão repetir os passos 1 a 4


![image 13]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile13.png)

|Tempo|Umidade|Vento|Praticar Esporte|
|---|---|---|---|
|Ensolarado|Alta|Fraco|Não|
|Ensolarado|Alta|Forte|Não|
|Nublado|Alta|Fraco|Sim|
|Chuvoso|Baixa|Fraco|Sim|
|Chuvoso|Alta|Forte|Não|


### Isso signiﬁca que Tempo é o atributo mais importante?

## Importância dos atributos

- ● A importância de um atributo está relacionada ao quanto ele contribui para organizar os dados ao longo da árvore
- ● Atributos usados perto da raiz tendem a impactar mais exemplos
- ● Atributos que aparecem várias vezes inﬂuenciam várias decisões
- ● Atributos que deixam grupos mais “puros” têm maior relevância


## Exercício

![image 14]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile14.png)

- ● Passo 1: Qual atributo parece separar melhor ‘Sim’ e ‘Não’?
- ● Passo 2: Qual categoria já ﬁcou pura?
- ● Passo 3: Escolhemos o atributo que deixa os grupos mais organizados?
- ● Passo 4: Para cada folha


- ○ Se todos os exemplos são da mesma classe, associar essa classe à folha
- ○ Senão repetir os passos 1 a 4


## Superfície de decisão

- ● O espaço é particionado em regiões retangulares (ou hiper-retangulares), e cada região corresponde a uma folha da árvore
- ● Cada novo nível da árvore adiciona um novo corte no espaço de atributos
- ● Árvores mais profundas produzem superfícies mais fragmentadas e complexas


## Exemplo: Iris dataset

![image 15]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile15.png)

![image 16]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile16.png)

## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

○ Capítulo 6

![image 17]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile17.png)

![image 18]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile18.png)

#### Diego Bezerra

![image 19]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile19.png)

dfb2@cesar.school in/diegodefb

![image 20]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile20.png)

![image 21]([CESAR School] - AM - Aula 03 - Árvores de Decisão.pptx_images/imageFile21.png)

