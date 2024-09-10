def somar_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    soma = 0
    for num in cpf:
        soma += int(num)
    return soma

def eh_par(num):
    if (num % 2 == 0):
        return "par"
    else:
        return "ímpar"

def solicitar_cpf():
    cpf = input("Digite um CPF (xxx.xxx.xxx-xx): ")
    print(f"CPF: {cpf} ({eh_par(int(cpf.replace('.', '').replace('-', '')))})")
    print(f"Soma dos números: {somar_cpf(cpf)} ({eh_par(somar_cpf(cpf))})")

if __name__ == "__main__":
    solicitar_cpf()