import numpy as np
from DouglasPeuker import *
from matplotlib import pyplot as plt
from matplotlib import animation
from GeometryLib import *
from LatManeuverPlanner import *
from Parameters import *


#def init():
#    line.set_data([], [])
#    return line,
#
#def animate(i):
#    line.set_data(x[0:i], y[0:i])
#    return line,

def f_x(x):
    return -0.00005*x**3+0.005*x**2+0.02*x

def CreateTrajectory(x_list , y_list, vehicle, object):
    num_points = len(x_list)
    input_points = []
    for i in range (num_points):
        point = Point(x_list[i],y_list[i])
        input_points.append(point)

    fig1 = plt.figure(1)
    fig1.suptitle("free reference path")
    PlotGl2dPoints(input_points, 'b')
    plt.plot(object.x_list, object.y_list, 'k')
    plt.ylim(-10, 10)
    plt.xlim(0, 80)

    sampled_path = SampleDouglasPeuker(input_points)
    fig2 = plt.figure(2)
    fig2.suptitle("sampled path")
    PlotGl2dPoints(sampled_path,'r--h')
    layers = GetLayers(sampled_path[1:],vehicle,object)
    for layer in layers:
        PlotGl2dPoints(layer.GetLayerVerticesPts(), 'm--o')
    plt.plot(object.x_list, object.y_list, 'k')
    plt.ylim(-10, 10)
    plt.xlim(0, 80)

    start_vertex = (sampled_path[0], 0.0, 0, 0)
    end_vertex = (sampled_path[len(sampled_path) - 1], 0.0, 0, 0)
    opt_path = GetLatManeuverPath(layers,start_vertex,end_vertex)
    fig3 = plt.figure(3)
    fig3.suptitle("optimal path")
    PlotGl2dPoints(opt_path, 'g--^')
    plt.plot(object.x_list, object.y_list, 'k')
    plt.ylim(-10, 10)
    plt.xlim(0, 80)


x = np.linspace(0, 80, 10)
y = f_x(x)
#fig = plt.figure(1)
#plt.plot(x,y)
#plt.ylim(-10,10)
#plt.xlim(0,80)
global object
global vehicle
object = Circle(Point(62,9),0.5)
vehicle = Circle(Point(0,0),0.5)
CreateTrajectory(x,y,vehicle,object)

#ax = plt.axes(xlim=(0,80), ylim=(-10,10))
#line, = ax.plot([], [], lw=2)

#anim = animation.FuncAnimation(fig, animate, init_func=init,
 #                              frames=11, interval=200, blit=True)
plt.ylim(-10,10)
plt.xlim(0,80)
plt.show()