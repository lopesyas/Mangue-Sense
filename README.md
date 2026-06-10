# ☀️ Mangue-Sense

O **Mangue-Sense** é um sistema modular em linha de comando desenvolvido em Python para o gerenciamento inteligente de usinas solares e seus equipamentos vinculados. O sistema visa monitorar a integridade operacional das placas e componentes por meio do registro de dados físicos e térmicos.

---

## 🚀 Funcionalidades

### 📈 Gerenciamento de Usinas
* **Cadastro Completo:** Registro de ID da usina, nome, empresa responsável, cidade, UF, potência nominal (kWp), quantidade de painéis solares, data de instalação e status atual.
* **Listagem em Tempo Real:** Visualização organizada de todas as usinas registradas com layout limpo e formatado.
* **Edição de Dados:** Permite atualizar informações cadastrais das usinas instantaneamente.
* **Exclusão Segura:** Remoção de usinas com tela de confirmação de segurança `(S/N)`.

### ⚙️ Gerenciamento de Equipamentos
* **Cadastro de Dispositivos:** Registro de ID do equipamento, nome, tipo, fabricante, modelo, data de instalação, status operacional e vinculação direta com a usina correspondente.
* **Visualização Completa:** Exibição estruturada com o status e a usina à qual cada equipamento está vinculado.
* **Placeholders Integrados:** Menus e rotas de código prontos para as futuras funcionalidades de edição e exclusão de equipamentos.
* **API unificada:** Fiz a unificação do nome da função de cadastro para `cadastrar_equipamento()` e mantive um alias compatível para evitar que imports antigos quebrem.

### 💾 Persistência de Dados & Arquitetura
* **Banco de Dados JSON:** Todos os registros são salvos automaticamente de forma persistente nas tabelas de arquivos em `data/usinas.json` e `data/equipamentos.json`.
* **Sincronização Bidirecional:** O sistema normaliza dinamicamente as chaves cadastradas para garantir a compatibilidade entre diferentes módulos desenvolvidos pela equipe.
* **Menu Interativo Dinâmico:** Interface no console limpa, fácil de navegar e com tratamento nativo contra entradas inválidas ou falhas de digitação.

---

## 📂 Estrutura do Projeto

```text
Mangue-Sense/
├── main.py                 # Ponto de entrada do sistema
├── requirements.txt        # Dependências do projeto (caso aplicável)
├── data/
│   ├── usinas.json         # Base de dados persistente de usinas
│   └── equipamentos.json   # Base de dados persistente de equipamentos
└── modules/
  ├── interface.py        # Orquestração de menus e navegação do console
  ├── usinas.py           # Operações e regras de negócio de usinas
  ├── equipamentos.py     # Operações e regras de negócio de equipamentos (API unificada)
  ├── json_manager.py     # Utilitários para carregar/salvar JSON (`load_json`, `save_json`)
  └── validacoes.py       # Validações e wrappers que reutilizam `usinas.py`
```

---

## 🛠️ Como Executar

### Pré-requisitos
* Python 3.x instalado em sua máquina.

### Executando o Sistema
1. Abra o seu terminal na pasta raiz do projeto.
2. Execute o comando:
   ```bash
   python3 main.py
   ```
3. Navegue utilizando as opções numéricas apresentadas no console interativo.

Observações rápidas sobre mudanças recentes:
- Fiz a normalização do carregamento de JSON em `modules/equipamentos.py` para aceitar um único objeto (dict) transformando-o em lista `[dict]`, evitando perda de dados quando o arquivo contém um único registro.
- Adicionei `modules/json_manager.py` com helpers para centralizar IO de JSON (`load_json` / `save_json`).
- Refatorei `modules/validacoes.py` para remover código interativo duplicado e criei wrappers que reutilizam `modules/usinas.py` para edição/exclusão.
- Corrigi um valor inválido em `data/usinas.json` (campo `Data de instalação`) para uma data plausível.

Se quiser, eu posso: organizar as chaves internas para um único padrão (ex.: snake_case em inglês), adicionar testes `pytest` ou rodar um formatador como `black` para padronizar o estilo.

---

## 📅 Roadmap de Desenvolvimento

### Próximos Passos (Próximas Semanas):
* **ÉPICO 4 — Upload e Armazenamento de Dados:**
  - [ ] Implementação de upload físico de imagens locais.
  - [ ] Registro e armazenamento estruturado de dados históricos de temperatura, geração e desempenho.
* **ÉPICO 5 — Inteligência e Cálculos:**
  - [ ] Função de cálculo automatizado do Diferencial Térmico ($\Delta T$) para detecção de anomalias térmicas.
  - [ ] Geração automática do Score de Desempenho e Eficiência associado à usina.
