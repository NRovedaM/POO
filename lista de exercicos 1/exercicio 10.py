age = int(input("informe sua idade: "))

if age <= 12:
    print("criança")
elif age > 12 and age <= 17:
    print("adolecente")
elif age >= 18  and age < 58:
    print("adulto")
elif age >= 58:
    print("idoso")
else:
    print("comando invalido")