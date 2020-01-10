casa = float(input('Qual o valor da casa ??'))
sal = float(input("Quanto você ganha ??"))
anos  = int(input('Em quantos anos você quer pagar a casa ??'))
prest = casa / (anos * 12)
nega = (sal * 30) / 100
if prest < nega:
    print('Emprestimo Aprovado')
else:
    print('Seu  foi emprestimo recusado')











