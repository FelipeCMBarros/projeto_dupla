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
  dado_para_guardar = int(input("Qual dado será guardado?"))
  for dado_para_guardar in dados_rolados:
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    dados_rolados.remove(dados_rolados[dado_para_guardar])

  lista = [dados_rolados, dados_no_estoque]
  return lista

