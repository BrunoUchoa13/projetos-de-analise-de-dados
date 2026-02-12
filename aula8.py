'''
def dividir (a, b):
    return a / b
a = int(input('digite um número: '))
b = int(input('digite outro número: '))  
resultado = dividir (a, b)

print(f"{a} dividido por {b} = {resultado}")
#ao usar denominador 0, o programa quebra, para evitar isso usamos o try e except
'''
'''
def dividir (a, b):
    try:
        resultado = float(a) / float(b)
    except ZeroDivisionError:
        print ("Erro: divisão por zero não é permitida.")
    except ValueError:
        print ("Erro: valor inválido informado.")
    else:
        print (f"resultado da divisão: {resultado}")
    finally:
        print ("Operação finalizada.")

n1 = input("digite um número: ")
n2 = input("digite outro número: ")
dividir (n1, n2)
'''
'''
#ex1
def numero():
    try:
        número = int(input("digite um número inteiro: "))
    except ValueError:
        print("erro: digite um número inteiro")
    else:
        print(f"o número escolhido é: {número}")
    finally:
        print("teste finalizado")
numero()
'''
'''
#ex2

def notas ():
    try:
        n1 = float(input("digite nota 1: ").replace ("," , "."))
        n2 = float(input("digite nota 2:"). replace ("," , "."))
        média = (n1 + n2) / 2
    except ValueError:
        print("Erro: digite um número entre 0.0 e 10.0")
    else:
        print (f"média: {média:.2f}")
    finally:
        print("teste finalizado")

notas ()
'''
'''
#ex3
def operações ():
    try:
        n1 = float(input("digite número 1: ").replace ("," , "."))  
        n2 = float(input("digite número 2: ").replace ("," , "."))
        
        print("1- soma") 
        print("2- subtração")
        print("3- multiplicação")
        print("4- divisão")
        option = int(input("escolha a operação: "))
        match option:
            case 1:
                resultado = n1 + n2
                print(f"{n1} + {n2} = {resultado}")
            case 2:
                resultado = n1 - n2
                print(f"{n1} - {n2} = {resultado}")
            case 3:
                resultado = n1 * n2
                print(f"{n1} * {n2} = {resultado}")
            case 4:
                resultado = n1 / n2
                print(f"{n1} / {n2} = {resultado}")
            case _:
                print("operação inválida")
    except ValueError:
        print("Erro: digite um número válido.")
    finally:
        print("Operação finalizada.")

operações()
'''
'''
#ex4
def cadastro ():
    try:
        nome = input("digite seu nome: ")
        idade = int(input("digite sua idade: "))
        if idade < 0:
            raise ValueError("idade precisa ser um número inteiro e positivo")
    except ValueError:
        print("Erro: em idade digite um número inteiro.")
    else:
        print(f"nome: {nome}")
        print(f"idade: {idade}")
    finally:
        print("teste finalizado")
cadastro ()
'''
'''
#ex5
def calcularimc():
    try:
        peso = float(input("me diz seu peso "))
        if peso <= 0:
            raise ValueError("digite seu peso correto, que é um número positivo")
        altura = float(input("me diz sua altura "))
        if altura <= 0:
            raise ValueError("digite sua altura correta, que é um número positivo")
    imc = peso / altura * altura
    except ValueError:
        print("Erro: digite peso ou altura válidos")
    else:
        if imc < 18.5:
        print(f"")
        elif imc < 25 =
        elif imc < 30 =
        else:

imc < 18.5 = Abaixo do peso
imc < 25= Peso normal
imc < 30 = Sobrepeso
Imc >=30 = Obesidade
#completar
'''
'''
#ex3
#uma lista é capaz de armazenar cada informação na sua tipagem(string, int, float...). Dicionário é justamente o nome que se dá para estas listas.
#a lista pode ser criada inserir os dados da lista dentro de chaves.
def buscarAlunos():
    alunos = {"Ana": 8.5, "Bruno": 7.0, "Carlos": 9.2}
    try:
        nome = input("Escreva o nome: "). capitalize()
        nota = alunos [nome]
    except KeyError:
        print("Erro: não encontrado")
    else:
        print(f"nota {nome}: {nota}")
    finally:
        print("busca concluída")
buscarAlunos()
'''
def buscaProdutos():
    produtos = {"arcondicionado": 2399.90, "geladeira": 3399.90, "tv": 5599.90, "microondas": 869.90}
    try:
        nome = input("digite o nome do produto: ").capitalize()
        preço = nome [nome]
        quantidade = int(input("digite a quantidade desejada: "))

    except KeyError:
        print("Erro: produto não encontrado")
    else:
        print(f"Produto {nome}: R$ {nome * quanidade}")
buscaProdutos()
















