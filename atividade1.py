'''

Exercicio 1 , idade em anos meses e dias

'''
import math

dias = int(input("Digite a idade em dias: ")) # Dias em idade

anos = math.ceil(dias/365)
meses = math.ceil(dias/30.417)

print("Idade em anos ",anos)
print("Idade em meses ",meses)
print("Idade em dias ",dias)
