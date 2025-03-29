print("insira três numeros imteiro:")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 and num2 == num3: #uma verificação a mais só pra prevenir graças
    print("os numeros são iguais!!!")
elif num1 > num2 and num1 > num3:
    print(f"o maior numero é {num1}")
elif num2 > num3:
    print(f"o maior numero é {num2}")
else:
    print(f"o maior numero é {num3}")