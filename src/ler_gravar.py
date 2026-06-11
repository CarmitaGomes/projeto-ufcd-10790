import json
from pathlib import Path

FICHEIRO_DADOS = "dados_ciclo.json"


def carregar_dados():
    
    """
    Ler o que já está na estrutura.
    Se o ficheiro não existir, devolve estrutura base com perfil.
    """
    if not Path(FICHEIRO_DADOS).exists():
        return {
            "perfil": {"nome": "", "idade": 0, "ultima_menstruacao": ""},
            "registos_ciclo": []
        }
    
    with open(FICHEIRO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_dados(dados_atualizados):
    """
    Escreve na estrutura do ficheiro JSON.
    """
    with open(FICHEIRO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados_atualizados, f, indent=2, ensure_ascii=False)