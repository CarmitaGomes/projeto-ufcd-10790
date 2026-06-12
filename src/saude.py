
# Cores para formatar o terminal
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
RESET = "\033[0m"

def analisar_saude_ciclo(dados):
    historico = dados.get("registos_ciclo", [])
    print("\n=========================================")
    print("    SISTEMA DE ANÁLISE DE SAÚDE  ")
    print("=========================================")

    if not historico:
        print(f"{AMARELO}[Aviso]{RESET} Ainda não existem dias registados para analisar.")
        return
    
    dias_menstruando = 0
    dias_vomitos = 0
    dias_fluxo_pesado = 0

    for dia in historico:
        if dia.get("fase") == "Menstruação":
            dias_menstruando += 1
    
            if dia.get("fluxo") == "Pesado":
                dias_fluxo_pesado += 1

        sintomas = dia.get("sintomas_adicionais", [])
        if "Vómitos" in sintomas:
            dias_vomitos += 1

    print(f"\n-> Resumo Clínico: Detetámos {dias_menstruando} dias de menstruação.")

    alerta = False

    if dias_menstruando > 7:
        print(f"{VERMELHO}[ALERTA MÁXIMO] Menstruação prolongada ({dias_menstruando} dias).")
        print(f"O parâmetro saudável é até 7 dias. Risco de Menorragia. Recomenda-se consulta médica.{RESET}")
        alerta = True

    if dias_fluxo_pesado >= 3:
        print(f"{AMARELO}[ALERTA MODERADO] Detetámos fluxo Pesado por {dias_fluxo_pesado} dias.")
        print(f"Monitorize os seus níveis de ferro para evitar anemia.{RESET}")
        alerta = True

    if dias_vomitos >= 2:
        print(f"{VERMELHO}[ALERTA SINTOMAS] Registou Vómitos em {dias_vomitos} dias do ciclo.")
        print(f"Dores ou sintomas gastrointestinais severos não devem ser ignorados.{RESET}")
        alerta = True

    if not alerta and dias_menstruando > 0:
        print(f"{VERDE}[Ok] O teu ciclo menstrual encontra-se dentro dos parâmetros normais de duração.{RESET}")

    mostrar_contactos_ajuda()

    
        
def mostrar_contactos_ajuda():
    """
    Apresenta uma lista estática de apoio e especialidades médicas.
    """
    print("\n-----------------------------------------")
    print("        CONTACTOS E RECOMENDAÇÕES        ")
    print("-----------------------------------------")
    print("• Linha Saúde 24: 808 24 24 24 (Apoio Geral)")
    print("• Especialidade Recomendada: Ginecologia / Obstetrícia")
    #print("• Hospitais de Referência: Consultar Serviço de Urgência da sua área residencial.")
    print("=========================================")