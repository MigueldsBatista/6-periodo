https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html


https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.VotingClassifier.html


Random Forest é um tipo específico de bagging, com a característica
da aleatoriedade das features

TERMOS QUE EU NAO SEI

bagging -> 

hold-out -> separar treino e teste

Cross-Validation -> separar treino e teste varias vezes, para ter uma média mais confiável do

out of bagging ->

classificacao x regressao

overfitting


QUESTÃO 1 -> a) Calcule a entropia do conjunto total apos a divisão pelo atributo palavra chave. aqui ele tb quer a entropia ponderada? Ou seja, a entropia de cada ramo multiplicada pela proporção de exemplos naquele ramo em relação ao total?

QUESTÃO 5 -> O erro medio quadratico total seria a mesma logica da entropia ponderada? pega cada grupo e calcula a media dos erros quadráticos, ponderando pela proporção de exemplos em cada grupo em relação ao total?

QUESTÃO 9 -> A seria so desenhar o grafico da arvore com as divisoes?

LISTA 2 

1 -> a) Calcule a entropia do conjunto total considerando as três classes.
ENTROPIA NORMAL?

e) Caso o próximo nó seja Avaliação, explique como o algoritmo lida com atributos multiclasse.
OQ É ESPERADO AQUI

---------------------- REVISAO ----------------------
Questão 16
Explique com suas palavras:
a) O que é Bagging (Bootstrap Aggregating) e qual problema ele busca resolver.
Bagging é uma forma de aprendizado para árvores de regressão, aonde basicamente pegamos amostras boostrap com reposição do dataset original e usamos para treinar os modelos e tirar a média do resultado para assim obter predições mais confiáveis

b) Por que Bagging reduz variância mas não necessariamente o viés do modelo.
Bagging reduz a variância pelo fato de tirar a média dos resultados, então isso diminui o efeito de outliers, porem ainda sim, é possivel que em dados com muito ruido o modelo acabe aprendendo estes padrões, resultando em um overfitting

c) Cite dois exemplos de algoritmos que usam Bagging.
Random Forest
Bagging SVM

d) Explique o papel do bootstrap no Bagging.
Bootstrap é necessário no bagging pois as amostras precisam ter reposição e ser aleatorias

Questão 17
Considere que você tem um dataset com 50.000 exemplos e 20 atributos para classificação.
a) Explique as principais diferenças entre treinar uma árvore de decisão simples e uma Random
Forest.
Usar uma árvore comum apenas iriamos calcular a entropia, ou gini, enquanto por uma random forest, iriamos garantir que boa parte do conjunto foi testada e que todas as features foram absorvidas, pois o RF obriga o modelo a olhar para features que ele talvez antes fosse ignorar

b) Por que o Random Forest seleciona apenas um subconjunto de atributos em cada divisão de
nó? Ele seleciona apenas um conjunto para garantir que os modelos sejam indepententes no treinamento, e combinar os resultados ao final para que no teste ele consiga identificar melhor padrões, minimizando a chance de decorar o ruido do dataset ou informações especificas


c) Cite duas vantagens do Random Forest em relação a uma única árvore.
* Random Forest diminui a variância, previnindo contra ruidos, outliers etc
* Garante que maior parte dos dados e das features sejam testados

d) Qual é o impacto do aumento do número de árvores na Random Forest sobre:
● Acurácia
● Tempo de treinamento
Numero de árvores tende a aumentar a acurácia do modelo, mas chega uma hora que o ganho de acurácia não compensa
devido ao tempo de teste que vai crescente exponencialmente mais, então precisa estar num meio termo


Questão 18 — Overfitting em Random Forest
Um Random Forest foi treinado com 500 árvores profundas em um dataset pequeno.
a) Ele ainda corre risco de overfitting? Justifique.
Sim ele corre o risco, foi mencionado que são árvores profundas e um dataset pequeno, mesmo que o modelo use a media, se a maioria dos dados tiver ruido e as árvores forem muito profundas, a media como um todo vai ser afetada

b) Explique o efeito do parâmetro max_depth sobre o overfitting.
Quanto maior esse parâmetro maior a change de overfitting, este parametro basicamente controla a profundidade da arvore
e sua complexidade (quantos niveis ela vai ter), arvores muito profundas deixam o modelo mais propenso a decorar os dados, fazendo ele ser altamente especializado e ruim em generalizar para novos dados

c) Como o Bagging ajuda a mitigar o overfitting em Random Forest?
Bagging ajuda a mitigar o overfitting, pois como tiramos varias amostras aleatorias e indepentendes, isso ajuda para que o modelo nao decore o conjunto como um todo, ja que ele precisa analisar varias amostras diferentes e depois tirar uma media, cada uma sendo uma arvore independente


d) Cite dois hiperparâmetros que podem ser ajustados para controlar a complexidade do
modelo.
- max_depth
- n_estimators

Questão 19 — Importância de Variáveis
Em uma Random Forest, você observa a seguinte ordem de importância dos atributos:

| Atributo    | Importância |
|-------------|-------------|
| Idade       | 0.40        |
| Renda       | 0.30        |
| Sexo        | 0.10        |
| Experiência | 0.20        |

