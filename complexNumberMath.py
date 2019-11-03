complexNumber1 = input("Please input the first complex number : ")
complexNumber2 = input("Please input the second complex number : ")
firstComponents = complexNumber1.split(" ")
secondComponents = complexNumber2.split(" ")
isB1Negative = firstComponents[1].strip() == '-'
isB2Negative = secondComponents[1].strip() == "-"
a1 = float(firstComponents[0])
if (firstComponents[2] == "i") :
	firstComponents[2] = "1"
b1 = float(firstComponents[2].replace("i", ""))
if (isB1Negative) :
	b1 = b1 * -1

a2 = float(secondComponents[0])
if (secondComponents[2] == "i") :
	secondComponents[2] = "1"
b2 = float(secondComponents[2].replace("i", ""))
if (isB2Negative) :
	b2 = b2 * -1

print("Addition : " + str(a1 + a2) + " " + str(b1 + b2) + "i")
print("Multiplication : " + str(a1 * a2 - b1 * b2) + " " + str(a1 * b2 + a2 * b1) + "i")
print("Subtraction : " + str(a1 - a2) + " " + str(b1 - b2) + "i")
#Division below
numerator1 = a1 * a2 + b1 * b2
numerator2 = a2 * b1 - a1 * b2
denominator = a2 * a2 + b2 * b2
print("Division : " + str(numerator1) + " / " + str(denominator) + " " + str(numerator2) + " / " + str(denominator))
print("Division : " + str(numerator1 / denominator) + " " + str(numerator2 / denominator) + "i")