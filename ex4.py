def ler_numero_positivo():
 while True:
   try:
     numero = int(input('Informe um número positivo: '))
     if numero > 0:
       return numero
   except ValueError:
     continue
 
def somar(n):
 return sum(i/(2*i-1) for i in range(2, n+1))
 
numero = ler_numero_positivo()
print(somar(numero))