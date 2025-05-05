import random
def rolar_dados(dados):
  lista_dados = []
  i = 0
  while i < dados:
    resposta = random.randint(1,6)
    lista_dados.append(resposta)
    i+=1
  return lista_dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
  if len(dados_no_estoque) < 4:
      dado = dados_rolados[dado_para_guardar]
      dados_no_estoque.append(dado)
      del dados_rolados[dado_para_guardar]
  return [dados_rolados, dados_no_estoque]

