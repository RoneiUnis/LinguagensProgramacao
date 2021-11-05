'''
Atividade 3 o menor
'''

numero1 = int(input('Primeiro numero: '))
numero2 = int(input('Segundo numero : '))
numero3 = int(input('Terceiro numero: '))

menor = numero1

if (numero2 < menor):
     menor = numero2
if (numero3 < menor):
     menor = numero3

print('o menor é: ',menor)
