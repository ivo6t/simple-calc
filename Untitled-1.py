num1 = input("chouse frist number ")
choise = input("what do you want do +,-,*,/,**,%: ")
num2 = input("chouse second number ")

if choise == "+":
    print(int(num1) + int(num2))
elif choise == "-":
    print(int(num1) - int(num2))
elif choise == "*":
    print(int(num1) * int(num2))
elif choise == "/":
    print(int(num1) / int(num2))
elif choise == "**":
    print(int(num1) ** int(num2))
elif choise == "%":
    print (int(num1) % int(num2))
else:
    print("error you have choused wrong sign")