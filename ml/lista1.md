# 📝 Resumo de Estudos: Aprendizado de Máquina - Árvores de Decisão

## Questão 1: Entropia e Ganho de Informação (E-mail Spam)

- **Entropia Total**: O conjunto possui 8 e-mails (4 Spam / 4 Não Spam). Como as classes estão equilibradas ($50\%$ cada), a **Entropia Inicial é 1.0**.
- **Divisão por "Palavra-chave"**:
    - **Ramo Contém**: 4 exemplos (3 Spam / 1 Não Spam). Entropia $\approx 0.811$.
    - **Ramo Não Contém**: 4 exemplos (1 Spam / 3 Não Spam). Entropia $\approx 0.811$.
- **Ganho de Informação ($GI$)**:
    - Cálculo: $1.0 - [(\frac{4}{8} \cdot 0.811) + (\frac{4}{8} \cdot 0.811)] = \mathbf{0.189}$.
- **Processo Recursivo**: O algoritmo é recursivo porque, após a primeira divisão, os subconjuntos ainda não estão "puros" ($H > 0$). Ele continua criando **Nós de Decisão** até atingir **Nós Folha** (puros) ou um critério de parada (como profundidade máxima).

---

## Questão 2: Comparação de Impureza (Gini vs. Entropia)

- **Cenário 1 (7 Classe A / 3 Classe B)**:
    - **Entropia**: $\approx 0.881$ | **Gini**: $0.42$
- **Cenário 2 (5 Classe A / 5 Classe B)**:
    - **Entropia**: $1.0$ | **Gini**: $0.5$
- **Análise de Impureza**: O cenário **5/5** apresenta maior impureza, pois as classes estão totalmente misturadas, representando a incerteza máxima do modelo.
- **Eficiência Computacional**: O **Coeficiente de Gini** é mais eficiente porque utiliza apenas operações aritméticas simples, enquanto a **Entropia** exige o cálculo de logaritmos, que demandam mais processamento.

---

## Questão 3: Interpretação de Árvore (Crédito)

- **Atributo Influente**: A **Renda** é o atributo mais importante, pois está na **Raiz** da árvore. Ela sozinha consegue definir a aprovação imediata para rendas $> 5000$.
- **Importância da Raiz**: Atributos próximos à raiz apresentam o **maior Ganho de Informação** ou a **maior redução de Gini** no conjunto total de dados.
- **Vantagens vs. Redes Neurais**:
    - **Explicabilidade**: Árvores são modelos "caixa-branca", fáceis de interpretar.
    - **Simplicidade**: Não exigem normalização de dados e são rápidas para treinar em dados tabulares.

---

## Questão 4: Overfitting e Hiperparâmetros

- **Identificação**: O **Modelo C** sofre de overfitting (Acurácia Treino: $100\%$ / Teste: $68\%$). Ele "decorou" os dados de treino e perdeu a capacidade de generalizar.
- **Causas**: Árvores muito profundas (`max_depth` alto) capturam ruídos e exceções do treino como se fossem regras gerais.
- **Controle (Hiperparâmetros)**:
    - `min_samples_split`: Mínimo de exemplos necessários para permitir uma nova divisão em um nó.
    - `min_samples_leaf`: Mínimo de exemplos que uma folha deve conter, evitando regras baseadas em casos isolados.

---

## Questão 5: Árvore de Regressão (Salários)

- **Diferença Chave**: Em vez de classes (Sim/Não), prevemos um **número contínuo**. A predição da folha é a **média** dos valores naquele nó.
- **Divisão (Experiência $\le 3$)**:
    - **Média Grupo 1 ($\le 3$)**: $(30+35+40)/3 = \mathbf{35}$ mil.
    - **Média Grupo 2 ($> 3$)**: $(70+75+80)/3 = \mathbf{75}$ mil.
- **Erro Quadrático**: O objetivo é minimizar a variância interna dos nós. Se cada folha tiver apenas um exemplo, o erro de treino será zero, mas o modelo sofrerá de **overfitting extremo**.

---
