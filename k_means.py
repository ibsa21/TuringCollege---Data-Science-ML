from math import fsum, sqrt
from random import sample
from typing import Dict, Iterable, List, Tuple, Sequence
from pprint import pprint
from collections import defaultdict
from functools import partial

Point = Tuple[int, ...]
Centroid = Point

def mean(data:Iterable[float]) -> float:
    data = list(data)
    return fsum(data) / len(data)

def dist(p:Point, q:Point, fsum = fsum, sqrt = sqrt, zip = zip)->float:
    return sqrt(fsum([(x - y)**2 for x, y in  zip(p, q)]))

def assign_data(centroid: Sequence[Centroid], data:Iterable[Point])->Dict[Centroid, List[Point]]:
    """grouping the data point to the closes centroids"""
    d = defaultdict(list)

    for point in data:
        closest_centroid =  min(centroid, key=partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)

def compute_centroid(groups:Iterable[Sequence[Point]])->List[Centroid]:
    """compute the centroid of each groups"""
    return [tuple(map(mean, zip(*group))) for group in groups]

def k_means(data:Iterable[Point], k:int = 2, iterations:int = 50) ->List[Centroid]:
    data = list(data)
    centroids = sample(data, k)

    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroid(labeled.values())
    
    return centroids

if __name__ == '__main__':

    points = [
    
        (10, 41, 23), 
        (22, 30, 29), 
        (11, 42, 5), 
        (20, 32, 4), 
        (12, 40, 12), 
        (21, 36, 23)
    ]
    centroids = k_means(points, k = 2)
    d = assign_data(centroids, points)

    pprint(d)
