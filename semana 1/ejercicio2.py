print("Ingrese un número: ",end="\n")
num = int(input())
if int(num) < 100:
    print("\nEl número es menor a 100")
elif int(num) == 100:
    print("\n100...")
elif int(num) > 100:
    print("\nEl número es mayor a 100")