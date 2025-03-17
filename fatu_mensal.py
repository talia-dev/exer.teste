faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento_estados.values())

percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}%")