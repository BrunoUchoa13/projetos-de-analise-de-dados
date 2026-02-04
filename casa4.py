'''
sal = float(input("qual seu salário: R$ "))
"Desconto de INSS"
desc11 =sal*0.11
desc9 =sal*0.09
desc8 =sal*0.08
"Desconto de VR"
desc6 =sal*0.06
desc5 =sal*0.05
"bônus"
bonus1 = 300
bonus2 = 200
"Descontos totais"
acionista = desc11+desc6
gerente = desc9+desc6
vendedor = desc8+desc5
"salario liquido"
aci = sal - acionista + bonus1
ger= sal - gerente + bonus2
vend= sal - vendedor + bonus2
if sal>=3000:
    print(f"cargo: acionista | salário: {aci}")
elif sal>=2000:
    print(f"cargo: gerente | salário: {ger}")
elif sal<2000:
    print(f"cargo: vendedor | salário: {vend}")
'''
#CORREÇÃO
nome = input("nome: ")
sal = float(input("qual seu salário: R$ "))
#inss
if sal>=3000:
    inss= sal*0.11
elif sal>=2000:
    inss=sal*0.09
elif sal<2000:
    inss=sal*0.08
#vale
if sal>=2000:
    vale= sal*0.06
else:
    vale=sal*0.05
#bonus
if sal>3000:
    bonus=300
else:
    bonus=200
salarioliquido = sal - (inss + vale) + bonus
print(f"nome: {nome}")
print(f"salário bruto: {sal: .2F}")
print(f"INSS: {inss: .2F}")
print(f"vale transporte: {vale: .2F}")
print(f"bônus: {bonus: .2F}")
print(f"salário líquido: {salarioliquido:.2F}")




