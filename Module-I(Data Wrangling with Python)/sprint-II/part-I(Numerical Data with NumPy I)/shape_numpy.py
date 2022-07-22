import numpy

def change_shape(row:int, col:int):
    nums = numpy.array(list(map(int, input().split())))
    nums.shape = (row, col)
    return nums

if __name__ == "__main__":
    #change shape
    print(change_shape(3,3))
