print("+---------------------------------------------+")
print("|              mini calculator                |")
print("+---------------------------------------------+")
print("+---------------------------------------------+")
num1= float(input("enter the first number : "))
print("+---------------------------------------------+")
num2= float(input("Enter the second nuumber : "))
print("+---------------------------------------------+")
def  add(num1,num2):
    print("you added answer is : ",num1+num2)
    
def  sub(num1,num2):
    print("you added answer is : ",num1-num2)

def  mul(num1,num2):
    print("you added answer is : ",num1*num2)
    
def  dev(num1,num2):
    print("you added answer is : ",num1/num2)
    
def  pow(num1,num2):
    print("you added answer is : ",num1^num2)
    
print("+---------------------------------------------+")
print("|  addition           :         A             |")
print("+---------------------------------------------+")
print("|  Substraction       :         B             |")
print("+---------------------------------------------+")
print("|  Multipication      :         C             |")
print("+---------------------------------------------+")
print("|  devition           :         D             |")
print("+---------------------------------------------+")
print("|  power              :         E             |")
print("+---------------------------------------------+")
op= str(input("Choose your operation :"))
print("+---------------------------------------------+")

print(f"your answer is : ")

match op:
    case 'A':
        add(num1,num2)
    case 'B':
        sub(num1,num2)
    case 'C':
        mul(num1,num2)
    case 'D':
        dev(num1,num2)
    case 'E':
        pow(num1,num2)
    case _:
        print("Enter the valid input next time:")
    


