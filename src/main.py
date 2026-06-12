# Aqui vai o código principal do seu projeto
#
from src.ler_gravar import carregar_dados, guardar_dados

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



def main():
    print("=== PERIOD TRACKER ===")
    dados = carregar_dados()
    dados = inicializar_perfil(dados)
    # Você pode adicionar mais funcionalidades aqui


if __name__ == "__main__":
    main()

