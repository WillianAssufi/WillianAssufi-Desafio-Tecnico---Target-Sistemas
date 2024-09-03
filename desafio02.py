def fibonacci(n):
    a, b = 0, 1

    while a < n:
        a, b = b, a + b
    return a == n
    
def main():
    while True:
        try:
            num = int(input("\nDigite 0 para encerrar o programa ou\nInforme um número para verificar: "))
            if num > 0:
                if fibonacci(num):
                    print(f"{num} é um número de Fibonacci.")
                else:
                    print(f"{num} não é um número de Fibonacci.")
            else:
                print("Digite um número inteiro positivo.")
            if num == 0:
                print("Programa encerrado.")
                exit()
        except ValueError:
            print("Digite um número válido.")

if __name__ == "__main__":
    main()