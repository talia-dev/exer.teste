def inverter_string(texto):
  texto_invertido = ""
  for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

string_usuario = input("Digite uma string: ")
string_invertida_usuario = inverter_string(string_usuario)
print(f"String invertida: {string_invertida_usuario}")