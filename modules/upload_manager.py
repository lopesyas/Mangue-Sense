import os
import json
import shutil
from datetime import datetime


def validar_arquivo_imagem(caminho_arquivo):
    """
    Valida uma imagem térmica.

    Regras:
    - Arquivo deve existir
    - Deve ser um arquivo
    - Extensão permitida: .jpg, .jpeg, .png
    - Tamanho máximo: 10 MB
    """

    # Verifica existência
    if not os.path.exists(caminho_arquivo):
        return False, "Arquivo não encontrado."

    # Verifica se é arquivo
    if not os.path.isfile(caminho_arquivo):
        return False, "O caminho informado não é um arquivo."

    # Verifica extensão
    extensao = os.path.splitext(caminho_arquivo)[1].lower()
    extensoes_permitidas = [".jpg", ".jpeg", ".png"]

    if extensao not in extensoes_permitidas:
        return False, "Extensão inválida. Use JPG, JPEG ou PNG."

    # Verifica tamanho
    tamanho = os.path.getsize(caminho_arquivo)

    if tamanho > (10 * 1024 * 1024):
        return False, "Arquivo maior que 10 MB."

    return True, "Arquivo válido."


def fazer_upload_imagem_termica(caminho_arquivo):
    """
    Faz upload da imagem térmica para a pasta uploads.

    Exemplo de nome:
    USINA_1_20260604_101530.jpg
    """

    valido, mensagem = validar_arquivo_imagem(caminho_arquivo)

    if not valido:
        raise ValueError(mensagem)

    # Caminho da pasta uploads na raiz do projeto
    raiz_projeto = os.path.dirname(os.path.dirname(__file__))
    pasta_uploads = os.path.join(raiz_projeto, "uploads")

    # Cria a pasta caso não exista
    os.makedirs(pasta_uploads, exist_ok=True)

    # Obtém extensão original
    extensao = os.path.splitext(caminho_arquivo)[1].lower()

    # Gera timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Nome solicitado pelo enunciado
    novo_nome = f"USINA_1_{timestamp}{extensao}"

    # Caminho final
    caminho_destino = os.path.join(pasta_uploads, novo_nome)

    # Copia o arquivo
    shutil.copy2(caminho_arquivo, caminho_destino)

    return caminho_destino