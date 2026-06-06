import json
import os

def validar_vinculo_usina(usina_id):
    """
    [ESBOÇO] Função de validação de vínculo com a usina.
    Retorna True por enquanto; implementar lógica conforme necessidade.
    """
    print("\n⚠️ Validação de vínculo de usina ainda não implementada (Responsável: Arthur).")
    return True


def editar_usina_interactive():
    """Wrapper interativo que reutiliza a função de `modules.usinas`.
    Mantém compatibilidade e evita duplicação de lógica no repositório.
    """
    try:
        from modules.usinas import editar_usina
    except Exception:
        print("Erro ao importar módulos.usinas para edição.")
        return None
    return editar_usina()


def excluir_usina_interactive():
    """Wrapper interativo que reutiliza a função de `modules.usinas` para exclusão."""
    try:
        from modules.usinas import excluir_usina
    except Exception:
        print("Erro ao importar módulos.usinas para exclusão.")
        return None
    return excluir_usina()