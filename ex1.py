import re
 
pattern = re.compile('^([a-eA-e]{10})$')
 
def invalido(resposta):
 return not bool(pattern.match(resposta))
 
def ler_gabarito():
 gabarito = input("Digite um gabarito: ")
 while invalido(gabarito):
   gabarito = input("Digite um gabarito válido (a-eA-E): ")
 
 return gabarito
 
def calcular_nota(resposta, gabarito):
 nota = 0
 for i in range(10):
   if gabarito[i].lower() == resposta[i].lower():
     nota = nota + 1
  
 return nota

def exibir_nota(nota):
  print("A nota da prova é: " + str(nota))

def ler_respostas():
  gabarito = ler_gabarito()
 
  for i in range(5):
    resposta = input("Digite as respostas da prova "+str(i+1)+": ")

    try:
 
      if not bool(pattern.match(resposta)):
        raise Exception
 
      nota = calcular_nota(resposta, gabarito)
      exibir_nota(nota)
    except Exception:
      print("Ocorreu algum erro ao avaliar a prova verifique a quantidade de questoes e o formato: " + resposta)
 
# EXECUTA O PROGRAMA
ler_respostas()