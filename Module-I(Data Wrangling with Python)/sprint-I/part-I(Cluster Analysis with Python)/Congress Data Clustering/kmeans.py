from sklearn import datasets
from math import fsum, sqrt
from random import sample
from typing import Iterable, Tuple, Sequence
from pprint import pprint
from functools import partial

Data = Tuple[float, ...]
Centroid = Data

def load_data():
    """load iris data and return 2D with rXc dimension
    r - examples of each dataset, 
    c-feature(sepal, and petal length, sepal, and petal width)
    """
    return [(a,b,c,d) for a,b,c,d in datasets.load_iris().data]

def mean(data:Iterable[float]) -> float:
    """calculating mean of data"""
    data = list(data)
    return fsum(data) / len(data)

def dist(p:Data, q:Data, fsum = fsum, sqrt = sqrt, zip = zip)->float:
    """calculating ecleaudian distance between two dataset Datas"""
    return sqrt(fsum([(x - y)**2 for x, y in  zip(p, q)]))

def assign_labels(data:Iterable[Data], Centroid:Sequence[Centroid]):
    """grouping the data Data to the closes centroids"""
    labels =[]
    for Data in data:
        label = min(Centroid, key=partial(dist, Data))
        labels.append(label)
    return labels

def compute_centroid(groups:Iterable[Sequence[Data]]): 
    """compute the centroid of each groups"""
    return [tuple(map(mean, zip(group))) for group in groups]

def k_means(data:Iterable[Data], k:int=3, iterations:int=50):
    """perform k-means clustering on the given data set"""

    data = list(data)
    centroids = sample(data, k)
    while i < iterations or prev_centroids != centroid:
        labeled = assign_labels(data, centroids)
        prev_centroid = centroids
        centroids = compute_centroid(labeled)
    return centroids
