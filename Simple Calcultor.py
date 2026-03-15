print("________________________________________Welcome to our simple calculator____________________________________________________________________________")

def add(num1,num2):
    
    a= num1+num2
    return(a)

def sub(num1,num2):
    
    b= num1-num2
    return(b)

def multiply(num1,num2):
    c= num1*num2

    return(c)

def division(num1,num2):

    d= num1/num2

    return(d)

num1=  float(input("First Number: "))

symbol= input("Symbol: ")

num2= float(input("Secound Number: "))


for i in range (0,1):
    if symbol=="+":
        result= add(num1,num2)
        print(result)
    
    elif symbol=="-":
        result== sub(num1,num2)
        print(result)

    elif symbol=="*":
        result= multiply(num1,num2)
        print(result)

    elif symbol== "/":
        result= division(num1,num2)
        print(result)

    else:
        print("Invalid Input!!, Try again!!")    

print("_____________________________________________Code ended____________________________________________________________")   

