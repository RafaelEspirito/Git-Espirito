saida = ''

def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    resultado = None
    op = str(operacao).lower()

    if op == '+' or op == 'adicao':
        resultado = adicao(num1, num2)
    elif op == '-' or op == 'subtracao':
        resultado = subtracao(num1, num2)
    elif op == '*' or op == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif op == '/' or op == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida. Use '+', '-', '*', '/' ou o nome completo."
    
    return resultado

print("🔢 Calculadora Simples")
print("Operações: +, -, *, / ou adicao, subtracao, multiplicacao, divisao.")
print("---")

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao_input = input("Digite a operação: ")

        resultado = calculadora(num1, num2, operacao_input)

        print(f"\nResultado da operação: {resultado}\n")

    except ValueError:
        print("\nErro: Entrada inválida. Digite apenas números válidos.\n")
        
    saida = input("Deseja continuar? (S/N): ")
    print("---")

print("Programa encerrado. Até mais!")