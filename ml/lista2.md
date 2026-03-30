### **Questão 16: Bagging (Bootstrap Aggregating)**
* **a) O que é e o que resolve:** Técnica de *ensemble* onde vários modelos idênticos são treinados independentemente em subconjuntos diferentes dos dados. Resolve o problema de **alta variância** (instabilidade) de modelos como árvores de decisão.
* **b) Variância vs. Viés:** Reduz a variância porque a média de modelos independentes cancela erros aleatórios. Não reduz necessariamente o viés; se o modelo base for simples, a média de vários modelos simples ainda será limitada.
* **c) Exemplos:** Random Forest e Bagged Decision Trees.
* **d) Papel do Bootstrap:** Gera **diversidade**. Amostrando com reposição, cada modelo vê dados ligeiramente diferentes, garantindo que não sejam idênticos.

### **Questão 17: Random Forest (RF)**
* **a) RF vs. Árvore Simples:** Árvore simples usa todos os dados e atributos; RF treina várias árvores com subconjuntos aleatórios de dados e colunas.
* **b) Subconjunto de Atributos:** Serve para **descorrelacionar** as árvores. Isso evita que um atributo dominante controle todas as divisões, forçando o modelo a aprender outros padrões.
* **c) Vantagens:** Mais robustez a ruídos e maior precisão (generalização) em dados novos.
* **d) Impacto do `n_estimators`:** Aumenta a acurácia (até estabilizar) e o tempo de treinamento cresce proporcionalmente.

### **Questão 18: Overfitting em RF**
* **a) Risco:** Sim, apesar da resistência, RF pode decorar ruídos se o dataset for pequeno e as árvores muito profundas.
* **b) `max_depth`:** Controla a complexidade; profundidade maior aumenta o risco de overfitting.
* **c) Bagging e Overfitting:** Bagging mitiga o overfitting ao tirar a média de modelos independentes, suavizando decisões extremas.
* **d) Hiperparâmetros:** `max_depth` e `min_samples_split`.

### **Questão 19: Importância de Variáveis**
* **a) Cálculo:** Mede-se a redução média da impureza (Gini ou MSE) que cada variável proporciona ao longo de todas as árvores.
* **b) Influência:** Exemplo: **Idade (0.40)** tem maior influência por apresentar o maior valor de importância acumulada.
* **c) Remover baixa importância?** Nem sempre. Um atributo pode ser pouco importante sozinho, mas essencial em conjunto com outro.
* **d) Situações enganosas:** Variáveis altamente correlacionadas ou com alta cardinalidade podem distorcer a importância.

### **Questão 20: Boosting vs. Bagging**
* **a) Diferença:** Bagging treina modelos em **paralelo** (independentes); Boosting treina em **sequência**, cada modelo corrige o erro do anterior.
* **b) Algoritmos:** XGBoost e AdaBoost.
* **c) Erros:** Boosting aumenta o peso/foco nas instâncias que o modelo anterior errou.
* **d) Viés e Variância:** Boosting reduz o viés ao forçar modelos simples a ficarem mais complexos sequencialmente; Bagging reduz apenas a variância pela média.

### **Questão 21: Out-of-Bag (OOB)**
* **a) Conceito:** Amostras não selecionadas para o treino de uma árvore específica devido ao Bootstrap.
* **b) Acurácia:** Amostras OOB testam cada árvore em dados "nunca vistos", gerando erro de validação automático.
* **c) Vantagem/Limitação:** **Vantagem:** Não precisa separar dados de teste. **Limitação:** Pode subestimar o erro em datasets pequenos.
* **d) Por que não vê tudo?** Para manter independência e diversidade entre as árvores.

### **Questão 22: Hiperparâmetros**
* **a) `n_estimators`:** Aumenta a estabilidade e reduz a variância do conjunto.
* **b) Reduzir `max_depth`:** Simplifica o modelo e combate o overfitting.
* **c) `max_features`:** Menos atributos por corte aumentam a diversidade e ajudam na generalização.
* **d) Exemplo:** `max_depth` baixo + `min_samples_split` alto.

### **Questão 24: RF para Regressão**
* **a) Previsão final:** Média aritmética das previsões de todas as árvores.
* **b) Vantagem:** Reduz impacto de *outliers* e gera predição mais suave que uma única árvore.
* **c) Critério (MSE):** Busca divisões que minimizam a soma dos erros quadráticos nos nós resultantes.

### **Questão 25: Cenário Real**
* **a) Escolha:** **Boosting** (XGBoost/LightGBM) costuma ser superior em datasets grandes (100k) e desbalanceados.
* **b) Desbalanceamento em RF:** Usar pesos de classe (`class_weight='balanced'`).

* **c) Boosting supera RF:** Quando é necessário baixo viés para capturar padrões sutis.

* **d) Bagging preferível:** Quando há muito ruído nos dados (Boosting pode aprender o ruído e sofrer overfitting).
