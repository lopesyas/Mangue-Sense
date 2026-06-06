
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
	"""Roda testes simples (9 casos) e imprime resultado.
	Retorna True se todos passarem, caso contrário False.
	"""
	failures = []

	# ΔT tests
	r = calcular_diferencial_termico(65, 30)
	if not (r["valido"] and r["valor"] == 35 and r["status"] == "ALERTA"):
		failures.append("dt_alerta")

	r = calcular_diferencial_termico(40, 20)
	if not (r["valido"] and r["valor"] == 20 and r["status"] == "OK"):
		failures.append("dt_ok")

	r = calcular_diferencial_termico(120, 60)
	if not (r["valido"] and r["status"] == "CRÍTICO"):
		failures.append("dt_critico")

	# Score tests
	s = calcular_score_geracao(800, 1000)
	if not (s["valido"] and round(s["valor"]) == 80 and s["status"] == "ALERTA"):
		failures.append("score_alerta")

	s = calcular_score_geracao(900, 1000)
	if not (s["valido"] and s["status"] == "OK"):
		failures.append("score_ok")

	s = calcular_score_geracao(200, 1000)
	if not (s["valido"] and s["status"] == "CRÍTICO"):
		failures.append("score_critico")

	# Risco tests
	if classificar_risco_usina("ALERTA", "OK") != "ALERTA":
		failures.append("risco_alerta")
	if classificar_risco_usina("OK", "CRÍTICO") != "CRÍTICO":
		failures.append("risco_critico")
	if classificar_risco_usina("OK", "OK") != "OK":
		failures.append("risco_ok")

	if failures:
		print("TESTES FALHARAM:", failures)
		return False
	print("TODOS OS TESTES PASSARAM")
	return True


if __name__ == "__main__":
	testar_calculos()

