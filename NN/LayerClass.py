from NeuronClass import *

# Class representing hidden or output layer


class Layer():

    MAP_INP_ALL         = 0
    MAP_INP_RANGE       = 1
    MAP_INP_RANGES      = 1
    MAP_INP_ITEM        = 2

    def __init__(self, layer_map_list):
        self.neurons_list = neurons_list
        self.layer_map_list = layer_map_list


    # List (vector) of input data
    # returns output of layer = [list of nodes outputs]
    def procesinput(self, input_list = []):
        start_index = 0
        layer_output_list = []
        for neuron in self.neurons_list:
            input_sublist = input_list[start_index:neuron.numberOfInputs]
            layer_output_list.append(neuron.ProcessInput(input_sublist))
            start_index = neuron.numberOfInputs
        return layer_output_list

    def getneuroninputlist(self,layer_input_list,neuron_map_list):
        neuron_input_list = []
        for inp_map in neuron_map_list:
            neuron_input_list.extend(inp_map[0](layer_input_list,inp_map[1]))
        return neuron_input_list

    @staticmethod
    def selectinputall(input_list,dummy):
        return input_list

    @staticmethod
    def selectinputrange(input_list,range):
        return input_list[range[0]:range[0]]

    @staticmethod
    def selectinputranges( input_list, range_list):
        input_subset = []
        for range in range_list:
            input_subset.extend(Layer.selectinputrange(input_list,range))
        return input_subset

    @staticmethod
    def selectinputelement(input_list,idx):
        return input_list[idx]