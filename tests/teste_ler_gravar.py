import sys
from pathlib import Path

# 1. Encontra o caminho absoluto para a pasta raiz do projeto
# Path(__file__).resolve() dá o caminho deste ficheiro de teste.
# .parent.parent recua duas vezes no caminho (sai de testes/ e vai para a raiz)
raiz_projeto = str(Path(__file__).resolve().parent.parent)

# 2. Adiciona temporariamente a raiz do projeto ao 'sys.path' do Python
if raiz_projeto not in sys.path:
    sys.path.append(raiz_projeto)

# 3. Agora o Python já sabe onde está a pasta src! Já podes importar:
from src.ler_gravar import carregar_dados, guardar_dados


def executar_teste_persistencia():
    print("=== TESTE DE LEITURA E GRAVAÇÃO ===")
    
    # Tentamos carregar os dados. Se for a primeira vez, gera o modelo base
    dados = carregar_dados()
    print("1. Dados lidos do ficheiro:", dados)
    
    # Modificamos o perfil para testar a escrita
    dados["perfil"]["nome"] = "Carmen"
    dados["perfil"]["idade"] = 23
    dados["perfil"]["ultima_menstruacao"] = "2026-06-11"
    
    # Gravamos de volta
    guardar_dados(dados)
    print("2. Dados modificados com sucesso no ciclo_dados.json!")

if __name__ == "__main__":
    executar_teste_persistencia()


    #comando para testar: python3 -m tests.teste_ler_gravar