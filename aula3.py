'''
match / case
Na aula passada nós mesmos indicamos a direção dentro do algoritmo. Agora é o próprio usário que decide como trabalhar dentro do algoritmo.
Em outras aplicações existem os switch cases, no Python trabalhamos com match case, ou seja, blocos ou caixinhas onde podemos trabalhar diversos comandos.
Case é um bloco de comandos que vai dar um resultado ao final para o usuário
'''
'''
#exemplo:
dia = int(input("dia: "))
match dia:
    case 1:
        print("domingo")
    case 2:
        print("segunda-feira")
    case 3:
        print("terça-feira")
    case 4:
        print("quarta-feira")
    case 5:
        print("quinta-feira")
    case 6:
        print("sexta-feira")
    case 7:
        print("sábado")
    case _:
        print("opção inválida")
'''
'''
mês = int(input("mes: "))
match mês:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("março")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
'''
'''
nota = (input("nota: "))
match: nota
    case "A":
        print("Excelente")
    case "B":
        print("Bom")
    case "C":
        print("Regular")
    case "D":
        print("Ruim")
    case "F":
        print("Reprovado")
    case"_":
        print("digite uma nota válida")
'''
idade = int(input("idade: "))
print("natacao")
print("corrida")
print("ciclismo")
esporte = input("esporte: ")
match esporte:
    case "natacao":
        print("natacao")
        if idade<10:
            print("mirim")
        elif idade<=14:
            print("infantil")
        else:
            print("juvenil")
    case "corrida":
        print("corrida")
        if idade<16:
            print("junior")
        else:
            print("infantil")
    case "ciclismo":
         print("ciclismo")
         if idade<=18:
            print("profissional")
         else:
            print("amador") 

















