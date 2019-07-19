import random
import math


class Neuron():

    ACTVN_FN_HARDLIM  = 0
    ACTVN_FN_HARDLIMS = 1
    ACTVN_FN_PURELIN  = 2
    ACTVN_FN_POSLIN   = 3
    ACTVN_FN_SATLIN   = 4
    ACTVN_FN_SATLINS  = 5
    ACTVN_FN_LOGSIG   = 6
    ACTVN_FN_TANSIG   = 7

    def __init__(self, activation_func, numberOfInputs = 1, bias = random.uniform(1,10)):
        self.activation_func = activation_func
        self.numberOfInputs = numberOfInputs
        self.weights_list
        for i in range(numberOfInputs):
            self.weights_list.append(random.uniform(1,10))
        self.bias = bias

    # List (vector) of input data
    # returns output of node = f(Wp + bias)
    def ProcessInput(self, input_list = []):
        sum = self.bias
        for i in range(self.numberOfInputs):
            sum = sum + (input_list[i] * self.weights_list[i])
        return self.activation_func(sum)

    def executeActivationFun(self,func_idx):
        if func_idx ==   Neuron.ACTVN_FN_HARDLIM:
            hardlim(func_idx)
        elif func_idx == Neuron.ACTVN_FN_HARDLIMS:
            hardlims(func_idx)
        elif func_idx == Neuron.ACTVN_FN_PURELIN:
            purelin(func_idx)
        elif func_idx == Neuron.ACTVN_FN_POSLIN:
            poslin()
        elif func_idx == Neuron.ACTVN_FN_SATLIN:
            satlin()
        elif func_idx == Neuron.ACTVN_FN_SATLINS:
            satlins()
        elif func_idx == Neuron.ACTVN_FN_LOGSIG:
            logsig()
        elif func_idx == Neuron.ACTVN_FN_TANSIG:
            tansig
:

    @staticmethod
    def hardlim(self, val):
        ret_val = 1
        if val < 0:
            ret_val = 0
        return ret_val

    @staticmethod
    def hardlims(self, val):
        ret_val = 1
        if val < 0:
            ret_val = -1
        return ret_val

    @staticmethod
    def purelin(self, val):
        return val

    @staticmethod
    def poslin(self, val):
        if val < 0:
            ret_val = 0
        else:
            ret_val = val
        return ret_val

    @staticmethod
    def satlin(self, val):
        if val < 0 :
            ret_val = 0
        elif val > 1 :
            ret_val = 1
        else:
            ret_val = val
        return ret_val

    @staticmethod
    def satlins(self, val):
        if val < -1:
            ret_val = -1
        elif val > 1:
            ret_val = 1
        else:
            ret_val = val
        return ret_val

    @staticmethod
    def logsig(self, val):
        return 1 / (1 + math.exp(-val))

    @staticmethod
    def tansig(self, val):
        return (math.exp(val) - math.exp(-val)) / (math.exp(val) + math.exp(-val))