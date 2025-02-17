def rfact(n):
    if n==1:
        return n
    else:
        return n*rfact(n-1)
    
numero=int(input("Enter your desired number:"))

if numero<=0:
    print("NO FACTORIAL!!!")
elif numero==0:
    print("Factorial of 0 is 1!")
else:
    print("The factorial is", rfact(numero))