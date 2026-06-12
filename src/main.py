# Aqui vai o código principal do seu projeto
#
from src.ler_gravar import carregar_dados, guardar_dados
from src.ciclo import recolher_dia_menstruacao, recolher_dia_geral

def inicializar_perfil(dados):
    if dados["perfil"]["nome"] == "":
        print("\n=========================================")
        print("    BEM-VINDA AO CONFIGURADOR DE PERFIL  ")
        print("=========================================")

        nome = input("Introduza o seu nome: ").strip()
        idade = int(input("Introduza a sua idade: "))
        print("Introduzir data no formato AAAA-MM-DD")
        ultima_mes = input("Data da ultima menstruação: ").strip()

        dados["perfil"]["nome"] = nome
        dados["perfil"]["idade"] = idade
        dados["perfil"]["ultima_menstruacao"] = ultima_mes

        guardar_dados(dados)
        print("\n[Boa] Perfil gravado no dados_ciclo.json!")
    else:
        print(f"\nOlá outra vez, {dados['perfil']['nome']}!")
    
    return dados

def gerir_fluxo_diario(dados):

    while True:
        historico = dados["registos_ciclo"]
        dia_atual = len(dados["registos_ciclo"]) + 1

        print("\n=========================================")
        print(f"       REGISTO DIÁRIO - DIA {dia_atual} DO CICLO       ")
        print("=========================================")
        print("1. Registar sintomas do dia de hoje")
        print("2. Sair do programa")

        opcao = input("Escolha uma opção (1/2): ").strip()

        if opcao == "1":
            esta_menstruada = "N"
            if dia_atual == 1:
                print(f"\nNo dia {dia_atual} do teu ciclo, estás menstruada?")
                esta_menstruada = input("Responda (S) para Sim ou (N) para Não: ").strip().upper()

            else:
                ultimo_registo = historico[-1]  

                if ultimo_registo.get("fase") == "Menstruação":
                    print(f"\nNo dia {dia_atual} do teu ciclo, ainda estás menstruada?")
                    esta_menstruada = input("Responda (S) para Sim ou (N) para Não: ").strip().upper()
                else:
                    esta_menstruada = "N"

            if esta_menstruada == "S":
                resposta_dia = recolher_dia_menstruacao(dia_atual)

        
            else:

                fase_estimada = "Fase Folicular" if dia_atual <= 11 else ("Ovulação" if dia_atual <= 16 else "Fase Lútea")
                resposta_dia = recolher_dia_geral(dia_atual, fase_estimada)

            dados["registos_ciclo"].append(resposta_dia)
            guardar_dados(dados)
            print(f"\n[Boa] Dados do Dia {dia_atual} adicionados ao histórico!")

        elif opcao == "2":
            print("\nA fechar aplicação...")
            break
        else:
            print("\nOpção inválida! selecione 1 ou 2.")






def main():
    print("=== PERIOD TRACKER ===")
    dados = carregar_dados()
    dados = inicializar_perfil(dados)
    # Você pode adicionar mais funcionalidades aqui

    gerir_fluxo_diario(dados)


if __name__ == "__main__":
    main()

