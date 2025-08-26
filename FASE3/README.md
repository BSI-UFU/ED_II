# 🚀 Projeto ASTROSIM_GUI  

Simulador interativo para **planejamento de missões espaciais**, com suporte a **busca, compressão e algoritmos de grafos** aplicados à navegação interplanetária, inventário de componentes e transmissão de dados.

---

## 🏗️ Arquitetura Geral

O projeto é organizado em três blocos principais:

ASTROSIM_GUI/
│
├── gui/ # Interfaces gráficas
│ ├── main_window.py # Janela principal
│ ├── space_map_gui.py # Visualização e interação com grafos espaciais
│ ├── mission_planner_gui.py
│ ├── inventory_gui.py
│ └── ...
│
├── images/ # Recursos visuais
│ ├── et.png
│ └── spaceTravel.png
│
├── modules/ # Algoritmos e lógica central
│ ├── buscaDFS.py
│ ├── buscaBFS.py
│ ├── buscaSequencial.py
│ ├── pesquisaRabinKarp.py
│ ├── hashing.py
│ ├── compressaoHuffman.py
│ ├── dijkstra.py
│ ├── ArvoreGeradoraMinima.py
│ ├── ordenacaoTopologica.py
│ ├── coloracao.py
│ └── ...
│
└── main.py # Ponto de entrada do sistema


📌 **Fluxo Básico:**  
- O usuário interage com a **interface gráfica (gui/)**.  
- A interface aciona os **algoritmos (modules/)** conforme a ação escolhida.  
- Os resultados são exibidos em telas interativas (mapa espacial, inventário, relatórios etc.).

---

## 🔍 Algoritmos Implementados e Funcionalidades

### 🔎 Algoritmos de Busca
**Módulos:** `buscaSequencial.py`, `pesquisaBinariaIterativa.py`, `hashing.py`, `pesquisaRabinKarp.py`

- **Busca Sequencial**: procura em listas desordenadas.  
- **Busca Binária**: procura eficiente em listas ordenadas.  
- **Rabin-Karp**: busca em documentos de missão/logs.  
- **Hashing**: acesso rápido via chave hash.  

---

### 📡 Compressão de Dados
**Módulo:** `compressaoHuffman.py`

- **Huffman**: compressão de mensagens e logs científicos para reduzir custo energético de transmissão.  
- Suporte para comparação de taxa de compressão.  

---

### 🌌 Grafos e Rotas Espaciais
**Módulos:** `buscaDFS.py`, `buscaBFS.py`, `dijkstra.py`, `ArvoreGeradoraMinima.py`, `coloracao.py`, `ordenacaoTopologica.py`

- **DFS**: exploração profunda de rotas espaciais.  
- **BFS**: menor caminho em grafos não ponderados.  
- **Dijkstra**: caminho mínimo em grafos ponderados (energia, tempo).  
- **Árvore Geradora Mínima (Prim/Kruskal)**: conexão mínima entre sondas.  
- **Coloração (Welch-Powell)**: minimizar conflitos de recursos.  
- **Ordenação Topológica (Tarjan/Kahn)**: dependências entre etapas da missão.  

---

## 📈 Complexidade e Eficiência

| Algoritmo        | Aplicação                      | Complexidade     | Eficiência esperada           |
|------------------|--------------------------------|------------------|-------------------------------|
| **Sequencial**   | Inventário simples             | `O(n)`           | Boa para listas pequenas      |
| **Binária**      | Inventário ordenado            | `O(log n)`       | Muito eficiente               |
| **Rabin-Karp**   | Logs de missão                 | `O(n+m)` médio   | Bom para grandes textos       |
| **Hashing**      | Inventário rápido              | `O(1)` médio     | Excelente para acesso direto  |
| **Huffman**      | Compressão                     | `O(n log n)`     | Reduz custo de transmissão    |
| **DFS**          | Exploração                     | `O(V+E)`         | Útil em mapas grandes         |
| **BFS**          | Caminho mínimo (não ponderado) | `O(V+E)`         | Excelente em grafos densos    |
| **Dijkstra**     | Caminho mínimo (ponderado)     | `O((V+E) log V)` | Ideal para custos energéticos |
| **AGM**          | Conectividade mínima           | `O(E log V)`     | Bom para redes de sondas      |
| **Coloração**    | Conflitos                      | `O(V²)`          | Aceitável em grafos médios    |
| **Ordenação Topológica**                          | Dependências     | `O(V+E)` | Muito eficiente    |

---

## 🎯 Conclusão

O **ASTROSIM_GUI** integra algoritmos de **busca, compressão e grafos** em um ambiente gráfico para auxiliar:  

- 🛰️ **Navegação Interplanetária** (rotas, custos, conexões)  
- 📡 **Transmissão de Dados** (compressão eficiente)  
- 📦 **Gestão de Inventário** (buscas rápidas e organizadas)  

Esse ecossistema fornece uma **ferramenta educacional e de simulação** para estudar algoritmos aplicados em cenários reais de **exploração espacial**.

---
