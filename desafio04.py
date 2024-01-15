import re
print('-------------------------------------------------------')
print('                  Contador de Palavras                 ')
print('-------------------------------------------------------')

fraseInformada = input('Digite sua frase: ')

result = len(re.findall(r"\w+", fraseInformada))

print("Em sua frase temos " + str(result) + " palavras.")