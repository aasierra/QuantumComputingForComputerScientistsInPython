from ComplexNumber import ComplexNumber
from ComplexNumber import parseComplexNumber
from Vector import Vector

vector1 = raw_input("Please input the first vector as a comma separated list of complex numbers of the format a + bi: ")
splitVector1 = vector1.split(',')
vector1Array = []
for numberString in splitVector1 :
    vector1Array.append(parseComplexNumber(numberString))
print("Inverse below : ")
for number in vector1Array :
    print(number.getInverse())
print("Scalar of 2 + i : ")
for number in vector1Array:
    print(number.scalarMultiply(ComplexNumber(2, 1)))
vector2 = raw_input("Please input the second vector as a comma separated list of complex numbers of the format a + bi: ")
splitVector2 = vector2.split(',')

vector2Array = []
for numberString in splitVector2 :
    vector2Array.append(parseComplexNumber(numberString))
resultVector = Vector(vector1Array).add(Vector(vector2Array))
for result in resultVector.components:
    print("|" + str(result) + "|")




