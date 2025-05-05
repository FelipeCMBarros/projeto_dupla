#Aqui serão feitas as funções do jogo
import random
def rolar_dados(dados): #Exercício 1
  lista_dados = []
  i = 0
  while i < dados:
    resposta = random.randint(1,6)
    lista_dados.append(resposta)
    i+=1
  return lista_dados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar): #Exercício 2
    nova_lista_rolados = dados_rolados.copy()
    nova_lista_estoque = dados_no_estoque.copy()

    if 0 <= dado_para_guardar < len(nova_lista_rolados):
        dado = nova_lista_rolados[dado_para_guardar]
        nova_lista_estoque.append(dado)
        del nova_lista_rolados[dado_para_guardar]

    return [nova_lista_rolados, nova_lista_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover): #Exercício 3
    nova_lista_rolados = dados_rolados.copy()
    nova_lista_estoque = dados_no_estoque.copy()

    if 0 <= dado_para_remover < len(nova_lista_estoque):
        dado = nova_lista_estoque[dado_para_remover]
        nova_lista_rolados.append(dado)
        del nova_lista_estoque[dado_para_remover]

    return [nova_lista_rolados, nova_lista_estoque]


