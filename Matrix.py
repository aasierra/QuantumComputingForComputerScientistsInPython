from Vector import Vector
class Matrix:
    def __init__(self, vectors):
        self.vectors = vectors

    def add(self, matrix):
        newVectors = []
        for i in range(0, len(matrix.vectors)) :
            newVectors.append(self.vectors[i].add(matrix.vectors[i]))
        return Matrix(newVectors)

    def scalarMultiply(self, matrix):
        newVectors = []
        for i in range(0, len(matrix.vectors)) :
            newVectors.append(self.vectors[i].scalarMultiply(matrix.vectors[i]))
        return Matrix(newVectors)

    def getInverse():
        newVectors = []
        for i in range(0, len(matrix.vectors)) :
            newVectors.append(self.vectors[i].getInverse(matrix.vectors[i]))
        return Matrix(newVectors)