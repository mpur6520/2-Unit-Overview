#Maru Puran
#September 26, 2023
#doing calculations using inputs, variables, as well as operators - outputs the results of calculations

name = input("Hello! What is your name?: ")
print("\nNice to meet you, " + name + "! We'll be doing some math today.\n")

#the arithmetic operators are:
# exponents ( ** ),         multiplacation ( * ),        integer division ( // )      assigment ( = )
# division ( / ),           remainder, mod ( % ),        addtion ( + ),        subtraction ( - )

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

#math done here and stored in variables w/ numbers
sum = num1 + num2 #addition
product = num1 * num2 #multiplacation
quotient = num1/num2 #division
exponent = num1 ** num2 #exponents
diff = num1 - num2 #subtraction
remainder = num1 % num2 #remainder
intQuotient = num1 // num2 #division, returns only integer

#print the results of math
print("\nThe sum of " + str(num1) + " and " + str(num2), "is", str(sum) + ".") #prints sum 
print("The product of", num1, "and", num2, "is", product) #prints product
print("The quotient of", num1, "divided by", num2, "is", str(quotient) + ".") #prints quotient
print("The result of", num1, "to the power of", num2, "is", str(exponent) + ".") #prints exponent
print("The difference of", num1, "subtracted by", num2, "is", str(diff) + ".") #prints difference
print("The remainder from", num1, "divided by", num2, "is", str(remainder) + ".") #prints remainder
print("The integer returned when you divide", num1, "by", num2, "is", str(intQuotient) + ".") #prints integer quotient