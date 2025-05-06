# Aqui será feito o programa do jogo
from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodadas = 0

while rodadas < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    while True:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input(">")

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            try:
                indice = int(input(">"))
                if 0 <= indice < len(dados_rolados):
                    dados_guardados.append(dados_rolados.pop(indice))
                else:
                    print("Índice inválido.")
            except:
                print("Entrada inválida.")

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            try:
                indice = int(input(">"))
                if 0 <= indice < len(dados_guardados):
                    dados_rolados.append(dados_guardados.pop(indice))
                else:
                    print("Índice inválido.")
            except:
                print("Entrada inválida.")

        elif opcao == '3':
            if rerrolagens < 2:
                rerrolagens += 1
                dados_rolados = rolar_dados(len(dados_rolados))
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            combinacao = input(">").strip()

            dados_finais = dados_rolados + dados_guardados

            if combinacao.isdigit():
                numero = int(combinacao)
                if numero not in cartela['regra_simples']:
                    print("Combinação inválida. Tente novamente.")
                    continue
                if cartela['regra_simples'][numero] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
                cartela = faz_jogada(dados_finais, str(numero), cartela)
                break  # <<< SAI DO LOOP DA RODADA

            elif combinacao in cartela['regra_avancada']:
                if cartela['regra_avancada'][combinacao] != -1:
                    print("Essa combinação já foi utilizada.")
                    continue
                cartela = faz_jogada(dados_finais, combinacao, cartela)
                break  # <<< SAI DO LOOP DA RODADA

            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodadas += 1  # <=== só conta a rodada quando a jogada foi feita

imprime_cartela(cartela)

total = 0
for valor in cartela['regra_simples'].values():
    if valor != -1:
        total += valor
for valor in cartela['regra_avancada'].values():
    if valor != -1:
        total += valor

print(f"Pontuação total: {total}")