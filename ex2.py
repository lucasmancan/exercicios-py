lista = [[1,11],[2,22],[3,33],[4,44]]
inversa = []
 
for i in lista:
 i.reverse()
 inversa.append(list(i))
 
print(inversa)