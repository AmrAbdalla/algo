import math
from collections import defaultdict
from Parameters import *


def FindOptimalPath(layers,start,goal):
    predecessors = {}
    distances = {}
    path = []
    predecessors[start] = None
    distances[start] = 0.0
    distances[goal] = float('inf')

    for layer in layers:
        vertices = layer.GetLayerVertices()
        for vertex in vertices:
            distances[vertex] = float('inf')

    first_layer_vertices = layers[0].GetLayerVertices()
    for vertex in first_layer_vertices:
        dist = distances[start] + CalculateCost(start, vertex)
        if dist < distances[vertex]:
            distances[vertex] = dist
            predecessors[vertex] = start

    for i in range(len(layers) - 1):
        current_layer = layers[i]
        current_layer_vertices = current_layer.GetLayerVertices()
        next_layer = layers[i + 1]
        next_layer_vertices = next_layer.GetLayerVertices()

        for current_vertex in current_layer_vertices:
            for next_vertex in next_layer_vertices:
                dist = distances[current_vertex] + CalculateCost(current_vertex,next_vertex)
                if dist < distances[next_vertex]:
                    distances[next_vertex] = dist
                    predecessors[next_vertex] = current_vertex


    last_layer_vertices = layers[len(layers) - 1].GetLayerVertices()
    for vertex in last_layer_vertices:
        dist = distances[vertex] + CalculateCost(vertex,goal)
        if dist < distances[goal]:
            distances[goal] = dist
            predecessors[goal] = vertex

    current_node = goal
    while current_node is not None:
        path.insert(0,current_node)
        current_node = predecessors[current_node]
    return path


def CalculateCost(currentVertex,nextVertex):
    c_action = W_ACTION * math.exp(abs(nextVertex[1] - currentVertex[1])/LATERAL_SHIFT)
    c_offset = nextVertex[1]
    c_object = nextVertex[2]
    return (c_action + c_offset + c_object)


global num
num = 0