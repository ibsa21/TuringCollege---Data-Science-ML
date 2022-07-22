import numpy

def get_determinant():
    return round(numpy.linalg.det(matrix), 2)

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(float, input().split())))
    
    print(get_determinant())
