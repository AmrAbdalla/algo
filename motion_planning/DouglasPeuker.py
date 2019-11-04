import numpy as np
import numpy.linalg
import math
from GeometryLib import *
from Parameters import *

def CalcDisPtLine(line,point):
    return abs(((line.p2.y - line.p1.y) * point.x) - ((line.p2.x - line.p1.x) * point.y) + (line.p2.x * line.p1.y) - (line.p2.y * line.p1.x)) / math.sqrt((line.p2.y - line.p1.y)**2 + (line.p2.x - line.p1.x)**2)


def GetFarthestPoint(line,points):
    largest_dist = 0.0
    num_points = len(points)
    farthest_point_idx = 0
    for i in range(num_points):
        tmp_dist = CalcDisPtLine(line,points[i])
        if(tmp_dist > largest_dist):
            largest_dist = tmp_dist
            farthest_point_idx = i
    return {"index":farthest_point_idx , "distance":largest_dist}

def GetNextSample(points):
    sample_idx = 0
    num_points = len(points)
    if(num_points > 1):
        if(num_points > 2):
            line = Line(points[0] , points[num_points - 1])
            farthest_point = GetFarthestPoint(line,points)
            if(farthest_point["distance"] > MAX_DIST):
                tmp_points = points[0:farthest_point["index"]+1]
                sample_idx = GetNextSample(tmp_points)
            else:
                sample_idx = num_points - 1
        else:
            sample_idx = 1
    return sample_idx

def SampleDouglasPeuker(points):
    sample_idx = 0
    num_points = len(points)
    samples = [points[sample_idx]]
    while sample_idx < (num_points-1):
        sample_idx = sample_idx + GetNextSample(points[sample_idx:num_points])
        samples.append(points[sample_idx])
    return samples