import random
def rolar_dados(dados):
  lista_dados = []
  i = 0
  while i < dados:
    resposta = random.randint(1,6)
    lista_dados.append(resposta)
    i+=1
  return lista_dados

def guardar_dado(dados_rolados, dados_guardados, i):
  if len(dados_guardados) < 4:
    dados_guardados.append(dados_rolados[i])
    dados_rolados.remove(dados_rolados[i])

  lista = [dados_rolados, dados_guardados]
  return lista

