"""
Ficheiro de Teste Interativo para validar os questionários do terminal
e a injeção de sintomas no dicionário do JSON.
"""
import sys
from pathlib import Path

# Configuração de pacotes e escopo do Python
raiz_projeto = str(Path(__file__).resolve().parent.parent)
if raiz_projeto not in sys.path:
    sys.path.insert(0, raiz_projeto)

from src.ler_gravar import carregar_dados, guardar_dados
from src.ciclo import calcular_fase_teorica, recolher_dia_menstruacao, recolher_dia_geral

def executar_teste_interativo():
    print("\n==================================================")
    
    # 1. Carrega o estado atual
    dados = carregar_dados()
    nome_user = dados["perfil"].get("nome", "Carmen")
    data_ultima = dados["perfil"].get("ultima_menstruacao", "2026-06-11")
    
    # 2. Calcula o dia com base nas funções do ciclo
    dia_atual = calcular_fase_teorica(data_ultima)
    print(f"Olá {nome_user}! Simulação interativa para o Dia {dia_atual} do ciclo.")
    print("==================================================")
    
    # 3. Dispara as perguntas
    print("\n[Simulação] Pretendes registar um dia de Menstruação?")
    opcao_fase = input("Digita (M) para Menstruação ou (G) para Geral: ").strip().upper()
    
    if opcao_fase == "M":
        resposta = recolher_dia_menstruacao(dia_atual)
        if resposta == "FIM_FLUXO":
            print("\n-> Teste capturou interrupção precoce (FIM_FLUXO).")
            return
    else:
        resposta = recolher_dia_geral(dia_atual, "Fase Folicular")
        
    # 4. Injeta na lista de registos e guarda
    dados["registos_ciclo"].append(resposta)
    guardar_dados(dados)
    print("\n[Sucesso] Respostas injetadas e salvas em src/dados_ciclo.json!")

if __name__ == "__main__":
    executar_teste_interativo()

    #comando para testar: python3 -m tests.teste_interativo