a) Explique como a Random Forest calcula a importância de cada variável.
A importância é calculada com base na redução total de impureza (seja Gini, Entropia ou MSE) que cada variável proporciona ao longo de todas as árvores da floresta. O atributo que mais reduz a impureza é o mais influente


b) Qual atributo influencia mais a classificação? Justifique.
- Aquele com menor MSE

c) Um atributo com baixa importância deve ser removido do modelo? Explique.
Não necessariamente, baixa importancia não quer dizer que nao tem, ainda sim podem existir padroes sutis que com um conjunto maior de treinamento sejam observados e aprendido pelo modelo pois modelos como RF obrigam o modelo a escolher features aleatorias que ele antes nao olharia

d) Cite duas situações em que a interpretação de importância de variável pode ser enganosa.
Vamos imaginar uma variavel ID, ela sempre daria erro quadratico = 0 pois cada ID sempre vai ter apenas uma classe final
ja que ele identifica unicamente as linhas, mas isso nao seria um bom dado preditivo pois o modelo so decoraria
Variáveis Correlacionadas. Se "Renda" e "Patrimônio" dizem a mesma coisa, a RF divide a importância entre elas, fazendo parecer que ambas são menos importantes do que realmente são.


Questão 20 — Boosting vs Bagging
a) Explique a principal diferença conceitual entre Bagging e Boosting.
Bagging seria aprendizado paralelo, todas as arvores sao treinadas ao mesmo tempo. Boosting seria sequencial e uma arvore vai aprendendo com os erros da outra

b) Cite dois algoritmos de Boosting conhecidos.
Adaboost XBoost

c) Explique como o Boosting lida com erros de instâncias mal classificadas.
O boosting usa peso para lidar instancias mal classificadas para reduzir o vies

d) Por que Boosting pode reduzir tanto viés quanto variância, enquanto Bagging foca apenas na
variância? Boosting pode reduzir tanto o vies quanto a variancia, Sobre a variancia:  como os modelos aprendem um com o erro do outro, o impacto de outliers ou decorar padroes específicos, quanto ao vies, o modelo utiliza peso para instancias mal classificadas, isso faz com que dados enviesados sejam mitigados pelos pesos com base (em sua importancia?)

Questão 21 — Random Forest e Out-of-Bag (OOB)
a) Explique o conceito de amostras Out-of-Bag (OOB) em Random Forest.
Amostras out of bag sao uma consequencia natural do random forest, pois nem sempre todos os dados vão ser escolhiso ja que as amostras sao aleatorias, out of bag são basicamente essas amostras que nao foram escolhidas e podem ser usadas depois para outros propositos como testes

b) Como o OOB pode ser usado para estimar a acurácia do modelo sem validação cruzada?
Podemos estimar a acuracia com as amostras OOB, pois sabemos que elas nao foram usadas durante o treino, entao nao precisamos da validação cruzada (que seria utilizar todas as combinacoes de dados para garantir que foram vistos)

c) Cite uma vantagem e uma limitação do uso de OOB.
Vantagem, não precisa separar dados para treino ja que isso acontece automaticamente
Desvantagem: Em conjuntos pequenos o modelo pode sofrer de underfitting

d) Explique por que cada árvore em Random Forest não vê todas as amostras do conjunto de
treinamento.
As arvores nao vem todas as amostras para garantir a independencia, e como o conjunto é escolhido de forma aleatoria eh natural que algumas sejam deixadas de fora

Questão 22
Considere os principais hiperparâmetros: 
- n_estimators
- max_depth
- min_samples_split
- max_features

a) Explique o efeito de aumentar n_estimators.
N estimators tende a aumentar a acuracia do modelo pois quer dizer que vamos ter mais arvores para aprender sobre aquele conjunto de dados, mas tambem vai aumentar o tempo de processamento

b) Explique o efeito de reduzir max_depth.
Reduzir o max_depth vai deixar nossa árvore mais rasa, geralmente o ideal é encontrar um meio termo entre log2(n) para o conjunto de dados, pois muito profundo resulta em overfitting mas muito raso pode gerar um underfitting

c) Explique como max_features afeta a diversidade das árvores e a generalização.
Diminuir max_features pode auxiliar a arvore a generalizar melhor para dados nao vistos, pois cada arvore vai pegar features diferentes e aprender seus padroes, e ao final ao combinar o resultado das arvores uma variedade maior de features vai ter sido estudada

d) Dê um exemplo de combinação de hiperparâmetros que poderia reduzir overfitting.
reduzir max_depth, definir min_samples_split e min_samples_leaf

Questão 24
Você treina uma Random Forest para prever o preço de casas.

a) Explique como a Random Forest calcula a previsão final para regressão.
Random forest vai de separar varias arvores de treinamento
para cada uma vai escolher um conjunto aleatorio dos dados e um conjunto aleatorio de features
e vai calcular a media dos valores de acordo com o intervalo especificado para tentar prever

b) Cite uma vantagem de usar Random Forest em regressão em relação a uma árvore simples.
Ajuda a reduzir o impacto de outliers

c) Explique como o critério de divisão (ex: MSE) é utilizado em cada árvore.
MSE (se analisa a divisao com menor erro quadratico medio)
GINI (se analisa a disivsao com o menor GINI)
GANHO DE INFORMACAO (se analisa o atributo que resultou apos a divisao no maior GI)25)