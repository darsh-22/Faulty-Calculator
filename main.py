# faulty calculator
# 45 * 3 = 555 ,56+9 = 77 ,56/6 = 4
print("Enter First value: ")
v1 = int(input()) # First integer value will be stored in v1 variable
print("Enter Second value: ")
v2 = int(input()) # Second integer value will e storein v2 variable
print("1. Addition\n2.Minus\n3.Multiplication\n4.Division")
c = int(input()) # User choices for calculations
if c == 1: 
    if (v1 == 56 and v2 == 9) or (v1 == 9 and v2 == 56): # if any of variables has 56 or 9 as an input it will return wrong output
        print("Addition is : 77")
    else:
        print("Addition is: " + str(v1 + v2))
elif c == 2:
    print("Minus is: " + str(v1 - v2))
elif c == 3:
    if (v1 == 45 and v2 == 3)or(v1 == 3 and v2 == 45): # if any of variables has 45 and 3 as an input it will return wrong output
        print("Multiplication is: 555")
    else:
        print("Multiplication is: " + str(v1 * v2))
else:
    if(v1 == 56 and v2 == 6)or(v1 == 6 and v2 == 56): # if any of variables has 56 and 6 as an input it will return wrong output
        print("Division is: 4")
    else:
        print("Division is: " + str(v1 / v2))
