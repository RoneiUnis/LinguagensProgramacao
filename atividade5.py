import re

def inverter(palavra):
    if re.match(r'^\w+$', palavra):
        return palavra[::-1]
    return palavra

frase = input('Digite uma frase: ')

fraseinvertida = "Você digitou: "+ frase +" \n" + \
                "A inversão ficou: " + ''.join(inverter(palavra) for palavra in re.split(r'(\W+)', frase))
print(fraseinvertida)
