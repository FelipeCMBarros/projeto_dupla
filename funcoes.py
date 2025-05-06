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

def calcula_pontos_regra_simples(dados): #Exercício 4
    pontos = {i: 0 for i in range(1, 7)}
    
    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado
            
    return pontos

def calcula_pontos_soma(dados): #Exercício 5
    total = 0
    for dado in dados:
        total += dado
    return total

def calcula_pontos_sequencia_baixa(dados): #Exercício 6
    unicos = sorted(set(dados))  
    consecutivos = 1  

    for i in range(1, len(unicos)):
        if unicos[i] == unicos[i - 1] + 1:
            consecutivos += 1
            if consecutivos >= 4:
                return 15
        else:
            consecutivos = 1  

    return 0

def calcula_pontos_sequencia_alta(dados): #Exercício 7
    unicos = sorted(set(dados))  # Remove duplicatas e ordena
    consecutivos = 1  # Contador de sequência atual

    for i in range(1, len(unicos)):
        if unicos[i] == unicos[i - 1] + 1:
            consecutivos += 1
            if consecutivos >= 5:
                return 30
        else:
            consecutivos = 1  # Reinicia a contagem

    return 0

def calcula_pontos_full_house(dados): #Exercício 8
    contagem = {}
    
    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
    
    valores_contagem = list(contagem.values())
    
    if sorted(valores_contagem) == [2, 3]:
        soma = 0
        for valor in dados:
            soma += valor
        return soma
    else:
        return 0
    
def calcula_pontos_quadra(dados): #Exercício 9
    contagem = {}

    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    for quantidade in contagem.values():
        if quantidade >= 4:
            soma = 0
            for valor in dados:
                soma += valor
            return soma

    return 0

def calcula_pontos_quina(dados): #Exercício 10
    contagem = {}

    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50

    return 0

def calcula_pontos_regra_avancada(dados): #Exercício 11
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(dados, categoria, cartela_de_pontos): #Exercício 12
    # Calcula os pontos
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancados = calcula_pontos_regra_avancada(dados)

    # Verifica se a categoria é simples (ex: "1", "2", ..., "6")
    if categoria.isdigit():
        numero = int(categoria)
        cartela_de_pontos['regra_simples'][numero] = pontos_simples[numero]
    else:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]

    return cartela_de_pontos

def imprime_cartela(cartela): #Exercício 13
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)