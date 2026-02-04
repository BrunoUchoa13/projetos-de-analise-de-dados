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
aci = desc11+desc6
ger = desc9+desc6
vend = desc8+desc5
"salario liquido"
acionista = sal - aci + bonus1
gerente= sal - ger + bonus2
vendedor= sal - vend + bonus2
if sal>=3000:
    print(f"seu cargo é acionista: {acionista}")
elif sal>=2000:
    print(f"seu cargo é gerente: {gerente}")
elif sal<2000:
    print(f"seu cargo é vendedor: {vendedor}")