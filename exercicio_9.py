def fibonacci_sequence(n):
    fibonacci = []
    for i in range(0, n):
        if i == 0 or i == 1:
            fibonacci.append(i)
        else:
            fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci

def obter_numero(message = "Digite um número: "):
    while True:
        try:
            valor = int(input(message))
            return valor
        except:
            print("Digite um valor válido!")

def main():
    n = obter_numero("Digite a quantidade de números para fibonacci: ")
    print(f"A sequência de Fibonacci com {n} termos é: {fibonacci_sequence(n)}")

main()