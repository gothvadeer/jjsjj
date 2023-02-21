#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
# carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
pessoa = {}
data = date.today().year
while True:
    pessoa["Nome"] = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Ano de nascimento: '))
    pessoa["Idade"] = data - idade
    pessoa["CTPS"] = int(input('Carteira de trabalho: '))
    if pessoa["CTPS"] == 0:
        break
    pessoa["Contratação"] = int(input('Ano de contratação: '))
    pessoa["Aposentadoria"] = (pessoa["Contratação"] + 35) - idade
    pessoa["Salário"] = float(input('Salário: '))
    break
print('=*'*20)
for k, v in pessoa.items():
    print(f'{k} é {v}')