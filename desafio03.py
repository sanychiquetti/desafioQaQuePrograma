import re
import unicodedata
print('-------------------------------------------------------')
print('            Verificador de Palíndromos                 ')
print('-------------------------------------------------------')

def remover_acentos(texto):
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore')
    texto = texto.decode('utf-8')
    return texto

frase = input("Digite uma frase: ")

frase_sem_acentos = remover_acentos(frase)

frase_formatada = re.sub(r'[^A-Za-z]', '', frase_sem_acentos).lower()

if frase_formatada == frase_formatada[::-1]:
    print(f"'{frase}' acertou sua frase é um palíndromo.")
else:
    print(f"'{frase}' não foi desa vez não é um palíndromo.")