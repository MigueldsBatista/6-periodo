# Lista de Exercícios 1 - Aprendizado de Máquina 2026.1

- Questão 1 - Um sistema de ﬁltragem de e-mail deseja classiﬁcar mensagens como Spam (1) ou Não Spam (0) com base em três atributos:


- ● Palavra-chave (Contém / Não contém)
- ● Links externos (Sim / Não)
- ● Domínio (Novo / Antigo)


Considere o seguinte conjunto de treinamento:

|Palavra-chave|Links externos|Domínio|Spam|
|---|---|---|---|
|Contém|Sim|Novo|1|
|Não contém|Não|Novo|1|
|Não contém|Sim|Antigo|0|
|Contém|Não|Novo|0|
|Contém|Sim|Novo|1|
|Contém|Sim|Antigo|1|
|Não contém|Não|Novo|0|
|Não contém|Não|Antigo|0|


- a) Calcule a entropia do conjunto total.
- b) Calcule a entropia após dividir pelo atributo Palavra-chave.
- c) Calcule o ganho de informação dessa divisão.
- d) Esse atributo seria uma boa escolha para o nó raiz? Justiﬁque.
- e) Explique por que o algoritmo de árvores de decisão aplica esse processo recursivamente.


![image 2](Lista de Exerícios 1 - Árvores de Decisão_images/imageFile2.png)

- Questão 2 — Considere um nó de decisão contendo 10 exemplos:


|Classe|Quantidade|
|---|---|
|A|7|
|B|3|


## Calcule

- a) A entropia do nó.
- b) O coeﬁciente de Gini.
- c) Agora considere um nó perfeitamente balanceado:

|Classe|Quantidade|
|---|---|
|A|5|
|B|5|


Calcule novamente:

- ● Entropia
- ● Gini


- d) Compare os resultados e explique qual situação representa maior impureza.
- e) Explique por que o coeﬁciente de Gini é computacionalmente mais eﬁciente que a entropia.


- Questão 3 - Considere a seguinte árvore de decisão treinada para prever aprovação de crédito:


Renda > 5000? ├── Sim → Aprovar └── Não

└── Histórico de crédito bom? ├── Sim → Aprovar └── Não → Negar

## Classiﬁque os seguintes clientes

|Cliente|Renda|Histórico|
|---|---|---|
|A|6000|Ruim|
|B|4000|Bom|
|C|2000|Ruim|
|D|8000|Bom|


## Perguntas

- a) Qual atributo tem maior inﬂuência no modelo?
- b) Explique por que atributos próximos da raiz da árvore tendem a ser mais importantes.
- c) Cite duas vantagens das árvores de decisão em comparação com modelos como redes neurais.


- Questão 4 - Um cientista de dados treinou três árvores de decisão para um problema de classiﬁcação.


|Modelo|max_depth|Acurácia Treino|Acurácia Teste|
|---|---|---|---|
|A|2|72%|70%|
|B|5|91%|84%|
|C|15|100%|68%|


## Perguntas

- a) Qual modelo apresenta overﬁtting?
- b) Explique por que árvores profundas são mais propensas a overﬁtting.
- c) Cite três técnicas para reduzir overﬁtting em árvores.
- d) Explique o papel dos hiperparâmetros:


- ● min_samples_split
- ● min_samples_leaf


![image 8](Lista de Exerícios 1 - Árvores de Decisão_images/imageFile8.png)

### Questão 5 - Um modelo de árvore de regressão deseja prever salário (mil reais) com base nosanos de experiência.Conjunto de dados:

|Experiência|Salário|
|---|---|
|1|30|
|2|35|
|3|40|
|6|70|
|7|75|
|8|80|


O algoritmo considera dividir os dados em:

Experiência ≤ 3 Experiência > 3

## Calcule

- a) A média do salário em cada grupo.
- b) O erro quadrático total após a divisão.
- c) Explique por que árvores de regressão utilizam erro quadrático médio como critério de divisão.
- d) O que acontece se a árvore continuar crescendo até que cada folha tenha apenas um exemplo?


- Questão 6 — Responda e justiﬁque:

- a) Árvores de decisão precisam que os atributos sejam normalizados ou padronizados?
- b) Árvores de decisão conseguem lidar naturalmente com dados não lineares?
- c) Uma árvore muito profunda tende a ter alta variância ou alto viés?
- d) Explique por que métodos baseados em Random Forest costumam ter melhor desempenho que uma única árvore.


- Questão 7 — Suponha que uma árvore de decisão seja treinada sem restrições em um conjunto de treinamento com 1 milhão de exemplos.

- a) Qual é a profundidade aproximada máxima que essa árvore poderia atingir?
- b) Explique por que isso acontece.
- c) Discuta por que isso representa um risco de overﬁtting extremo.


- Questão 8 — Um modelo de árvore de decisão foi treinado e apresentou:


- ● Acurácia de treino: 100%
- ● Acurácia de teste: 60%


- a) O que provavelmente ocorreu durante o treinamento?
- b) Cite duas possíveis causas para esse comportamento.
- c) Proponha duas modiﬁcações no modelo para melhorar a generalização.


- Questão 9 — Uma árvore de decisão foi treinada para classiﬁcar pontos no plano bidimensional utilizando dois atributos:


- ● x1 (idade)
- ● x2 (renda)


A árvore gerada foi:

x1 ≤ 30 ?

├── Sim │ └── x2 ≤ 2000 ? │ ├── Sim → Classe A │ └── Não → Classe B └── Não

└── x2 ≤ 5000 ?

├── Sim → Classe B └── Não → Classe C

Considere os seguintes pontos:

|Ponto|x1|x2|
|---|---|---|
|P1|25|1500|
|P2|28|4000|
|P3|35|3000|
|P4|40|7000|


- a) Classiﬁque cada ponto utilizando a árvore.
- b) Descreva quais regiões do plano (x1,x2) correspondem a cada classe.
- c) Explique por que árvores de decisão produzem fronteiras de decisão retangulares (ou hiper-retangulares).
- d) Discuta uma limitação desse tipo de fronteira ao modelar relações complexas entre variáveis.
- e) Cite um modelo que pode superar essa limitação.


- Questão 10 — Um conjunto de dados é usado para prever se uma pessoa vai ao parque (Sim/Não). Atributos:


- ● Clima (Ensolarado, Nublado, Chuvoso)
- ● Temperatura (Alta, Média, Baixa)
- ● Vento (Fraco, Forte)


Conjunto de treinamento:

|Clima|Temperatura|Vento|Vai ao parque|
|---|---|---|---|
|Ensolarado|Alta|Fraco|Não|
|Ensolarado|Alta|Forte|Não|
|Nublado|Alta|Fraco|Sim|


|Chuvoso|Média|Fraco|Sim|
|---|---|---|---|
|Chuvoso|Baixa|Fraco|Sim|
|Chuvoso|Baixa|Forte|Não|
|Nublado|Baixa|Forte|Sim|
|Ensolarado|Média|Fraco|Não|
|Ensolarado|Baixa|Fraco|Sim|
|Chuvoso|Média|Forte|Não|


- a) Calcule a entropia do conjunto total.
- b) Considere dividir pelo atributo Clima. Calcule a entropia de cada subconjunto.
- c) Calcule o ganho de informação dessa divisão.
- d) Explique se Clima seria uma boa escolha para o nó raiz.
- e) Suponha que o nó Clima = Ensolarado ainda não esteja puro. Qual atributo deveria ser testado em seguida? Justiﬁque.


