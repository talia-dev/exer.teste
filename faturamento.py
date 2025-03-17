import json

dados_faturamento = """
[
  {"dia": 1, "valor": 22174.1664},
  {"dia": 2, "valor": 24537.6698},
  {"dia": 3, "valor": 26139.6134},
  {"dia": 4, "valor": 0.0},
  {"dia": 5, "valor": 0.0},
  {"dia": 6, "valor": 26742.6612},
  {"dia": 7, "valor": 0.0},
  {"dia": 8, "valor": 42889.2258},
  {"dia": 9, "valor": 46251.174},
  {"dia": 10, "valor": 11191.4714},
  {"dia": 11, "valor": 0.0},
  {"dia": 12, "valor": 0.0},
  {"dia": 13, "valor": 3847.4823},
  {"dia": 14, "valor": 373.7838},
  {"dia": 15, "valor": 2659.7563},
  {"dia": 16, "valor": 48924.2448},
  {"dia": 17, "valor": 18419.2614},
  {"dia": 18, "valor": 0.0},
  {"dia": 19, "valor": 0.0},
  {"dia": 20, "valor": 35240.1826},
  {"dia": 21, "valor": 43829.1667},
  {"dia": 22, "valor": 18235.6852},
  {"dia": 23, "valor": 43529.1667},
  {"dia": 24, "valor": 13327.1122},
  {"dia": 25, "valor": 0.0},
  {"dia": 26, "valor": 0.0},
  {"dia": 27, "valor": 25681.8318},
  {"dia": 28, "valor": 1718.1221},
  {"dia": 29, "valor": 1322.0088},
  {"dia": 30, "valor": 8414.61}
]
"""

faturamento = json.loads(dados_faturamento)

valores_faturamento = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)
media_mensal = sum(valores_faturamento) / len(valores_faturamento)
dias_acima_media = len([valor for valor in valores_faturamento if valor > media_mensal])

print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_media}")