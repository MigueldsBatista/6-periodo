# Aprendizado de Máquina - Compilação Completa

## Índice
1. [Introdução ao Aprendizado de Máquina](#introdução)
2. [Aprendizado Supervisionado](#aprendizado-supervisionado)
3. [Árvores de Decisão](#árvores-de-decisão)
4. [Medidas de Impureza: Entropia e Gini](#medidas-de-impureza)
5. [Overfitting e Underfitting](#overfitting-e-underfitting)
6. [Ensemble Learning](#ensemble-learning)
7. [Referências](#referências)

---

## Introdução

### O que é Aprendizado de Máquina?

Aprendizado de Máquina é uma disciplina que permite aos computadores aprender a partir de dados sem serem explicitamente programados. É o processo de extrair padrões de dados e utilizá-los para fazer previsões ou tomar decisões automáticas.

### Objetivos Principais

- Introduzir conceitos básicos e algoritmos clássicos de aprendizado de máquina
- Compreender as etapas de aquisição, tratamento, análise e visualização de dados
- Implementar ciclos completos de treinamento, validação e testes
- Explorar problemas práticos e suas soluções

### Pré-requisitos

- Conhecimento sólido em Análise e Visualização de Dados
- Matrizes de correlação, gráficos de dispersão e distribuição
- Conceitos estatísticos, cálculo e álgebra linear
- Lógica computacional

### Tipos de Problemas em ML

O aprendizado de máquina resolve diversos tipos de problemas:

- **Previsão de valores**: Prever preço de imóvel, estimativa de vendas
- **Detecção de anomalias**: Detecção de fraude, identificação de comportamentos anormais
- **Recomendação**: Recomendação de filmes, produtos personalizados
- **Segmentação**: Divisão de clientes em grupos com características similares
- **Reconhecimento**: Identificação de imagens, categorização de objetos
- **Previsão de comportamento**: Predição de churn (abandono de clientes)

---

## Aprendizado Supervisionado

### Definição

Aprendizado Supervisionado é um tipo de aprendizado onde os dados de treinamento incluem rótulos (labels) que definem um padrão previamente identificado. O algoritmo aprende a partir desses pares entrada-saída para fazer previsões em dados novos.

### Características Principais

- Depende de um rótulo que define um padrão
- Os rótulos podem ser:
  - **Categóricos** (classificação): Spam/Não-spam, Gato/Cachorro
  - **Numéricos contínuos** (regressão): Preço, temperatura, peso

### Dois Paradigmas Principais

#### 1. Aprendizado Baseado em Instâncias

Compara a instância de teste com exemplos armazenados no conjunto de treino.

**Características:**
- Mede similaridade entre instâncias
- Usa a maioria dos vizinhos próximos para classificação
- Exemplo clássico: k-Nearest Neighbors (kNN)

**Como funciona kNN:**
- Para classificar uma nova instância, encontra os k vizinhos mais próximos
- Classifica baseado na maioria dos rótulos desses vizinhos
- Requer armazenar todo o conjunto de treinamento

#### 2. Model-Based Learning

Constrói um modelo matemático baseado nos dados que representa uma função relacionando entradas às saídas.

**Características:**
- Cria uma representação abstrata dos padrões
- Permite fazer previsões sem manter os dados originais
- O modelo pode ser:
  - Uma superfície de separação entre classes
  - Uma função que realiza fitting nos dados
  - Uma estrutura simbólica (como árvores)

### Desafios Principais no Aprendizado Supervisionado

1. **Algoritmo ruim**: Escolha inadequada do modelo para o problema
2. **Dado ruim**:
   - Quantidade insuficiente de exemplos
   - Dados não representativos (tendenciosos)
   - Dados com baixa qualidade (erros, valores faltantes)
   - Features (atributos) irrelevantes
   - Ruído excessivo

---

## Árvores de Decisão

### Conceito Fundamental

Uma Árvore de Decisão é uma técnica de aprendizado supervisionado que simula o processo natural de tomada de decisão humana através de perguntas sucessivas sobre os atributos dos dados.

**Ideia central:** Em vez de memorizar exemplos como faz o kNN, ou fazer fitting em toda a distribuição dos dados, a árvore de decisão **deriva uma estrutura que explica os dados através de uma série de decisões lógicas**.

### Características e Vantagens

**Aplicabilidade:**
- Funciona tanto para classificação quanto para regressão
- Não requer normalização de dados
- Transformam o processo humano de fazer perguntas em um modelo matemático

**Vantagens principais:**
- Fáceis de interpretar e explicar
- Explicáveis para pessoas não técnicas
- Servem como base para modelos mais avançados (Random Forest, Boosting)
- Fornecem importância de atributos naturalmente
- Funcionam bem com dados categóricos e numéricos misturados

### Estrutura de uma Árvore de Decisão

```
                    [Nó Raiz]
                       |
              [Nó de Decisão]
               /             \
            [Ramo]         [Ramo]
           /                  \
      [Nó de Decisão]    [Nó Folha]
       /            \
   [Folha]      [Folha]
```

**Componentes:**

- **Nó Raiz**: Primeiro nó de decisão, que representa o atributo mais importante
- **Nó de Decisão**: Nó que se divide em dois ou mais ramos baseado em uma condição
- **Nó Folha (Leaf)**: Nó terminal que não se divide mais, contém a predição final (classe ou valor)
- **Ramo (Branch)**: Seta representando uma decisão (verdadeiro/falso ou uma categoria)
- **Profundidade**: Número de decisões consecutivas necessárias para chegar a uma predição

### Processo de Construção de uma Árvore

O algoritmo ID3/C4.5 segue este processo:

1. **Escolher o atributo raiz**: Qual atributo separa melhor as classes?
2. **Criar ramos**: Dividir os dados baseado nas categorias do atributo
3. **Verificar pureza**: Se um ramo é puro (contém apenas uma classe), cria uma folha
4. **Recursão**: Para cada ramo impuro, repetir o processo

**Exemplo prático - Jogar tênis:**

Dados históricos com atributos: Tempo (ensolarado/nublado/chuvoso), Umidade (alta/baixa), Vento (fraco/forte), Praticar Esporte (sim/não)

```
|Tempo      |Umidade|Vento |Praticar Esporte|
|Ensolarado |Alta   |Fraco |Não             |
|Ensolarado |Alta   |Forte |Não             |
|Nublado    |Alta   |Fraco |Sim             |
|Chuvoso    |Baixa  |Fraco |Sim             |
|Chuvoso    |Alta   |Forte |Não             |
```

Atributo "Tempo" separa melhor as classes (2 não, 2 sim quando ensolarado vs 0 não, 2 sim quando nublado).

### Importância dos Atributos

A importância de um atributo está relacionada ao **quanto ele contribui para organizar os dados ao longo da árvore**.

Fatores de influência:
- Atributos usados perto da raiz tendem a impactar mais exemplos
- Atributos que aparecem várias vezes influenciam várias decisões
- Atributos que deixam grupos mais "puros" têm maior relevância

### Superfícies de Decisão

Árvores de decisão particionam o espaço em regiões retangulares (ou hiper-retangulares):
- Cada novo nível da árvore adiciona um novo corte no espaço de atributos
- Árvores mais profundas produzem superfícies mais fragmentadas e complexas
- Cada folha da árvore corresponde a uma região retangular

---

## Medidas de Impureza

### Motivação: A Busca pela Pureza

No caos dos dados, queremos encontrar a pureza. Uma divisão usando um atributo é boa se **aumenta a homogeneidade** dos subconjuntos resultantes.

Mas como medir isso? E como comparar diferentes possíveis divisões?

### Entropia

**Definição:** Entropia é uma medida de incerteza ou desordem em um conjunto de dados. Vem da teoria da informação.

**Fórmula:**

$$H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$$

Onde:
- $H(S)$ é a entropia do conjunto S
- $p_i$ é a proporção de exemplos da classe i no conjunto
- $c$ é o número total de classes
- $\log_2$ é o logaritmo na base 2

**Propriedades:**
- Varia entre 0 e log₂(c), onde c é o número de classes
- Quando H(S) = 0: conjunto é puro (todas as instâncias têm a mesma classe)
- Quando H(S) = log₂(c): máxima desordem (distribuição uniforme entre classes)
- Muda pouco para mudanças próximas de 0 ou 1
- Mais sensível a mudanças próximas de 0.5 (máxima incerteza)

### Exemplo de Entropia

**Cenário 1:** Dataset com 6 exemplos, sendo 2 positivos e 4 negativos

$$p_{positivo} = 2/6 = 0.333$$
$$p_{negativo} = 4/6 = 0.667$$
$$H = -[0.333 \times \log_2(0.333) + 0.667 \times \log_2(0.667)]$$
$$H = -[0.333 \times (-1.585) + 0.667 \times (-0.585)]$$
$$H ≈ 0.918$$

**Cenário 2:** Dataset com 6 exemplos, sendo 5 positivos e 1 negativo

$$p_{positivo} = 5/6 = 0.833$$
$$p_{negativo} = 1/6 = 0.167$$
$$H = -[0.833 \times \log_2(0.833) + 0.167 \times \log_2(0.167)]$$
$$H ≈ 0.650$$

O segundo cenário tem menor entropia (mais puro).

### Ganho de Informação

**Definição:** O Ganho de Informação mede **quanto a incerteza (entropia) diminui após dividir os dados por um atributo**.

**Fórmula:**

$$IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$$

Onde:
- $H(S)$ é a entropia do conjunto original
- $H(S_v)$ é a entropia do subconjunto v após a divisão
- $|S_v|$ é o número de exemplos em cada subconjunto
- $|S|$ é o número total de exemplos

**Interpretação:**
- IG positivo: a divisão reduz a entropia (bom!)
- IG maior: maior redução de incerteza (melhor divisão)

**Estratégia de construção:**
Escolhemos o atributo com **maior ganho de informação** para dividir em cada nó.

### Coeficiente de Gini

**Definição:** Gini mede o **grau de mistura de classes em um nó**. Quanto mais puro (homogêneo) um nó, menor seu Gini.

**Fórmula:**

$$Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$$

Onde:
- $p_i$ é a proporção de exemplos da classe i
- $c$ é o número de classes

**Propriedades:**
- Varia entre 0 e (c-1)/c
- Quando Gini = 0: conjunto é puro
- Quando Gini é máximo: distribuição uniforme entre classes
- Mede a probabilidade de erro de classificação aleatória
- Computacionalmente mais simples que entropia (não usa logaritmo)

### Exemplo de Gini

**Dataset com 10 exemplos: 5 spam, 5 não-spam**

$$Gini = 1 - [(0.5)^2 + (0.5)^2] = 1 - 0.5 = 0.5$$

(Máxima impureza para 2 classes)

**Dataset com 8 exemplos: 6 spam, 2 não-spam**

$$Gini = 1 - [(0.75)^2 + (0.25)^2] = 1 - [0.5625 + 0.0625] = 1 - 0.625 = 0.375$$

(Menos impuro)

### Impureza Ponderada Após Divisão

Quando dividimos um nó em subconjuntos, calculamos:

$$Gini_{weighted} = \frac{|Left|}{|Total|} \times Gini(Left) + \frac{|Right|}{|Total|} \times Gini(Right)$$

**Estratégia de construção:**
Escolhemos o atributo que gera a **menor impureza média ponderada**.

### Entropia vs Gini

| Aspecto | Entropia | Gini |
|---------|----------|------|
| Base teórica | Teoria da informação | Probabilidade |
| Sensibilidade | Mais sensível próximo a 0.5 | Mais uniforme |
| Computação | Requer logaritmo | Mais simples |
| Resultado prático | Árvores muito similares | Árvores muito similares |
| Uso comum | Algoritmos ID3, C4.5 | Algoritmo CART |

**Na prática:** Geralmente a árvore construída com Entropia ou Gini é muito parecida. A escolha depende da preferência e contexto do problema.

---

## Overfitting e Underfitting

### O Problema: Memorização vs Generalização

Quando deixamos a árvore crescer sem limites, ela terá a liberdade de:
- Dividir infinitamente em subconjuntos mais e mais específicos
- Criar nós até que cada folha tenha apenas 1 exemplo
- Ou até que todos os exemplos de uma folha sejam puros

**Resultado:** Erro de treinamento = 0%, mas péssima generalização em dados novos.

### Overfitting em Árvores de Decisão

**Definição:** Overfitting ocorre quando o modelo **aprende não apenas os padrões reais, mas também o ruído** nos dados.

**Sintomas:**
- Excelente desempenho no conjunto de treinamento
- Péssimo desempenho em dados novos (teste/validação)
- Árvore muito profunda e complexa
- Folhas com poucos exemplos

**Por que árvores de decisão são propensas?**
- Podem dividir infinitamente
- Não há penalidade natural para complexidade
- Facilmente memorizam detalhes que não se generalizam

### Underfitting

**Definição:** Underfitting ocorre quando o modelo é **muito simples** para captar os padrões nos dados.

**Sintomas:**
- Péssimo desempenho tanto no treinamento quanto na validação
- Árvore rasa demais (pouca profundidade)
- Alta tendência/viés (high bias)

### Estratégias para Controlar Overfitting

#### 1. Profundidade Máxima (max_depth)

Limita quantos níveis a árvore pode ter:
- Árvores rasas têm menos chance de memorizar
- Reduz overfitting, mas pode aumentar underfitting

#### 2. Número Mínimo para Dividir (min_samples_split)

Núm. mínimo de exemplos em um nó antes de permitir divisão:
- Impede divisão quando há poucos dados
- Evita criar nós muito específicos

#### 3. Número Mínimo por Folha (min_samples_leaf)

Garante que cada folha tenha pelo menos N exemplos:
- Evita folhas com 1 exemplo só
- Força mais exemplos em cada decisão final

#### 4. Poda (Pruning)

Remove nós que não trazem melhoria significativa:
- **Poda por custo-complexidade**: Remove nós se redução de erro < threshold
- **Poda reduzida**: Verifica desempenho em conjunto separado

### Regressão com Árvores de Decisão

Quando o alvo é **contínuo** (regressão), o algoritmo funciona diferentemente:

**Processo:**
- Divide os dados buscando minimizar o **erro quadrático** dentro dos nós
- Cada folha prevê a **média** dos valores no nó
- Objetivo: que valores dentro do nó sejam próximos da média

**Fórmula de divisão:**

$$minimize \sum_{i \in Left}(y_i - \bar{y}_{left})^2 + \sum_{j \in Right}(y_j - \bar{y}_{right})^2$$

Onde $\bar{y}$ é a média dos valores em cada região.

**Overfitting em regressão:**
- Se deixar crescer muito, cada folha terá 1 exemplo
- Erro de treinamento = 0
- Previsão = valores exatos observados (não generaliza)

---

## Ensemble Learning

### Conceito Fundamental

**Inspiração:** "Vox populi, vox Dei" (A voz do povo é a voz de Deus)

Ensemble Learning (Aprendizado em Comitê) é uma abordagem que combina **múltiplos preditores diferentes** para obter uma previsão melhor do que cada um isoladamente.

**Ideia central:** A combinação de várias decisões independentes é geralmente mais confiável que uma única decisão.

### Princípio de Funcionamento

1. **Diversidade:** Treinar modelos diferentes ou em subconjuntos diferentes de dados
2. **Independência:** Cada modelo comete erros em regiões diferentes
3. **Agregação:** Combinar previsões (votação, média, weighted average)
4. **Redução de erro:** Erros extremos de alguns modelos são compensados por acertos de outros

### Superfícies de Decisão em Ensembles

Enquanto uma única árvore cria fronteiras retangulares abruptas, um ensemble:
- Suaviza as transições
- Cria superfícies mais complexas e realistas
- Reduz a variância das previsões

### Estratégias de Agregação

**Para Classificação:**
- **Votação por Maioria:** Escolher a classe que mais árvores predizem
- **Votação Ponderada:** Dar pesos diferentes a cada modelo
- **Votação Probabilística:** Média das probabilidades preditas

**Para Regressão:**
- **Média Simples:** $(pred_1 + pred_2 + ... + pred_n) / n$
- **Média Ponderada:** Pesar predições por confiabilidade de cada modelo

### Bagging (Bootstrap Aggregating)

**Definição:** Técnica que treina múltiplos modelos em subconjuntos aleatórios do conjunto de dados original (com reposição - bootstrap) e agrega suas previsões.

**Processo:**

1. Criar M amostras bootstrap:
   - Selecionar n exemplos do dataset original **com reposição**
   - Repetir M vezes (cada amostra do mesmo tamanho do original)

2. Treinar um modelo em cada amostra

3. Fazer previsões:
   - Cada modelo faz uma predição
   - Agregação: votação (classificação) ou média (regressão)

**Características:**
- Cada amostra é uma variação dos dados originais
- Alguns exemplos aparecem múltiplas vezes, outros desaparecem
- Cria modelos ligeiramente diferentes

**Vantagem principal:** Reduz a **variância** mantendo o viés

**Propriedade interessante:**
- ~67% dos dados entram em cada bootstrap
- ~33% (Out-of-Bag - OOB) não entram em uma amostra específica
- OOB funciona como validação interna do modelo

### Random Forest

**Definição:** Caso especial de Bagging que combina:
- Bootstrap do conjunto de treinamento
- Seleção aleatória de atributos (features) em cada divisão

**Processo de construção:**

1. Gerar M amostras bootstrap dos dados
2. Para cada amostra:
   - Treinar uma árvore de decisão
   - **Em cada divisão, considerar apenas K atributos aleatórios**
   - Crescer árvore sem restrição (para desempenho)
3. Agregar previsões de todas as árvores

**Diferença crucial com Bagging:**
- Bagging: usa todos os atributos em cada divisão
- Random Forest: usa apenas subconjunto aleatório de atributos

**Benefício da seleção aleatória de features:**
- As árvores são **mais independentes** umas das outras
- Reduz correlação entre árvores
- Melhora agregação (menos colinearidade)
- Importante: seleção aleatória de features aparece no RF, não no bootstrapping!

### Out-of-Bag (OOB) Validation

**Conceito:** Dados que não foram selecionados no bootstrap para um determinado modelo.

**Estatística:**
- Cada árvore é treinada com ~67% dos dados originais
- Os ~33% restantes funcionam como teste para aquela árvore específica
- Permite estimar desempenho sem conjunto de validação separado

**Aplicação:**
- Validação interna do modelo
- Estimativa de importância de features
- Detecção de overfitting

### Importância de Features em Random Forest

**Conceito:** Mede quanto cada atributo contribui para as decisões do modelo.

**Cálculo:**
- Para cada feature em cada árvore: mede redução de impureza (Gini ou Entropia) gerada pelas divisões
- Média sobre todas as árvores
- Normaliza para soma = 1

**Aplicações:**
- Identificar quais variáveis mais influenciam as previsões
- Ajudar na interpretação do modelo
- Apoiar seleção ou redução de features (feature engineering)
- Detectar features irrelevantes

**Importante:** Alta importância não significa causalidade, apenas que a variável foi útil para melhorar as divisões.

### Vantagens de Random Forest em Overfitting

Ao contrário de uma árvore individual profunda:

- Cada árvore vê apenas ~67% dos dados (bootstrap)
- Cada divisão usa apenas subconjunto de features
- A previsão final é agregação de muitas árvores independentes
- **Resultado:** Random Forest é muito menos sensível a overfitting

Você pode crescer árvores muito profundas sem o risco excessivo de overfitting que uma árvore individual teria.

### Boosting

**Definição:** Técnica sequencial que treina uma série de classificadores fracos, cada um aprendendo com os erros dos anteriores.

**Conceito chave:** 

Um **aprendiz fraco (weak learner)** é um classificador ligeiramente melhor que classificação aleatória (acurácia > 50% em binário).

Um **aprendiz forte (strong learner)** é um classificador com acurácia significativamente alta.

Boosting transforma vários weak learners em um strong learner.

**Processo geral:**

1. Treinar um classificador base (weak learner)
2. Identificar exemplos que foram classificados incorretamente
3. Dar mais peso/importância a esses exemplos
4. Treinar novo classificador focando nos erros anteriores
5. Repetir sequencialmente
6. Combinar todos os classificadores (geralmente votação ponderada)

**Características:**
- **Sequencial:** Cada modelo depende do anterior
- **Focado em erros:** Novos modelos corrigem fraquezas anteriores
- **Pesos adaptativos:** Exemplos difíceis recebem mais atenção
- **Agregação ponderada:** Modelos melhores recebem pesos maiores

**Exemplos de algoritmos:**
- AdaBoost: Adaptive Boosting
- XGBoost: Extreme Gradient Boosting
- Gradient Boosting: Boosting baseado em gradientes

**Vantagem principal:** Reduz tanto variância quanto viés (bias)

**Trade-off:** Custo computacional maior que Bagging

**Limitação:** 
- Sensível a outliers e ruído
- Risco de overlearning (overfitting)
- Parâmetros precisam ser ajustados com cuidado

### Bagging vs Boosting

| Aspecto | Bagging | Boosting |
|---------|---------|----------|
| Treinamento | Paralelo/Independente | Sequencial |
| Dependência | Modelos independentes | Cada modelo depende do anterior |
| Foco | Reduz variância | Reduz viés e variância |
| Amostras | Bootstrap com reposição | Peso adaptativo |
| Agregação | Média/Votação simples | Votação ponderada |
| Sensibilidade a outliers | Robusta | Sensível |
| Tempo | Rápido (treino paralelo) | Mais lento (sequencial) |

---

## Questões de Revisão

1. **Profundidade de Árvore:** Qual é a profundidade aproximada de uma Árvore de Decisão treinada sem restrições em um dataset com um milhão de instâncias? (Resposta: log₂(n) ≈ 20 níveis)

2. **Gini dos Filhos:** A impureza Gini de um nó é geralmente menor ou maior que a de seu nó pai? (Resposta: Menor ou igual - nunca maior, pois divisões reduzem impureza)

3. **Max_depth e Overfitting:** Se uma Árvore está sofrendo overfitting no treinamento, diminuir max_depth é uma boa ideia? (Resposta: Sim, limita complexidade)

4. **Scaling e Underfitting:** Se uma Árvore está sofrendo underfitting, é boa ideia escalar os atributos de entrada? (Resposta: Não - árvores são invariantes a scaling)

---

## Referências

- CARVALHO, ANDRÉ ET AL. Inteligência Artificial - Uma Abordagem de Aprendizado de Máquina. LTC, 2011.
- GUIDO, Sarah; MULLER, ANDREAS. Introduction to Machine Learning with Python - A Guide for Data Scientists. O'Reilly Media, 2016.
- GÉRON, AURÉLIEN. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems. 2ª Edição. O'Reilly Media, 2019.
  - Capítulo 6: Decision Trees
  - Capítulo 7: Ensemble Learning and Random Forests
  - Capítulos 10-11: Training Models e Training Deep Neural Networks

---

## Glossário Técnico

- **Atributo/Feature:** Variável de entrada usado para fazer previsões
- **Bootstrap:** Amostragem com reposição dos dados
- **Classificação:** Tarefa de prever categorias discretas
- **Classe:** Categoria ou rótulo em problemas de classificação
- **Ensemble:** Grupo de múltiplos modelos treinados juntos
- **Entropia:** Medida de desordem/incerteza em um conjunto
- **Ganho de Informação:** Redução de entropia após uma divisão
- **Gini:** Medida de impureza baseada em probabilidade
- **Hyperparâmetro:** Parâmetro ajustado antes do treinamento
- **Instância:** Um exemplo individual no dataset
- **Overfitting:** Modelo memoriza dados de treino, não generaliza
- **Pruning:** Remoção de nós desnecessários da árvore
- **Regressão:** Tarefa de prever valores contínuos
- **Rótulo/Label:** Valor alvo que se quer prever
- **Underfitting:** Modelo muito simples para os dados
