'''
print("1 - par ou impar")
print("2 - maior ou menor")
print("3 - calcule o dobro")
continua = 's'
while continua == 's':

    option = int(input("escolha uma opção: "))
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
    continua = input("deseja continua? (s/n): ").lower().strip() #lower transforma tudo em caixa baixa e strip apaga todos os espaços
    if continua != 's':
        print("teste encerrado")
        break #interrompe a linha do comando case
'''
'''
nome = input("nome: ")
while True:
    p1 = float(input("prova1 (0.0 a 10.0): ").replace (",","."))
    if p1 >=0.0 and p1 <=10:
        break 
    else:
        print("nota inválida: digite um valor entre 0.0 e 10.0")
while True:
    p2 = float(input("prova2 (0.0 a 10.0): ").replace (",","."))
    if p2 >=0.0 and p2 <=10:
        break
    else:
        print("nota inválida: digite um valor entre 0.0 e 10.0")
med = (p1 + p2) / 2
if med >=6:
    resultado = "aprovado"
else:
    resultado = "reprovado"

print(f"\nnome: {nome}")
print(f"\nprova 1 {p1}")
print(f"\nprova 2 {p2}")
print(f"\nmédia {med:.2F}")
print(f"resultado final: {resultado}")
'''
'''
Aula 5
Esqueci de salvar a versão anterior e a versão nova do meu projeto. O que fazer?
Quero compartilhar meu projeto com minha equipe. Como fazer?
tudo o que faz, tudo o que vc escreve você deve subir no github para servir com portfolio.
GIT: é um sistema de controle opensouce que permite com que compartilhemos nossas aplicações, permitindo que outras pessoas trabalhem ao mesmo tempo
GITHUB: platatorma em nuvem que usa o GIT para guardar projetos, possibilitando que outras pessoas colaborem, compartilhem e acompanhem alterações
'''
