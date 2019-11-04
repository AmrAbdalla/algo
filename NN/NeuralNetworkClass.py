from NeuralNetworkConfig import *

# Class representing the whole neural network


class NeuralNetwork():
    NUMBER_OF_HIDDEN_LAYERS = 2
    NUMBER_OF_INPUTS = 20
    NUMBER_OF_OUTPUTS = 3

    def __init__(self):
        self.layers_list = []
        self.num_layers = len(network)
        for i in range(self.num_layers):
            self.layers_list.append(Layer(network(i),input_map_list(i)))