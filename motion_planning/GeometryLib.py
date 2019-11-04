from math import *
import numpy as np
from matplotlib import pyplot as plt

def transformPoint(frame_of_reference, point):
    angle_cos = cos(frame_of_reference.angle)
    angle_sin = sin(frame_of_reference.angle)
    transformed_point = Point()
    transformed_point.x = (point.x * angle_cos) - (point.y * angle_sin) + frame_of_reference.ref_point.x
    transformed_point.y = (point.x * angle_sin) + (point.y * angle_cos) + frame_of_reference.ref_point.y
    return transformed_point


def convRadToDeg(angle_rad):
    angle_deg = angle_rad * 180.0 / math.pi
    return angle_deg

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1 = Point(), p2 = Point()):
        self.p1 = p1
        self.p2 = p2

class Frame():
    def __init__(self, ref_point=Point(), angle=0.0):
        self.ref_point = ref_point
        self.angle = angle

def PlotGl2dPoints(points,color_shap):
    list_x = []
    list_y = []
    for point in points:
        list_x.append(point.x)
        list_y.append(point.y)

    plt.plot(list_x, list_y, color_shap)

class Circle():
    def __init__(self, center=Point(),r=1.0):
        self.center = center
        self.r = r
        self.x_list = []
        self.y_list = []
        t = np.linspace(0, 2*pi, 360)
        for v in t:
            self.x_list.append((self.r * cos(v)) + self.center.x)
            self.y_list.append((self.r * sin(v)) + self.center.y)

def IntersectCircletoCircle(c1=Circle(),c2=Circle()):
    ret_val = False
    diff_x = c1.center.x - c2.center.x
    diff_y = c1.center.y - c2.center.y
    dist = sqrt(diff_x**2 + diff_y**2)
    if dist <= (c1.r + c2.r):
        ret_val = True
    return ret_val