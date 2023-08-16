num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

meth = str(input("what do you need:"))

if (meth == '+'):
    print(num1+num2)

elif (meth == '-'):
    print(num1-num2)

elif (meth == '*'):
    print(num1*num2)

elif (meth == '/'):
    print(num1/num2)

else:
    print("error")

