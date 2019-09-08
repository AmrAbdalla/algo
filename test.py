import math

#list = [1,2,3,4,5,6]
#sublist = []
#sublist.extend(list[0:3])
#sublist.extend(list[5:6])
#print(sublist)


def logsig(val):
    return 1 / (1 + math.exp(-val))


def sqr(val):
    return val * val


def calculate(func,val):
    return func(val)


var = 2

print(calculate(logsig,var))