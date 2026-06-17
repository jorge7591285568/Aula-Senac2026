import heapq
from typing import List, Dict, Tuple

# Biblioteca: heapq - para algoritmo de ordenação eficiente (min-heap)
# Biblioteca: typing - para tipos explícitos (List, Dict, Tuple)

def dijkstra(
    grafo: Dict[int, List[Tuple[int, float]]],
    inicio: int,
    fim: int
) -> Tuple[List[int], float]:
    """
    Implementa o algoritmo de Dijkstra para encontrar o caminho mais curto.
    
    Args:
        grafo: Dicionário onde grafo[u] = [(v, peso), ...] representa
               arestas de u para v com peso
        inicio: Nodo de partida
        fim: Nodo de destino
    
    Returns:
        (caminho, distancia) - Lista de nodos e distância total
    """
    
    # Inicializa distâncias com infinito para todos os nodos
    distancias: Dict[int, float] = {node: float('inf') for node in grafo}
    distancias[inicio] = 0
    
    # Prédecessor para reconstruir o caminho
    predecessores: Dict[int, int] = {node: None for node in grafo}
    
    # Min-heap: (distancia, nodo)
    heap: List[Tuple[float, int]] = [(0, inicio)]
    
    # Nodos visitados
    visitados: set = set()
    
    while heap:
        distancia_atual, nodo_atual = heapq.heappop(heap)
        
        if nodo_atual in visitados:
            continue
        
        visitados.add(nodo_atual)
        
        if nodo_atual == fim:
            break
        
        # Explora vizinhos
        for vizinho, peso in grafo.get(nodo_atual, []):
            if vizinho in visitados:
                continue
            
            nova_distancia = distancia_atual + peso
            
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                predecessores[vizinho] = nodo_atual
                heapq.heappush(heap, (nova_distancia, vizinho))
    
    # Reconstrói o caminho de fim para início
    caminho: List[int] = []
    nodo = fim
    
    while nodo is not None:
        caminho.append(nodo)
        nodo = predecessores[nodo]
    
    caminho.reverse()
    
    if caminho[0] != inicio:
        return [], float('inf')
    
    return caminho, distancias[fim]


# Exemplo de uso
if __name__ == "__main__":
    # Grafo de exemplo: nodo -> [(vizinho, peso), ...]
    grafo_exemplo = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    
    caminho, distancia = dijkstra(grafo_exemplo, 0, 3)
    
    if caminho:
        print(f"Caminho mais curto: {caminho}")
        print(f"Distância total: {distancia}")
    else:
        print("Não existe caminho entre os nodos")