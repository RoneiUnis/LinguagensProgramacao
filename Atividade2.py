'''
Atividade 2 Forma triangulo ou não ?
'''

a = int(input("Digiteo lado a: ")) 
b = int(input("Digiteo lado b: ")) 
c = int(input("Digiteo lado c: ")) 

if a > b+c :
        print("Os lado a ",a," lado b ",b, " lado c ",c,"não formam um triangulo.")
       
else :
        print("Os lados formam um triangulo de area!",(a*(b+c)/2))
 
