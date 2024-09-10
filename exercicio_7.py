def calcular_soma_quadrados(vetor):
    vetor_calculado = []
    soma = 0

    for num in vetor:
        vetor_calculado.append(int(num)**2)
    
    return sum(vetor_calculado)

def main():
    vetor_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Soma do quadrado do vetor {vetor_A} é: {calcular_soma_quadrados(vetor_A)}")

main()