Monte graficamente o comportamento dos piores, melhores e casos médios dos algoritmos da busca linear e insertion sort

Guia Prático: Visualização Empírica de Complexidade Assintótica
1. Objetivo
O objetivo desta atividade é validar experimentalmente a complexidade teórica dos algoritmos Busca Linear e Insertion Sort. Você irá implementar os algoritmos, medir o tempo de execução para diferentes tamanhos de entrada (n) e plotar gráficos para comparar os resultados com as curvas assintóticas esperadas.

2. Algoritmos e Cenários
Para cada algoritmo, devemos testar três configurações de arrays:

- Melhor Caso
- Pior Caso
- Caso Médio

* Busca Linear

Elemento na 1ª posição.
Elemento ausente ou na última posição.
Elemento em posição aleatória.

* Insertion Sort
Array já ordenado.
Array ordenado em ordem reversa.
Array com elementos aleatórios.


3. Roteiro de Implementação
Passo 1: Gerador de Entradas

Crie uma função que gere arrays de tamanhos variados (ex: n = [100, 500, 1000, 5000, 10000]). Para o Insertion Sort, em entradas muito grandes (acima de 20.000), o tempo pode crescer drasticamente devido à natureza quadrática O(n^2), então escolha os limites com cuidado.

Passo 2: Medição de Tempo
Não use o relógio de parede! Utilize funções de alta precisão da sua linguagem (como time.perf_counter() em Python ou console.time() em JavaScript).
Dica: Para evitar ruídos do sistema operacional, execute cada teste 5 ou 10 vezes para o mesmo n e tire a média.



Passo 3: Plotagem
Utilize bibliotecas gráficas (Matplotlib para Python, Chart.js para JS) para gerar dois gráficos distintos:
Eixo X: Tamanho do Array (n).
Eixo Y: Tempo de execução (milissegundos ou segundos).

4. O que se espera ver nos gráficos?
Busca Linear: Você deverá ver linhas retas. Mesmo no pior caso, o crescimento deve ser constante e proporcional a n, caracterizando O(n).
Insertion Sort: No Melhor Caso, a curva será linear (O(n)).
No Pior e Médio Caso, você verá uma parábola acentuada, refletindo o crescimento quadrático (O(n^2)). Note como, à medida que n dobra, o tempo de execução aproximadamente quadruplica.

5. Perguntas para o Relatório
A curva do "Caso Médio" do Insertion Sort ficou mais próxima do Melhor ou do Pior caso? Por quê?
Houve algum "ruído" nos gráficos (picos de tempo inesperados)? O que pode ter causado isso no hardware?
A partir de qual valor de n a diferença de performance entre a Busca Linear e o Insertion Sort (Pior Caso) torna o algoritmo de ordenação impraticável para uso em tempo real?

