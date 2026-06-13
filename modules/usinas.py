import os
from modules.json_manager import load_json, save_json

# Caminho para persistência em JSON
CAMINHO_USINAS = os.path.join(os.path.dirname(__file__), "..", "data", "usinas.json")


def _carregar_usinas():
    """Carrega usinas do JSON e normaliza campos legados (chaves PT → chaves EN)."""
    dados = load_json(CAMINHO_USINAS)
    if not dados:
        return []

    normalizados = []
    for item in dados:
        # Suporte a chaves legadas em português (dados antigos no JSON)
        usina = {
            "id":              int(item.get("id") or item.get("ID da usina", 0)),
            "nome":            str(item.get("nome") or item.get("Nome da usina", "")),
            "empresa":         str(item.get("empresa") or item.get("Empresa responsável pela usina", "")),
            "cidade":          str(item.get("cidade") or item.get("Cidade da usina", "")),
            "estado":          str(item.get("estado") or item.get("UF da usina", "")),
            "potencia":        float(item.get("potencia") or item.get("Potência da usina (kWp)", 0.0)),
            "qtd_paineis":     int(item.get("qtd_paineis") or item.get("Quantidade de painéis", 0)),
            "data_instalacao": str(item.get("data_instalacao") or item.get("Data de instalação", "")),
            "status_usina":    str(item.get("status_usina") or item.get("Status da usina", "ATIVA")),
            # Campos obrigatórios do MVP — garante que existam mesmo em registros antigos
            "score_geracao":   item.get("score_geracao", 100),
            "status_risco":    item.get("status_risco", "OK"),
            "dados_operacionais": item.get("dados_operacionais", []),
        }
        normalizados.append(usina)

    return normalizados


def _salvar_usinas(dados):
    save_json(CAMINHO_USINAS, dados)


# Lista em memória carregada ao importar o módulo
usinas = _carregar_usinas()


# ──────────────────────────────────────────────
# CRUD
# ──────────────────────────────────────────────

def cadastrar_usina():
    print("\n==== CADASTRO DE USINA ====")

    # ID automático: maior existente + 1
    proximo_id = max((u["id"] for u in usinas), default=0) + 1
    print(f"ID gerado automaticamente: {proximo_id}")

    nova_usina = {
        "id":              proximo_id,
        "nome":            input("Nome da usina: ").strip().title(),
        "empresa":         input("Empresa responsável: ").strip().title(),
        "cidade":          input("Cidade: ").strip().title(),
        "estado":          input("UF (sigla): ").strip().upper(),
        "potencia":        0.0,
        "qtd_paineis":     0,
        "data_instalacao": input("Data de instalação (DD/MM/AAAA): ").strip(),
        "status_usina":    input("Status da usina (ATIVA/INATIVA): ").strip().upper(),
        # Campos obrigatórios do MVP
        "score_geracao":        100,
        "status_risco":         "OK",
        "dados_operacionais":   [],
    }

    try:
        nova_usina["potencia"] = float(input("Potência (kWp): "))
    except ValueError:
        print("⚠️ Potência inválida. Definindo como 0.0")

    try:
        nova_usina["qtd_paineis"] = int(input("Quantidade de painéis: "))
    except ValueError:
        print("⚠️ Quantidade inválida. Definindo como 0")

    usinas.append(nova_usina)
    _salvar_usinas(usinas)

    print("\n=========== USINA CADASTRADA ===========")
    _exibir_usina(nova_usina)
    print("✅ Usina cadastrada com sucesso!")
    return nova_usina


def listar_usinas():
    print("\n=========== LISTA DE USINAS ===========")
    if not usinas:
        print("⚠️ Nenhuma usina cadastrada.")
        return
    for usina in usinas:
        _exibir_usina(usina)
        print("=" * 40)


def editar_usina():
    try:
        id_editar = int(input("\nID da usina para editar: "))
    except ValueError:
        print("❌ ID inválido!")
        return

    for usina in usinas:
        if usina["id"] == id_editar:
            print(f"\nEditando: {usina['nome']} — deixe em branco para manter o valor atual.")

            novo_nome    = input(f"Nome [{usina['nome']}]: ").strip().title()
            nova_empresa = input(f"Empresa [{usina['empresa']}]: ").strip().title()
            nova_cidade  = input(f"Cidade [{usina['cidade']}]: ").strip().title()
            novo_estado  = input(f"UF [{usina['estado']}]: ").strip().upper()

            if novo_nome:    usina["nome"]    = novo_nome
            if nova_empresa: usina["empresa"] = nova_empresa
            if nova_cidade:  usina["cidade"]  = nova_cidade
            if novo_estado:  usina["estado"]  = novo_estado

            nova_potencia = input(f"Potência [{usina['potencia']}]: ").strip()
            if nova_potencia:
                try:
                    usina["potencia"] = float(nova_potencia)
                except ValueError:
                    print("⚠️ Potência inválida. Mantendo valor anterior.")

            _salvar_usinas(usinas)
            print("✅ Usina editada com sucesso!")
            return

    print("❌ Nenhuma usina encontrada com esse ID.")


def excluir_usina():
    resposta = input("\nDeseja excluir alguma usina? (S/N): ").strip().upper()
    if resposta != "S":
        print("Exclusão cancelada.")
        return

    try:
        id_excluir = int(input("ID da usina para excluir: "))
    except ValueError:
        print("❌ ID inválido!")
        return

    for usina in usinas:
        if usina["id"] == id_excluir:
            confirmacao = input(f"Confirmar exclusão de '{usina['nome']}'? (S/N): ").strip().upper()
            if confirmacao == "S":
                usinas.remove(usina)
                _salvar_usinas(usinas)
                print("✅ Usina excluída com sucesso!")
            else:
                print("Exclusão cancelada.")
            return

    print("❌ Nenhuma usina encontrada com esse ID.")


# ──────────────────────────────────────────────
# Utilitário interno
# ──────────────────────────────────────────────

def _exibir_usina(usina):
    print(f"  ID:              {usina['id']}")
    print(f"  Nome:            {usina['nome']}")
    print(f"  Empresa:         {usina['empresa']}")
    print(f"  Cidade/UF:       {usina['cidade']}/{usina['estado']}")
    print(f"  Potência:        {usina['potencia']} kWp")
    print(f"  Painéis:         {usina['qtd_paineis']}")
    print(f"  Instalação:      {usina['data_instalacao']}")
    print(f"  Status usina:    {usina['status_usina']}")
    print(f"  Score geração:   {usina['score_geracao']}")
    print(f"  Status risco:    {usina['status_risco']}")


if __name__ == "__main__":
    listar_usinas()
