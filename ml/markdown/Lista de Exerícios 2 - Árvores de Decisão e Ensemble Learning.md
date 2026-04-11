# Lista de Exercícios 2 - Aprendizado de Máquina 2026.1

- Questão 1: Um site de e-commerce deseja classiﬁcar produtos em três categorias com base em três atributos:


- ● Preço (Baixo / Médio / Alto)
- ● Avaliação de clientes (Ruim / Boa / Excelente)
- ● Disponibilidade (Em estoque / Esgotado)


Conjunto de treinamento:

|Preço|Avaliação|Estoque|Categoria|
|---|---|---|---|
|Baixo|Boa|Em estoque|A|
|Alto|Excelente|Em estoque|C|
|Médio|Boa|Esgotado|B|
|Baixo|Ruim|Esgotado|A|
|Alto|Boa|Em estoque|C|
|Médio|Excelente|Em estoque|B|


![image 2](Lista de Exerícios 2 - Árvores de Decisão e Ensemble Learning_images/imageFile2.png)

|Baixo|Excelente|Em estoque|A|
|---|---|---|---|
|Médio|Ruim|Esgotado|B|


#### Perguntas:

- a) Calcule a entropia do conjunto total considerando as três classes.
- b) Calcule a entropia após dividir pelo atributo Preço.
- c) Determine o ganho de informação dessa divisão.
- d) Explique se Preço seria uma boa escolha para o nó raiz e por quê.
- e) Caso o próximo nó seja Avaliação, explique como o algoritmo lida com atributos multiclasse.


- Questão 2: Um nó contém os seguintes exemplos para classiﬁcação em três classes:


|Classe|Quantidade|
|---|---|
|A|4|
|B|3|
|C|3|


#### Perguntas:

- a) Calcule a entropia do nó.
- b) Calcule o coeﬁciente de Gini.
- c) Agora considere um nó perfeitamente balanceado com 10 exemplos (A: 3, B: 3, C: 4). Calcule novamente.
- d) Compare os resultados e discuta qual nó apresenta maior impureza.
- e) Explique qual critério seria mais sensível a mudanças na proporção de classes e por quê.


### Questão 3:Um conjunto de dados possui 10.000 registros para prever se um usuário clicaráem um anúncio. Foram treinadas três árvores:

|Modelo|max_depth|min_samples_leaf|Acurácia Treino|Acurácia Teste|
|---|---|---|---|---|
|A|3|10|75%|73%|
|B|12|1|99%|65%|
|C|8|5|88%|80%|


Perguntas:

- a) Qual modelo apresenta overﬁtting? Justiﬁque.
- b) Explique o efeito do parâmetro min_samples_leaf na generalização da árvore.
- c) Discuta o papel do parâmetro max_depth na complexidade do modelo.
- d) Proponha duas estratégias para melhorar a performance do modelo B sem reduzir a profundidade.


### Questão 4: Um modelo de árvore de regressão deseja prever a quantidade de vendas (emunidades) com base em dois atributos: Preço e Desconto (%). Conjunto de dados:

|Preço|Desconto|Vendas|
|---|---|---|
|50|5|200|
|60|10|180|
|70|0|150|


|55|15|220|
|---|---|---|
|65|5|190|
|75|10|160|


A árvore divide primeiro por Preço ≤ 60 e depois por Desconto ≤ 10.

Perguntas: a) Calcule a média de Vendas em cada folha após a divisão. b) Calcule o erro quadrático total da árvore. c) Explique por que árvores de regressão usam erro quadrático médio como critério de divisão. d) O que aconteceria se a árvore continuasse dividindo até cada folha ter apenas um exemplo?

- Questão 15: Um conjunto de dados possui dois atributos numéricos (x1, x2) e três classes. A árvore gerada foi: x1 ≤ 50 ? ├── Sim │ └── x2 ≤ 20 ? │ ├── Sim → Classe A │ └── Não → Classe B └── Não


└── x2 ≤ 60 ?

├── Sim → Classe B

└── Não → Classe C

Pontos a classiﬁcar:

![image 8](Lista de Exerícios 2 - Árvores de Decisão e Ensemble Learning_images/imageFile8.png)

|Ponto|x1|x2|
|---|---|---|
|P1|45|15|
|P2|40|25|
|P3|55|50|
|P4|60|70|


