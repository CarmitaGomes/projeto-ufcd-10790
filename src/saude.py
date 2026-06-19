from src.ler_gravar import guardar_dados, carregar_medicos

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
    especialidades_sugeridas = set()


    if dias_menstruando > 7:
        print(f"{VERMELHO}[ALERTA MÁXIMO] Menstruação prolongada ({dias_menstruando} dias).")
        print(f"O parâmetro saudável é até 7 dias. Risco de Menorragia. Recomenda-se consulta médica.{RESET}")
        alerta = True
        especialidades_sugeridas.add("Ginecologia")

    if dias_fluxo_pesado >= 3:
        print(f"{AMARELO}[ALERTA MODERADO] Detetámos fluxo Pesado por {dias_fluxo_pesado} dias.")
        print(f"Monitorize os seus níveis de ferro para evitar anemia.{RESET}")
        alerta = True
        especialidades_sugeridas.add("Ginecologia")

    if dias_vomitos >= 2:
        print(f"{VERMELHO}[ALERTA SINTOMAS] Registou Vómitos em {dias_vomitos} dias do ciclo.")
        print(f"Dores ou sintomas gastrointestinais severos não devem ser ignorados.{RESET}")
        alerta = True
        especialidades_sugeridas.add("Clínica Geral")

    if not alerta and dias_menstruando > 0:
        print(f"{VERDE}[Ok] O teu ciclo menstrual encontra-se dentro dos parâmetros normais de duração.{RESET}")
        especialidades_sugeridas.add("Clínica Geral")

    print("\n-----------------------------------------")
    ajuda = input("Gostaria de ver uma lista de especialistas recomendados para a sua zona? (S/N): ").strip().upper()

    if ajuda == "S":
        mostrar_contactos_ajuda(dados, list(especialidades_sugeridas))
        
    else:
        print("\n• Linha Saúde 24: 808 24 24 24 (Apoio Geral Alternativo)")
        print("=========================================")



        
def mostrar_contactos_ajuda(dados, lista_especialidades):
    """
    Apresenta uma lista estática de apoio e especialidades médicas.
    """

    perfil = dados["perfil"]
    if "localizacao" not in perfil or perfil["localizacao"] == "":
        print("\n")
        zona = input("Introduza a sua Cidade/Zona (Ex: Lisboa / Porto): ").strip().capitalize()
        perfil["localizacao"] = zona
        guardar_dados(dados)

    zona_user = perfil["localizacao"]

    print(f"\nA procurar médicos na zona de {VERDE}{zona_user}{RESET}...")

    lista_medicos = carregar_medicos()

    medicos_zona = lista_medicos.get(zona_user, {})

    # CORREÇÃO: Varremos a lista, tratando uma especialidade de cada vez!
    for esp in lista_especialidades:
        # Agora 'esp' é uma string limpa (ex: "Ginecologia"), o que o .get() adora!
        lista_final = medicos_zona.get(esp, [])

        print(f"\n--- MÉDICOS RECOMENDADOS ({esp} - {zona_user}) ---")
        if lista_final:
            for med in lista_final:
                print(f"• {med['nome']} | Clínica: {med['clinica']} | Tel: {med['contacto']}")
        else:
            print(f"{AMARELO}[Aviso]{RESET} De momento, não temos médicos de {esp} registados para a zona '{zona_user}'.")
    print("=========================================")