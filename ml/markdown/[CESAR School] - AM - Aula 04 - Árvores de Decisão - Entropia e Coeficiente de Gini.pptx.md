![image 1]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile1.png)

![image 2]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile2.png)

![image 3]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile3.png)

![image 4]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile4.png)

# Aprendizado de Máquina

###### Árvores de Decisão

2026 | Fevereiro

### Nem todo caminho que leva ao acerto é o caminho correto.

## Construindo Árvores de Decisão

![image 5]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile5.png)

|Palavras-chave|Links Externos|Dominio|Spam|
|---|---|---|---|
|Contem|Sim|Novo|1|
|Nao contem|Nao|Novo|1|
|Nao contem|Sim|Antigo|0|
|Contem|Nao|Novo|0|
|Contem|Sim|Novo|1|
|Contem|Sim|Antigo|1|
|Nao contem|Nao|Antigo|0|
|Contem|Sim|Antigo|1|
|Não contém|Sim|Antigo|0|
|Não contém|Sim|Antigo|0|


Não contém Contém

Não Sim Antigo Novo

## Aplicando sobre uma amostra

##### ● Testando novo exemplo: Palavras-chave: contém; links externos: sim;

##### domínio: novo; spam: 1

![image 6]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile6.png)

Não contém Contém

Não Sim Antigo Novo

### No meio do caos dos dados, queremos encontrar a pureza.

## Medidas de Impureza

![image 7]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile7.png)

- ● Temos duas classes na variável alvo
- ● Em todo conjunto, temos uma alta Impureza

- ○ Dos 10 exemplos
- ○ 5 são da classe positiva (spam)
- ○ 5 da classe negativa (não é spam)


- ● Relação entre as classes (p1)
- ● 0.5 é a relação de maior impureza possível


## Medida de Impureza

- ○ Temos exatamente metade dos dados como classe positiva e metade como classe negativa
- ○ Se o conjunto de dados tivesse 100% positivos ou negativos, seria considerado PURO.
- ○ A Árvore de Decisão tenta encontrar decisões puras


## E como medir o nível de impureza?

- ● Entropia

○ Começa no zero, sobe até o valor máximo de um e volta para zero

- ● pi = proporção da classe i no conjunto S
- ● log2 = logaritmo na base 2
- ● A soma percorre todas as classes
- ● Importante saber que:


![image 8]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile8.png)

![image 9]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile9.png)

○ 0 ≤ H(S) ≤ log2(c), ondecé o número de classes

## Entropia: Exemplo

- ● Se temos 6 exemplos, sendo 2 da classe positiva
- ● Em outro subconjunto também temos 6 exemplos, mas 5 da classe positiva:


![image 10]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile10.png)

![image 11]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile11.png)

![image 12]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile12.png)

## Medida de Impureza

|Palavras-chave|Links Externos|Dominio|Spam|
|---|---|---|---|
|Contem|Sim|Novo|1|
|Nao contem|Nao|Novo|1|
|Nao contem|Sim|Antigo|0|
|Contem|Nao|Novo|0|
|Contem|Sim|Novo|1|
|Contem|Sim|Antigo|1|
|Nao contem|Nao<br><br>![image 13]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile13.png)|Antigo|0|
|Contem|Sim|Antigo|1|
|Não contém|Sim|Antigo|0|
|Não contém|Sim|Antigo|0|


![image 14]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile14.png)

Palavras-chave

Entropia: Exercício

![image 15]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile15.png)

- ● Calcular a proporção de classes e a entropia para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e entropia para cada ramo (subconjunto) contém e não-contém


![image 16]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile16.png)

## Entropia: Resolução

![image 17]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile17.png)

- ● Calcular a proporção de classes e a entropia para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e entropia para cada ramo (subconjunto) contém e não-contém


![image 18]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile18.png)

![image 19]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile19.png)

![image 20]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile20.png)

![image 21]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile21.png)

![image 22]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile22.png)

