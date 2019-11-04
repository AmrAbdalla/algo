from GeometryLib import *
import numpy as np
from matplotlib import pyplot as plt
from DijkstraSearch import *
from Parameters import *

class Layer:
    def __init__(self,vehicle,object,ref_point=Point(),orientation=0.0,lat_sampling_shift=0.0,lat_min_shift=0.0,lat_max_shift=0.0,layer_index = 0):
        self.ref_point = ref_point
        self.orientation = orientation
        self.lat_sampling_shift = lat_sampling_shift
        self.lat_min_shift = lat_min_shift
        self.lat_max_shift = lat_max_shift
        c_obj = 0.0
        if IntersectCircletoCircle(Circle(ref_point, vehicle.r), object):
            c_obj = float('inf')
        self.ref_vertex = (self.ref_point,0.0,c_obj,layer_index)
        self.lat_vertices = []
        self.layer_index = layer_index
        self.lat_vertices = self.SampleLaterally(vehicle,object)


    def GetRefVertex(self):
        return self.ref_vertex

    def SampleLaterally(self,vehicle,object):
        current_shift = 0.0
        tmp_samples = []
        frame = Frame(self.ref_point,self.orientation)

        if self.lat_min_shift < 0.0 and self.lat_sampling_shift > 0.0:
            while current_shift >= (self.lat_min_shift + self.lat_sampling_shift):
                current_shift = current_shift - self.lat_sampling_shift
                tmp_point = transformPoint(frame,Point(0.0,current_shift))
                c_obj = 0.0
                if IntersectCircletoCircle(Circle(tmp_point,vehicle.r),object):
                    c_obj = float('inf')
                tmp_samples.insert(0,(tmp_point,current_shift,c_obj,self.layer_index))

        tmp_samples.append(self.ref_vertex)

        if self.lat_max_shift > 0.0 and self.lat_sampling_shift > 0.0:
            while current_shift <= (self.lat_max_shift - self.lat_sampling_shift):
                current_shift = current_shift + self.lat_sampling_shift
                tmp_point = transformPoint(frame,Point(0,current_shift))
                c_obj = 0.0
                if IntersectCircletoCircle(Circle(tmp_point, vehicle.r), object):
                    c_obj = float('inf')
                tmp_samples.append((tmp_point,current_shift,c_obj,self.layer_index))
        return tmp_samples

    def GetLayerVertices(self):
        return self.lat_vertices

    def GetLayerVerticesPts(self):
        tmp_points = []
        for vertex in self.lat_vertices:
            tmp_points.append(vertex[0])
        return tmp_points


def GetLayers(points,vehicle,object):
    num_points = len(points)
    layers = []
    for i in range(num_points - 1):
        angle = atan2((points[i].y - points[i+1].y),(points[i].x - points[i+1].x))
        layers.append(Layer(vehicle,object,points[i],angle,LATERAL_SHIFT,LATERAL_SHIFT_MIN,LATERAL_SHIFT_MAX,i))
    return layers


def GetLatManeuverPath(layers,start_vertex,end_vertex):
    path_points = []
    vertices_path =  FindOptimalPath(layers, start_vertex, end_vertex)

    for vertex in vertices_path:
        path_points.append(vertex[0])

    return path_points
