import networkx as nx
import numpy as np 
from itertools import permutations
from scipy.spatial import distance_matrix

def calculate_route_distance(graph, route):
    """Calcula a distância total de um caminho."""
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i + 1]]['weight']
    return distance

# Versão 1: Algoritmo de Força Bruta (Sem GitHub Copilot)
def brute_force_tsp(graph, start_node):
    """Resolve o problema do caixeiro viajante por força bruta."""
    nodes = list(graph.nodes)
    nodes.remove(start_node)
    shortest_route = None
    min_distance = float('inf')

    for perm in permutations(nodes):
        route = [start_node] + list(perm) + [start_node]
        distance = calculate_route_distance(graph, route)
        if distance < min_distance:
            min_distance = distance
            shortest_route = route

    return shortest_route, min_distance

'''
# Versão 2: Algoritmo do Vizinho Mais Próximo (Otimizado com GitHub Copilot)
def nearest_neighbor_tsp(graph, start_node):
    """Resolve o problema do caixeiro viajante usando o Algoritmo do Vizinho Mais Próximo."""
    unvisited = set(graph.nodes)
    unvisited.remove(start_node)
    route = [start_node]
    current_node = start_node

    while unvisited:
        nearest_node = min(unvisited, key=lambda node: graph[current_node][node]['weight'])
        route.append(nearest_node)
        unvisited.remove(nearest_node)
        current_node = nearest_node

    route.append(start_node)  # Retorna ao ponto de partida
    return route, calculate_route_distance(graph, route)
'''

# Criando o grafo com cidades e distâncias
graph = nx.Graph()
cities = ['A', 'B', 'C', 'D']
distances = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20,
    ('B', 'C'): 35, ('B', 'D'): 25,
    ('C', 'D'): 30
}

for (city1, city2), distance in distances.items():
    graph.add_edge(city1, city2, weight=distance)

# Comparação das duas versões
brute_route, brute_distance = brute_force_tsp(graph, 'A')
#nearest_route, nearest_distance = nearest_neighbor_tsp(graph, 'A')

print(f"Força Bruta - Melhor Rota: {brute_route}, Distância: {brute_distance}")
#print(f"Vizinho Mais Próximo - Melhor Rota: {nearest_route}, Distância: {nearest_distance}")