numero=int(input("Enter a number:"))
if numero > 1:
    for i in range(2,int(numero**0.5)+1):
        if numero%i==0:
            print(f"{numero} is not a prime numeber!")
            break
    else:
        print(f"{numero} is a prime number!")
else:
    print(f"{numero} is not a prime number!")
