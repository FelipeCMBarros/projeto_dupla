import random
def rolar_dados(dados):
  lista_dados = []
  i = 0
  while i < dados:
    resposta = random.randint(1,6)
    lista_dados.append(resposta)
    i+=1
  return lista_dados
    
