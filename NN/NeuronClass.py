import random
import math

# Class representing neural network node


class Neuron():

    def __init__(self, activation_func, num_inputs, bias = 1):
        self.activation_func = activation_func
        self.num_inputs = num_inputs
        self.weights_list = []
        for i in range(num_inputs):
            self.weights_list.append(random.uniform(1,10))
        self.bias = bias

    # List (vector) of input data
    # returns output of node = f(Wp + bias)
    def processinput(self, input_list = []):
        sum = self.bias
        for i in range(self.num_inputs):
            sum = sum + (input_list[i] * self.weights_list[i])
        return self.activation_func(sum)

    # ret = 0  val < 0,  ret = 1  val >= 0
    @staticmethod
    def hardlim(self, val):
        ret_val = 1
        if val < 0:
            ret_val = 0
        return ret_val

    # ret = -1  val < 0,  ret = +1  val >= 0
    @staticmethod
    def hardlims(self, val):
        ret_val = 1
        if val < 0:
            ret_val = -1
        return ret_val

    # ret = val
    @staticmethod
    def purelin(self, val):
        return val

    # ret = 0  val < 0,  ret = val   0 <= val
    @staticmethod
    def poslin(self, val):
        if val < 0:
            ret_val = 0
        else:
            ret_val = val
        return ret_val

    # ret = 0  val < 0,  ret = val   0 <= val <= 1, ret = 1  val > 1
    @staticmethod
    def satlin(self, val):
        if val < 0 :
            ret_val = 0
        elif val > 1 :
            ret_val = 1
        else:
            ret_val = val
        return ret_val

    # ret = -1  val < -1,  ret = val   -1 <= val <= 1, ret = 1  val > 1
    @staticmethod
    def satlins(self, val):
        if val < -1:
            ret_val = -1
        elif val > 1:
            ret_val = 1
        else:
            ret_val = val
        return ret_val

    # ret = 1/(1 + exp(val))
    @staticmethod
    def logsig(self, val):
        return 1 / (1 + math.exp(-val))

    # ret = (exp(val) - exp(-val))/(exp(val) + exp(-val))
    @staticmethod
    def tansig(self, val):
        return (math.exp(val) - math.exp(-val)) / (math.exp(val) + math.exp(-val))