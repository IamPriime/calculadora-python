def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido, usando ponto para decimais.")


def calcular(opcao, a, b):
    if opcao == "1":
        return a + b
    if opcao == "2":
        return a - b
    if opcao == "3":
        return a * b
    if opcao == "4":
        if b == 0:
            raise ValueError("Não é possível dividir por zero.")
        return a / b
    raise ValueError("Operação inválida.")


def main():
    while True:
        print("\nCALCULADORA PYTHON\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n0 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "0":
            print("Calculadora encerrada.")
            break
        if escolha not in {"1", "2", "3", "4"}:
            print("Opção inválida.")
            continue
        a = ler_numero("Primeiro número: ")
        b = ler_numero("Segundo número: ")
        try:
            print(f"Resultado: {calcular(escolha, a, b):g}")
        except ValueError as erro:
            print(erro)


if __name__ == "__main__":
    main()
