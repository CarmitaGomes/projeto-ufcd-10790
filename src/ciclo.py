"""
Módulo responsável por gerir a recolha de dados diários 
e simular a passagem dos 28 dias do ciclo menstrual.
"""
from datetime import datetime

def calcular_fase_teorica(data_ultima_str):
    """
    Com base na data da última menstruação fornecida no perfil,
    calcula teoricamente em que dia do ciclo (1 a 28) a utilizadora está hoje.
    """
    try:
        # Converte o texto guardado no JSON para um objeto de data real do Python
        data_ultima = datetime.strptime(data_ultima_str, "%Y-%m-%d")
        data_atual = datetime.now()
        
        # Calcula a diferença absoluta em dias
        diferenca_dias = (data_atual - data_ultima).days
        
        # O ciclo reinicia a cada 28 dias. O operador % descobre o dia atual (1-28)
        dia_ciclo = (diferenca_dias % 28) + 1
        return dia_ciclo
    except Exception:
        # Caso ocorra algum erro de digitação de datas, assume o dia 1 
        return 1

def recolher_dia_menstruacao(numero_dia):
    """
    Gere o menu interativo no terminal para capturar os sintomas
    específicos de um dia da Fase de Menstruação (Semana 1).
    """
    print(f"\n--- REGISTO DO DIA {numero_dia} (Fase de Menstruação) ---")
    print("Se a tua menstruação terminou hoje, digite [F] para Finalizar esta fase.")

    # 1. Captura da Intensidade do Fluxo
    ## retirar a opção F, já não será necessária
    print("1 - Intensidade do Fluxo:")
    print("    [P] Pesado | [M] Médio | [L] Ligeiro ")
    fluxo_input = input("Escolha a opção (P/M/L): ").strip().upper()
    
    # Validação segura com .get()
    fluxo_map = {"P": "Pesado", "M": "Médio", "L": "Ligeiro"}
    fluxo = fluxo_map.get(fluxo_input, "Médio")
    
    # 2. Captura da Intensidade das Cólicas
    ## colocar opção para escolher ou não registar cólicas
    print("\n2 - Intensidade das Cólicas:")
    print("    [P] Pesadas | [M] Medianas | [L] Ligeiras | [N] Nenhuma")
    colicas_input = input("Escolha a opção (P/M/L/N): ").strip().upper()
    
    colicas_map = {"P": "Pesadas", "M": "Medianas", "L": "Ligeiras", "N": "Nenhuma"}
    colicas = colicas_map.get(colicas_input, "Nenhuma")
    
    # 3. Captura de Sintomas Adicionais (Uso de loop while com flag de saída)
    sintomas_adicionais = []
    print("\n3 - Selecione sintomas adicionais (digite o número ou '0' para terminar):")
    print("    1. Vómitos\n    2. Cansaço\n    3. Insónia\n    4. Dores de cabeça")
    
    opcoes_sintomas = {"1": "Vómitos", "2": "Cansaço", "3": "Insónia", "4": "Dores de cabeça"}
    
    while True:
        opcao = input("Adicionar sintoma (0 para sair): ").strip()
        if opcao == "0":
            break
        if opcao in opcoes_sintomas:
            sintoma_nome = opcoes_sintomas[opcao]
            if sintoma_nome not in sintomas_adicionais:
                sintomas_adicionais.append(sintoma_nome)
                print(f"  -> {sintoma_nome} adicionado.")
            else:
                print("  (! ) Esse sintoma já foi adicionado!")
        else:
            print("  (! ) Opção inválida. Tenta de novo.")
            
    # Retorna o dicionário estruturado com as respostas recolhidas
    return {
        "dia_ciclo": numero_dia,
        "fase": "Menstruação",
        "fluxo": fluxo,
        "colicas": colicas,
        "sintomas_adicionais": sintomas_adicionais
    }


def recolher_dia_geral(numero_dia, nome_fase):
    """
    Gere o menu interativo para as restantes fases do ciclo (Semanas 2, 3 e 4),
    onde o fluxo menstrual já não está presente.
    """
    print(f"\n--- REGISTO DO DIA {numero_dia} ({nome_fase}) ---")
    
    # Para as outras fases, monitorizamos os níveis de energia e humor
    print("1 - Nível de Energia Geral:")
    print("    [A] Alto | [M] Moderado | [B] Baixo")
    energia_input = input("Escolha a opção (A/M/B): ").strip().upper()
    energia_map = {"A": "Alto", "M": "Moderado", "B": "Baixo"}
    energia = energia_map.get(energia_input, "Moderado")
    
    # Sintomas comuns das outras fases (como acne ou retenção de líquidos)
    sintomas_adicionais = []
    print("\n2 - Selecione sintomas detetados (digite o número ou '0' para terminar):")
    print("    1. Acne\n    2. Mudanças de Humor\n    3. Retenção de Líquidos\n    4. Sensibilidade Mamária")
    
    opcoes_sintomas = {"1": "Acne", "2": "Mudanças de Humor", "3": "Retenção de Líquidos", "4": "Sensibilidade Mamária"}
    
    while True:
        opcao = input("Adicionar sintoma (0 para sair): ").strip()
        if opcao == "0":
            break
        if opcao in opcoes_sintomas:
            sintoma_nome = opcoes_sintomas[opcao]
            if sintoma_nome not in sintomas_adicionais:
                sintomas_adicionais.append(sintoma_nome)
                print(f"  -> {sintoma_nome} adicionado.")
            else:
                print("  (! ) Esse sintoma já foi adicionado!")
        else:
            print("  (! ) Opção inválida. Tenta de novo.")
            
    return {
        "dia_ciclo": numero_dia,
        "fase": nome_fase,
        "energia": energia,
        "sintomas_adicionais": sintomas_adicionais
    }