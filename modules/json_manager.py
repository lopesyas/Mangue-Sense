import json
import os
from typing import Any


def load_json(caminho: str) -> Any:
    """Carrega um arquivo JSON. Normaliza um dict único para lista.
    Retorna lista, dict ou None em caso de erro.
    """
    if not os.path.exists(caminho):
        return None
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if isinstance(dados, dict):
                return [dados]
            return dados
    except Exception as e:
        print(f"Erro ao carregar JSON {caminho}: {e}")
        return None


def save_json(caminho: str, dados: Any) -> bool:
    """Salva dados em JSON. Cria diretório pai se necessário."""
    try:
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Erro ao salvar JSON {caminho}: {e}")
        return False
