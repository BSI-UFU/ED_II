
# AstroSim - Fase 2: Módulos de Busca, Compressão e Hashing

## Arquitetura Geral

A Fase 2 do projeto **AstroSim** expande a aplicação com foco em algoritmos clássicos de Estrutura de Dados II. A arquitetura é composta por múltiplos módulos GUI (Tkinter com ttkbootstrap), cada um responsável por uma funcionalidade distinta:

- **main_window.py**: Interface principal que orquestra os módulos.
- **inventory_gui.py / inventory_manager.py**: Gerencia um inventário de componentes espaciais, com suporte a busca sequencial e binária.
- **text_search_windows.py**: Permite busca de padrões em textos com o algoritmo de Rabin-Karp.
- **data_transmission_gui.py / compressaoHuffman.py**: Comprime e descomprime mensagens usando o algoritmo de Huffman.
- **hashing.py**: Implementa múltiplas funções de hash e estratégias de tratamento de colisão.

Todos os módulos são integrados por meio da interface gráfica e se comunicam com estruturas internas ou banco de dados para simulação, análise e visualização de dados.

---

## Algoritmos Implementados e Integração

### 1. Busca Sequencial
- **Arquivo**: `buscaSequencial.py`
- **Descrição**: Percorre linearmente a lista até encontrar a chave buscada.
- **Uso**: Na GUI do inventário, permite buscar por código, nome ou categoria.
- **Complexidade**:
  - Melhor caso: **O(1)** (primeiro elemento)
  - Pior caso: **O(n)**
- **Eficiência**: Baixa em listas grandes, mas útil para dados não ordenados.

---

### 2. Busca Binária Iterativa
- **Arquivo**: `pesquisaBinariaIterativa.py`
- **Descrição**: Divide o vetor ordenado ao meio repetidamente até encontrar o item.
- **Uso**: Utilizado em listas ordenadas do inventário para acelerar a busca.
	A lista de componentes (todos) é ordenada com base em um atributo específico do componente, 
	como cod_invent, nome ou categoria, dependendo do que o usuário escolheu para a busca.
	Trecho do código: lista_ordenada = sorted(todos, key=key_func)  # Ordena a lista de componentes com base no atributo selecionado
- **Pré-requisito**: Lista deve estar ordenada por chave de busca.
- **Complexidade**:
  - Melhor caso: **O(1)**
  - Pior caso: **O(log n)**
- **Eficiência**: Alta, ideal para grandes volumes de dados ordenados.

---

### 3. Algoritmo de Rabin-Karp
- **Arquivo**: `pesquisaRabinKarp.py`
- **Descrição**: Usa função hash para buscar padrões em strings de forma eficiente.
- **Uso**: Módulo `text_search_windows.py` permite buscas rápidas em documentos ou logs.
- **Complexidade**:
  - Esperado: **O(n + m)** (n: texto, m: padrão)
  - Pior caso (muitas colisões): **O(nm)**
- **Eficiência**: Muito bom para múltiplas buscas em grandes textos.

---

### 4. Compressão e Descompressão de Huffman
- **Arquivo**: `compressaoHuffman.py`
- **Descrição**: Gera árvore binária com base na frequência de caracteres para criar códigos prefixados ideais.
- **Uso**: Em `data_transmission_gui.py`, permite compactar e transmitir mensagens reduzindo o tamanho.
- **Complexidade**:
  - Construção: **O(n log n)**
  - Compressão/Descompressão: **O(n)**
- **Eficiência**: Alta compressão para textos com muitos caracteres repetidos.

---

### 5. Hashing com Múltiplas Funções
- **Arquivo**: `hashing.py`
- **Descrição**: Implementa diversas funções hash para transformar chaves em índices.
  - **Funções implementadas**:
    - Divisão: `h(k) = k mod m`
    - Multiplicação
    - Meio-quadrado
    - Raiz
    - Extração de dígitos
    - XOR + Compressão
    - Rotação de bits
    - Atribuição de peso posicional
- **Colisões**:
  - **Encadeamento separado** (listas encadeadas em cada posição)
  - **Endereçamento aberto** com rehash
- **Uso**: Integrável ao inventário ou ao módulo de autenticação de dados.
- **Complexidade**:
  - Média: **O(1)**
  - Pior caso (colisões): **O(n)**
- **Eficiência**: Muito rápida com boa função hash e baixa taxa de colisão.

---

## Comparativo de Desempenho (Testes Empíricos)

| Algoritmo      | Tempo Médio | Eficiência Observada |
|----------------|-------------|-----------------------|
| Sequencial     | Alto        | Linear, ineficiente para grandes listas |
| Binária        | Baixo       | Muito rápido com listas ordenadas |
| Rabin-Karp     | Médio       | Eficiente com múltiplos padrões |
| Huffman        | Médio       | Ótima taxa de compressão |
| Hashing        | Muito Baixo | Melhor desempenho geral |

---

## Estrutura dos Arquivos

```
├── main.py                       # Inicializa o aplicativo AstroSim
├── main_window.py               # Interface principal
├── inventory_gui.py             # GUI de inventário com busca
├── inventory_manager.py         # Controle de dados e banco de dados
├── buscaSequencial.py           # Algoritmo de busca linear
├── pesquisaBinariaIterativa.py  # Algoritmo de busca binária
├── pesquisaRabinKarp.py         # Busca eficiente por padrões em texto
├── compressaoHuffman.py         # Compressão/descompressão
├── hashing.py                   # Funções hash e tratamento de colisões
├── data_transmission_gui.py     # Interface de transmissão de dados
├── text_search_windows.py       # Interface de busca textual com Rabin-Karp
```

---

## Conclusão

A Fase 2 do AstroSim integra diversos algoritmos fundamentais em um ambiente interativo, didático e modular. Cada algoritmo foi aplicado de forma prática, com suporte à visualização de desempenho e impacto em cenários reais simulados.
