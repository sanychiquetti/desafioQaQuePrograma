nomeUsuario = input('Olá, qual seu nome? ')
numeroInformado = int(input(nomeUsuario + " me diga um número: "))

if numeroInformado % 2 == 0:
    print("O número", numeroInformado, "que você digitou é par.")
else:
    print("O número", numeroInformado, "que você digitou é ímpar.")
