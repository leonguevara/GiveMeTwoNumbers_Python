#   givemetwonumbers.py
#   GiveMeTwoNumbers_Python
#
#   This program will ask the user for two whole numbers and two real numbers.  It will show
#   the addition, subtraction, multiplication, division and remainder of division of the two
#   whole numbers, as well as the division of both numbers treated as real numbers.
#
#   It will also show the addition, subtraction, multiplication and division of the two real
#   numbers.
#
#   Python interpreter: 3.6
#
#   Author: León Felipe Guevara Chávez
#   email:  leon.guevara@itesm.mx
#   date:   May 20, 2017
#

#   We ask for the two whole numbers
print("Give me two whole numbers:")
wholeNumber1 = int(input("Whole number 1:"))
wholeNumber2 = int(input("Whole number 2:"))

#   We ask for the two real numbers
print("\nGive me two real numbers:")
realNumber1 = float(input("Real number 1:"))
realNumber2 = float(input("Real number 2:"))

#   We display the results regarding the whole numbers
print("\n===Whole numbers:")
print(str(wholeNumber1) + " + " + str(wholeNumber2) + " = " + str(wholeNumber1 + wholeNumber2))
print(str(wholeNumber1) + " - " + str(wholeNumber2) + " = " + str(wholeNumber1 - wholeNumber2))
print(str(wholeNumber1) + " * " + str(wholeNumber2) + " = " + str(wholeNumber1 * wholeNumber2))
#   Python treats division as a floating point numbers operation, so we need to convert the result
#   to integer to show the integer division
print(str(wholeNumber1) + " / " + str(wholeNumber2) + " = " + str(int(wholeNumber1 / wholeNumber2))
      + " (cast as integer)")
print(str(wholeNumber1) + " mod " + str(wholeNumber2) + " = " + str(wholeNumber1 % wholeNumber2))
print(str(wholeNumber1) + " / " + str(wholeNumber2) + " = " + str(wholeNumber1 / wholeNumber2))

#   We display the results regarding the real numbers
print("\n===Real numbers:")
print(str(realNumber1) + " + " + str(realNumber2) + " = " + str(realNumber1 + realNumber2))
print(str(realNumber1) + " - " + str(realNumber2) + " = " + str(realNumber1 - realNumber2))
print(str(realNumber1) + " * " + str(realNumber2) + " = " + str(realNumber1 * realNumber2))
print(str(realNumber1) + " / " + str(realNumber2) + " = " + str(realNumber1 / realNumber2))
print(str(realNumber1) + " mod " + str(realNumber2) + " = " + str(realNumber1 % realNumber2))
