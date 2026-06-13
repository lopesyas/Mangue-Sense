
def calcular_diferencial_termico(t_equipamento, t_ambiente):
	"""Calcula ΔT e retorna dict com valor, status, valido e mensagem.
	Regras de classificação:
	- ≤25 -> OK
	- 25 < ΔT ≤ 40 -> ALERTA
	- >40 -> CRÍTICO
	Validações:
	- t_equipamento entre -15 e 150
	- t_ambiente entre -15 e 60
	"""
	try:
		te = float(t_equipamento)
		ta = float(t_ambiente)
	except (TypeError, ValueError):
		return {"valor": None, "status": "INVALIDO", "valido": False, "mensagem": "Temperaturas devem ser numéricas."}

	if not (-15 <= te <= 150):
		return {"valor": None, "status": "INVALIDO", "valido": False, "mensagem": "Temperatura do equipamento fora dos limites (-15..150)."}
	if not (-15 <= ta <= 60):
		return {"valor": None, "status": "INVALIDO", "valido": False, "mensagem": "Temperatura ambiente fora dos limites (-15..60)."}

	dt = te - ta
	if dt <= 25:
		status = "OK"
	elif dt <= 40:
		status = "ALERTA"
	else:
		status = "CRÍTICO"

	return {"valor": dt, "status": status, "valido": True, "mensagem": "Cálculo realizado com sucesso."}


def calcular_score_geracao(atual, esperada):
	"""Calcula score de geração em porcentagem e classifica.
	Validações: esperada != 0, atual >=0, esperada >=0
	Classificação:
	- >80 -> OK
	- 50 ≤ score ≤ 80 -> ALERTA
	- <50 -> CRÍTICO
	"""
	try:
		atual_v = float(atual)
		esperada_v = float(esperada)
	except (TypeError, ValueError):
		return {"valor": None, "status": "INVALIDO", "valido": False, "mensagem": "Valores devem ser numéricos."}

	if esperada_v <= 0:
		return {"valor": None, "status": "INVALIDO", "valido": False, "mensagem": "Valor esperado deve ser maior que zero."}
	if atual_v < 0:
		return {"valor": None, "status": "INVALIDO", "valido": False, "mensagem": "Valor atual não pode ser negativo."}

	score = (atual_v / esperada_v) * 100

	if score > 80:
		status = "OK"
	elif score >= 50:
		status = "ALERTA"
	else:
		status = "CRÍTICO"

	return {"valor": score, "status": status, "valido": True, "mensagem": "Cálculo realizado com sucesso."}


def classificar_risco_usina(dt_status, score_status):
	"""Classifica risco geral da usina a partir dos status de ΔT e Score.
	Aceita strings como entrada. Retorna 'CRÍTICO', 'ALERTA' ou 'OK'.
	"""
	s_dt = str(dt_status).strip().upper()
	s_score = str(score_status).strip().upper()

	if any(k in s_dt or k in s_score for k in ("CRIT", "CRÍT")):
		return "CRÍTICO"
	if "ALERT" in s_dt or "ALERT" in s_score:
		return "ALERTA"
	return "OK"


def testar_calculos():
	"""Roda 9 casos de teste com output detalhado por caso.
	Retorna True se todos passarem, caso contrário False.
	"""
	failures = []
	resultados = []

	def _checar(nome, descricao, resultado_obtido, esperado_status, unidade="", valor_fmt=None):
		ok = resultado_obtido["valido"] and resultado_obtido["status"] == esperado_status
		if valor_fmt:
			ok = ok and valor_fmt(resultado_obtido["valor"])
		status_icon = "✅ PASSOU" if ok else "❌ FALHOU"
		valor = resultado_obtido.get("valor")
		valor_str = f"  →  resultado = {round(valor, 1)}{unidade}" if valor is not None else ""
		print(f"  {status_icon}  [{nome}] {descricao}{valor_str}  →  {resultado_obtido['status']}")
		if not ok:
			failures.append(nome)

	print("\n========================================")
	print("     MOTOR DE CÁLCULO — SUITE DE TESTES")
	print("========================================")

	# ── Bloco 1: Diferencial Térmico ──────────────
	print("\n  [ DIFERENCIAL TÉRMICO (ΔT) ]")

	r = calcular_diferencial_termico(40, 20)
	_checar("dt_ok",      "Equip 40°C / Amb 20°C  →  esperado OK",      r, "OK",      "°C")

	r = calcular_diferencial_termico(65, 30)
	_checar("dt_alerta",  "Equip 65°C / Amb 30°C  →  esperado ALERTA",  r, "ALERTA",  "°C")

	r = calcular_diferencial_termico(120, 60)
	_checar("dt_critico", "Equip 120°C / Amb 60°C →  esperado CRÍTICO", r, "CRÍTICO", "°C")

	# ── Bloco 2: Score de Geração ──────────────────
	print("\n  [ SCORE DE GERAÇÃO (%) ]")

	s = calcular_score_geracao(900, 1000)
	_checar("score_ok",      "Geração 900/1000 kWh   →  esperado OK",      s, "OK",      "%")

	s = calcular_score_geracao(800, 1000)
	_checar("score_alerta",  "Geração 800/1000 kWh   →  esperado ALERTA",  s, "ALERTA",  "%")

	s = calcular_score_geracao(200, 1000)
	_checar("score_critico", "Geração 200/1000 kWh   →  esperado CRÍTICO", s, "CRÍTICO", "%")

	# ── Bloco 3: Classificação de Risco da Usina ──
	print("\n  [ CLASSIFICAÇÃO DE RISCO DA USINA ]")

	r1 = classificar_risco_usina("OK", "OK")
	icon1 = "✅ PASSOU" if r1 == "OK" else "❌ FALHOU"
	print(f"  {icon1}  [risco_ok]      ΔT OK   + Score OK      →  {r1}")
	if r1 != "OK": failures.append("risco_ok")

	r2 = classificar_risco_usina("ALERTA", "OK")
	icon2 = "✅ PASSOU" if r2 == "ALERTA" else "❌ FALHOU"
	print(f"  {icon2}  [risco_alerta]  ΔT ALERTA + Score OK    →  {r2}")
	if r2 != "ALERTA": failures.append("risco_alerta")

	r3 = classificar_risco_usina("OK", "CRÍTICO")
	icon3 = "✅ PASSOU" if r3 == "CRÍTICO" else "❌ FALHOU"
	print(f"  {icon3}  [risco_critico] ΔT OK   + Score CRÍTICO →  {r3}")
	if r3 != "CRÍTICO": failures.append("risco_critico")

	# ── Resultado final ────────────────────────────
	print("\n========================================")
	total = 9
	passou = total - len(failures)
	if not failures:
		print(f"  RESULTADO: {passou}/{total} testes passaram")
		print("  ✅ TODOS OS TESTES PASSARAM")
	else:
		print(f"  RESULTADO: {passou}/{total} testes passaram")
		print(f"  ❌ FALHAS: {failures}")
	print("========================================\n")

	return len(failures) == 0


if __name__ == "__main__":
	testar_calculos()