Perguntas: a) Classiﬁque cada ponto. b) Desenhe as regiões de decisão no plano x1 × x2 para cada classe. c) Explique por que árvores de decisão produzem fronteiras retangulares. d) Discuta uma limitação dessas fronteiras ao modelar relações complexas. e) Cite dois modelos que podem superar essa limitação.

## Questão 16

Explique com suas palavras:

- a) O que é Bagging (Bootstrap Aggregating) e qual problema ele busca resolver.
- b) Por que Bagging reduz variância mas não necessariamente o viés do modelo.
- c) Cite dois exemplos de algoritmos que usam Bagging.
- d) Explique o papel do bootstrap no Bagging.


## Questão 17

Considere que você tem um dataset com 50.000 exemplos e 20 atributos para classiﬁcação.

- a) Explique as principais diferenças entre treinar uma árvore de decisão simples e uma Random Forest.
- b) Por que o Random Forest seleciona apenas um subconjunto de atributos em cada divisão de nó?


- c) Cite duas vantagens do Random Forest em relação a uma única árvore.
- d) Qual é o impacto do aumento do número de árvores na Random Forest sobre:


- ● Acurácia
- ● Tempo de treinamento


## Questão 18 — Overﬁtting em Random Forest

Um Random Forest foi treinado com 500 árvores profundas em um dataset pequeno.

- a) Ele ainda corre risco de overﬁtting? Justiﬁque.
- b) Explique o efeito do parâmetro max_depth sobre o overﬁtting.
- c) Como o Bagging ajuda a mitigar o overﬁtting em Random Forest?
- d) Cite dois hiperparâmetros que podem ser ajustados para controlar a complexidade do modelo.


## Questão 19 — Importância de Variáveis

Em uma Random Forest, você observa a seguinte ordem de importância dos atributos:

|Atributo|Importância|
|---|---|
|Idade|0.40|
|Renda|0.30|
|Sexo|0.10|
|Experiência|0.20|


- a) Explique como a Random Forest calcula a importância de cada variável.
- b) Qual atributo inﬂuencia mais a classiﬁcação? Justiﬁque.


- c) Um atributo com baixa importância deve ser removido do modelo? Explique.
- d) Cite duas situações em que a interpretação de importância de variável pode ser enganosa.


## Questão 20 — Boosting vs Bagging

- a) Explique a principal diferença conceitual entre Bagging e Boosting.
- b) Cite dois algoritmos de Boosting conhecidos.
- c) Explique como o Boosting lida com erros de instâncias mal classiﬁcadas.
- d) Por que Boosting pode reduzir tanto viés quanto variância, enquanto Bagging foca apenas na variância?


## Questão 21 — Random Forest e Out-of-Bag (OOB)

a) Explique o conceito de amostras Out-of-Bag (OOB) em Random Forest. b) Como o OOB pode ser usado para estimar a acurácia do modelo sem validação cruzada? c) Cite uma vantagem e uma limitação do uso de OOB. d) Explique por que cada árvore em Random Forest não vê todas as amostras do conjunto de treinamento.

## Questão 22

Considere os principais hiperparâmetros: n_estimators, max_depth, min_samples_split, max_features.

- a) Explique o efeito de aumentar n_estimators.
- b) Explique o efeito de reduzir max_depth.
- c) Explique como max_features afeta a diversidade das árvores e a generalização.
- d) Dê um exemplo de combinação de hiperparâmetros que poderia reduzir overﬁtting.


## Questão 24

Você treina uma Random Forest para prever o preço de casas.

- a) Explique como a Random Forest calcula a previsão ﬁnal para regressão.
- b) Cite uma vantagem de usar Random Forest em regressão em relação a uma árvore simples.
- c) Explique como o critério de divisão (ex: MSE) é utilizado em cada árvore.


## Questão 25

Você tem um problema de classiﬁcação com 100.000 exemplos, 30 atributos e classes desbalanceadas.

- a) Você usaria Bagging ou Boosting? Justiﬁque.
- b) Em Random Forest, qual estratégia você usaria para lidar com desbalanceamento de classes?
- c) Cite uma situação em que Boosting pode superar Random Forest.
- d) Discuta um cenário em que Bagging é preferível a Boosting.


