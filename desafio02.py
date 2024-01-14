print('-------------------------------------------------------')
print('                   Calculadora Básica                  ')
print('-------------------------------------------------------')

try:
   primeiroNumero = float(input("Escolha o primeiro número: "))
   segundoNumero = float(input("Agora informe o segundo número: "))

   escolhendOoperacao = input("Qual a operação você deseja? (+, -, *, /): ")

   if escolhendOoperacao == "+":
      resultado = primeiroNumero + segundoNumero
   elif escolhendOoperacao == "-":
      resultado = primeiroNumero - segundoNumero
   elif escolhendOoperacao == "*":
      resultado = primeiroNumero * segundoNumero
   elif escolhendOoperacao == "/":
      if segundoNumero == 0:
         print("Erro: Divisão por zero não é permitida.")
         resultado = None
      else:
          resultado = primeiroNumero / segundoNumero
   else:
      print("Operação inválida.")
      resultado = None

   if resultado is not None:
          print("Resultado: {:.2f}".format(resultado))
          
except ValueError:
    print("Erro: Certifique-se de inserir números válidos.")