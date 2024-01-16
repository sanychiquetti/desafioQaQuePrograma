import random
print('-------------------------------------------------------')
print('               Gerando Números Aleatórios              ')
print('-------------------------------------------------------')

def gerarNumerosAleatorios(numerosSorteados):
   while True:
      numero = random.randint(0,61)
      if numero not in numerosSorteados:
         return numero
      
def gerandoListaNaoRepetida():
   numerosSorteados = []
   while len(numerosSorteados) < 6:
      numeroAleatorio = gerarNumerosAleatorios(numerosSorteados)
      numerosSorteados.append(numeroAleatorio)
   numerosSorteados.sort()
   return numerosSorteados

numerosAlatorios = gerandoListaNaoRepetida()
print("Os números aleatórios sortedos foram: ", numerosAlatorios)