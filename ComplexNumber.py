#All operations between complex numbers can be put in this file.
class ComplexNumber:
    
    def add(self, number):
        return ComplexNumber(self.realValue + number.realValue, self.imaginaryValue + number.imaginaryValue)

    def getInverse(self):
        return ComplexNumber(-self.realValue, -self.imaginaryValue)

    def scalarMultiply(self, scalar):
        return ComplexNumber(self.realValue * scalar.realValue - self.imaginaryValue * scalar.imaginaryValue, self.realValue * scalar.imaginaryValue + scalar.realValue * self.imaginaryValue)

    def __init__(self, a, b):
        self.realValue = a
        self.imaginaryValue = b
    def __str__(self):
        return str(self.realValue) + " " + str(self.imaginaryValue) + "i"


#Takes in a string representing a complex number such a 1 + 2i
#Returns a parsed ComplexNumber class
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