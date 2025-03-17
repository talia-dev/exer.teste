def fibonacci(numero):
    fib = [0, 1]
    while fib[-1] <= numero:
        fib.append(fib[-1] + fib[-2])
    if numero in fib:
        print(f'O número {numero} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {numero} não pertence à sequência de Fibonacci.')

try:
    numero_usuario = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    fibonacci(numero_usuario)
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")