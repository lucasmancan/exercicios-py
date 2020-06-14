def primo(numero):
 qt_divisores = 0
 for i in range(1, numero + 1):
  if numero % i == 0:
    qt_divisores +=1
  if qt_divisores == 2:
   return 1
 return 0
 
numero = int(input("Digite um número: "))
print(primo(numero))