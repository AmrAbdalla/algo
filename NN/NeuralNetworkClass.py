from NeuralNetworkConfig import *

# Class representing the whole neural network


class NeuralNetwork():
    NUMBER_OF_HIDDEN_LAYERS = 2
    NUMBER_OF_INPUTS = 20
    NUMBER_OF_OUTPUTS = 3

    def __init__(self, layers_list = [0 for i in range(NUMBER_OF_HIDDEN_LAYERS)]):
        self.layers_list = layers_list