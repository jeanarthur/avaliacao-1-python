def obter_numero(message = "Digite um número: "):
    while True:
        try:
            valor = float(input(message))
            return valor
        except:
            print("Digite um valor válido!")

def obter_media(vetor):
    return sum(vetor) / len(vetor)

def main():
    notas = []

    for i in range(1, 5):
        notas.append(obter_numero(f"Nota {i}: "))

    media_final = obter_media(notas)
    print(f"Média final: {media_final}")

    if media_final >= 7:
        print("APROVADO")
        return
    
    notas.append(obter_numero(f"Nota Prova Final: "))
    media_final = obter_media(notas)
    print(f"Média final: {media_final}")

    if media_final >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")

main()