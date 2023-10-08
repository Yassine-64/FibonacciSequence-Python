
n = int(input("Veuillez entrer un entier n supérieur à 2 : "))
U0 = 0
U1 = 1


print("La suite de Fibonacci jusqu'à", n, ":")
print(U0)
print(U1)


while U0 + U1 <= n:
    Un = U0 + U1
    print(Un)
    U0 = U1
    U1 = Un
