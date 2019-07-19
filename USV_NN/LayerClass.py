from NeuronClass import *

class Layer():
    def __init__(self, neurons_list = []):
        self.neurons_list = neurons_list


    # List (vector) of input data
    # returns output of layer = [list of nodes outputs]
    def UpdateLayer(self, input_list = [], input_map = []):
        start_index = 0
        layer_output_list = []
        for neuron in self.neurons_list:
            input_sublist = input_list[start_index:neuron.numberOfInputs]
            layer_output_list.append(neuron.ProcessInput(input_sublist))
            start_index = neuron.numberOfInputs
        return layer_output_list