![image 23]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile23.png)

![image 24]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile24.png)

![image 25]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile25.png)

![image 26]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile26.png)

![image 27]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile27.png)

![image 28]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile28.png)

![image 29]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile29.png)

- ● Calcular a proporção de classes e a entropia para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e entropia para cada ramo (subconjunto) contém e não-contém


![image 30]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile30.png)

- ● Calcular a proporção de classes e a entropia para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e entropia para cada ramo (subconjunto) contém e não-contém


### Informação não é o que você sabe, é o quanto de dúvida você consegue eliminar.

![image 31]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile31.png)

## Ganho de informação

###### ● Mede quanto a incerteza (entropia) diminui após dividir os dados por um atributo

![image 32]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile32.png)

- ○ H(S) é a entropia antes da divisão
- ○ H(Sv) é a entropia após a divisão
- ○ Escolhemos o atributo com maior ganho


## Calculando o Ganho de informação

![image 33]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile33.png)

![image 34]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile34.png)

![image 35]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile35.png)

![image 36]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile36.png)

![image 37]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile37.png)

![image 38]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile38.png)

![image 39]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile39.png)

![image 40]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile40.png)

![image 41]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile41.png)

## A melhor decisão

![image 42]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile42.png)

- ● A melhor decisão a ser tomada será a que nos der um valor maior de Ganho de Informação
- ● Aplicar esse algoritmo de forma recursiva, construindo assim as próximas ramiﬁcações da mesma forma sobre os subconjuntos de dados


Não contém Contém

Não Sim Antigo Novo

## Coeﬁciente de Gini

![image 43]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile43.png)

- ● Mede o grau de mistura de classes em um nó
- ● Quanto mais puro (ou homogêneo) for um nó, menor será o Gini
- ● Durante a construção da árvore:


![image 44]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile44.png)

- ○ Calculamos o Gini de cada divisão
- ○ Escolhemos a que gera menor impureza média ponderada, podendo selecionar diferentes combinações de nós


![image 45]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile45.png)

conjunto (todo o conjunto palavras chave)

- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 46]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile46.png)

![image 47]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile47.png)

![image 48]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile48.png)

![image 49]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile49.png)

![image 53]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile53.png)

- conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 54]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile54.png)

![image 55]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile55.png)

![image 56]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile56.png)

![image 57]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile57.png)

![image 61]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile61.png)

- ● Calcular a proporção de classes e Gini para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 62]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile62.png)

- ● Calcular a proporção de classes e Gini para o conjunto (todo o conjunto palavras chave)
- ● Calcular a proporção e Gini para cada ramo (subconjunto) contém e não-contém


![image 64]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile64.png)

![image 65]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile65.png)

## Entropia vs Gini

- ● Geralmente a árvore construída com Entropia ou Gini é muito parecida
- ● Entropia

- ○ Baseada na teoria da informação
- ○ Mais sensível a mudanças próximas de 0.5


- ● Gini


- ○ Mede probabilidade de erro de classiﬁcação aleatória
- ○ Computacionalmente mais simples


## Exercício

|Tempo|Umidade|Vento|Praticar Esporte|
|---|---|---|---|
|Ensolarado|Alta|Fraco|Não|
|Ensolarado|Alta|Forte|Não|
|Nublado|Alta|Fraco|Sim|
|Chuvoso|Baixa|Fraco|Sim|
|Chuvoso|Alta|Forte|Não|


## Referências

● GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2a Edição: O'Reilly Media, 2019.

○ Capítulo 6

![image 67]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile67.png)

![image 68]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile68.png)

#### Diego Bezerra

![image 69]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile69.png)

dfb2@cesar.school in/diegodefb

![image 70]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile70.png)

![image 71]([CESAR School] - AM - Aula 04 - Árvores de Decisão - Entropia e Coeficiente de Gini.pptx_images/imageFile71.png)

