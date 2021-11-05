'''
Atividade 4 numero primo
'''



def primo(numero):
 	for i in range(2,numero):
 		if not numero%i:
 			return False
 		else:
 			print(str(numero) + ' é numero primo')
 			return True
 			
for numero in range(0,101):
 	primo(numero)
