# 🧭 Projeto: Busca em Labirintos

---

## 📜 Introdução

Este projeto implementa três algoritmos clássicos de busca aplicados em um labirinto:

- 🔍 **Busca em Largura (BFS):** Explora os nós mais próximos da origem primeiro, garantindo encontrar o menor caminho.
- 🌲 **Busca em Profundidade (DFS):** Explora um caminho até o final antes de retroceder e explorar alternativas.
- ⭐ **Busca A* (A-estrela):** Combina o custo acumulado com uma heurística para encontrar o menor caminho com maior eficiência.

O objetivo é que o agente navegue no labirinto e exiba visualmente os caminhos visitados de acordo com o algoritmo escolhido.

---

## 🛠️ Estrutura do Projeto

| Arquivo         | Função                                                                 |
|------------------|------------------------------------------------------------------------|
| `labirinto.py`   | Define o ambiente do labirinto e os métodos para verificar movimentos. |
| `busca.py`       | Implementa os algoritmos BFS, DFS e A*.                                |
| `agente.py`      | Representa o agente que realiza as buscas.                             |
| `main.py`        | Integra tudo e gerencia a interface visual com Pygame.                |

---

## 🧩 Algoritmos Implementados

### 🔍 **Busca em Largura (BFS)**
- Utiliza uma fila para explorar os caminhos sistematicamente.
- ✅ Garante o menor caminho.
- 📉 Desempenho limitado em labirintos grandes.

### 🌲 **Busca em Profundidade (DFS)**
- Utiliza uma pilha para explorar profundamente antes de retroceder.
- 🚀 Rápido em ambientes pequenos.
- ❌ Nem sempre encontra o menor caminho.

### ⭐ **Busca A* (A-estrela)**
- Combina os benefícios de BFS com uma heurística (distância Manhattan).
- 🏆 Sempre encontra o menor caminho com menor custo.
- 🧠 Inteligente e eficiente.

---

## 🎨 Visualização

Os algoritmos são visualizados com Pygame:
- 🟩 **Verde** para BFS.
- 🟥 **Vermelho** para DFS.
- 🟥 **Vermelho** para A*.

---

## 📊 Comparação dos Algoritmos

| Critério             | 🔍 BFS                          | 🌲 DFS                        | ⭐ A*                          |
|----------------------|----------------------------------|------------------------------|-------------------------------|
| **Velocidade**        | Mais lenta (explora tudo)       | Mais rápida em ambientes pequenos | Rápida e eficiente             |
| **Caminho Encontrado**| Garante o menor caminho         | Nem sempre o menor           | Sempre o menor caminho         |
| **Espaço Visitado**   | Explora toda a área até o objetivo | Explora profundamente primeiro | Explora o essencial (heurística) |
| **Visualização**      | 🟩 Rastro progressivo em verde  | 🟥 Rastro progressivo em vermelho |  🟥 Rastro progressivo em vermelho |

---

## 🚀 Como Executar

1. Clone este repositório:
    ```bash
   git clone https://github.com/joaovitormelo7/projetoIA-pygame.git

2. Instale as dependências:
    ```bash
    pip install pygame

3. Execute o projeto:
    ```bash
    python3 main.py || python main.py