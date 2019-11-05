class Vector:
    def __init__(self, components):
        self.components = components
    
    def add(self, vector):
        newVector = []
        for i in range(0, len(self.components)):
            newVector.append(self.components[i].add(vector.components[i]))
        return Vector(newVector)

    def scalarMultiply(self, scalar):
        newVector = []
        for i in range(0, len(self.components)):
            newVector.append(self.components[i].scalarMultiply(vector.components[i]))
        return Vector(newVector)

    def getInverse():
        newVector = []
        for i in range(0, len(self.components)):
            newVector.append(self.components[i].getInverse())
        return Vector(newVector)