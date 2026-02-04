'''
print("1 - par ou impar")
print("2 - maior ou menor")
print("3 - calcule o dobro")
option = int(input("\nescolha uma opção: "))
match option:
    case 1:
        print("1 - par ou impar")
        num = int(input("digite um número "))
        if num%2==0:
            print("é par")
        else:
            print("é ímpar")
    case 2:
        print("2 - maior ou menor")
        num1 = int(input("escolha o primeiro numero: "))
        num2 = int(input("escolha o segundo numero: "))
        if num1>num2:
            print(f"{num1} é maior")
        elif num1<num2:
            print(f"{num2} é maior")
        else:
            print("os números são iguais")
    case 3:
        print("3 - calcule o dobro")
        numb = int(input("digite um número: "))
        print(numb *2)
    case _:
        print("opção inválida")
'''
'''
a estrutura looping é uma constução de repetição que pode ser escolhida por você ou pelo usuário. Existem dois tipos
FOR = valor inicial e valor final para ser testado
WHILE = enquanto o FOR trabalha com uma limitação de testes ou tentativas, vamos usar o WHILE enquanto a variável estiver valendo ou respostas lógicas 
'''
'''
for i in range (0, 101):
    if i %2==0:
        print (i)
'''
'''
for i in range (1, 112):
    if i %2!=0:
        print (i)
'''
'''
quant = int(input("escolha a quantidade de testes: ))
for i in range (1, quantidade +1):
    num = int(input("escolhe um número: "))
    if num %2==0:
        print(f"{num} é par")
    else:
        print(f"{num} é ímpar")
'''
'''
n= int(input("digite um número: "))
for i in range (1, 11):
    print(f"{n} x {i} = {n*i}")
'''
'''
quanto = int(input("escolha a quantidade de teste: "))
for i in range (1, quanto +1):
    print(f"{i} aluno")
    nome = input("nome: ")
    p1 = float(input("prova1: "))
    p2 = float(input("prova2 "))
    p3 = float(input("prova3: "))
    med = (p1 + p2 + p3) / 3
    if med >=7:
        resultado = "aprovado"
    elif med >=5:
        resultado = "recuperação"
    else:
        resultado = "reprovado"
print(f"\nnome: {nome}")
print(f"\nprova 1 {p1}")
print(f"\nprova 2 {p2}")
print(f"\nprova 3 {p3}")
print(f"\nmédia {med:.2F}")
print(f"resultado final: {resultado}")
'''

