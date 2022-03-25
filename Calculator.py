def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

if __name__ =="__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add(num1,num2)
    result1 = sub(num1,num2)
    result3 = multi(num1,num2)
    result4 = div(num1,num2)
    print(result)
    print(result1)
    print(result3)
    print(result4)


