class ComplexNumber:

    def getInverse(self):
        return ComplexNumber(-self.realValue, -self.imaginaryValue)

    def getScalared(self, scalar):
        return ComplexNumber(self.realValue * scalar.realValue - self.imaginaryValue * scalar.imaginaryValue, self.realValue * scalar.imaginaryValue + scalar.realValue * self.imaginaryValue)

    def __init__(self, a, b):
        self.realValue = a
        self.imaginaryValue = b
    def __str__(self):
        return str(self.realValue) + " " + str(self.imaginaryValue) + "i"


def complexNumberAdd(complexNumber1, complexNumber2):
    return ComplexNumber(complexNumber1.realValue + complexNumber2.realValue, complexNumber1.imaginaryValue + complexNumber2.imaginaryValue)

def vectorAdd(vector1, vector2):
    returnVector = []
    "This will take in a vector and add it to the second vector"
    for i in range(0, len(vector1)):
        returnVector.append(complexNumberAdd(vector1[i], vector2[i]))

    return returnVector


def parseComplexNumber(numberString):
    components = numberString.strip().split(" ")
    isNegative = components[1].strip() == '-'
    a = float(components[0])
    if (components[2].strip() == "i") :
	    components[2] = "1"
    b = float(components[2].strip().replace("i", ""))
    if (isNegative) :
	    b = b * -1

    return ComplexNumber(a, b)

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
    print(number.getScalared(ComplexNumber(2, 1)))
vector2 = raw_input("Please input the second vector as a comma separated list of complex numbers of the format a + bi: ")
splitVector2 = vector2.split(',')

vector2Array = []
for numberString in splitVector2 :
    vector2Array.append(parseComplexNumber(numberString))
resultVector = vectorAdd(vector1Array, vector2Array)
for result in resultVector:
    print("|" + str(result) + "|")




