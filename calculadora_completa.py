### calculadora.py (versão base com menu interativo)
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

def mostrar_menu():
    print("===== Calculadora Simples =====")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '5':
        print("Encerrando a calculadora.")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        continue

    if opcao == '1':
        print(f"Resultado: {somar(num1, num2)}")
    elif opcao == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif opcao == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcao == '4':
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Opção inválida. Tente novamente.")

    print()  # Linha em branco


### calculadora_gui.py (com interface Tkinter)
import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        a = float(entrada1.get())
        b = float(entrada2.get())
        operacao = operacao_var.get()

        if operacao == 'Somar':
            resultado = a + b
        elif operacao == 'Subtrair':
            resultado = a - b
        elif operacao == 'Multiplicar':
            resultado = a * b
        elif operacao == 'Dividir':
            if b == 0:
                raise ZeroDivisionError
            resultado = a / b
        else:
            resultado = 'Selecione uma operação.'

        resultado_label.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não permitida.")

janela = tk.Tk()
janela.title("Calculadora Tkinter")

entrada1 = tk.Entry(janela)
entrada1.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

operacao_var = tk.StringVar()
operacao_menu = tk.OptionMenu(janela, operacao_var, 'Somar', 'Subtrair', 'Multiplicar', 'Dividir')
operacao_menu.pack()

botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack()

resultado_label = tk.Label(janela, text="Resultado: ")
resultado_label.pack()

janela.mainloop()


### calculadora_argparse.py (com argumentos via terminal)
import argparse

def main():
    parser = argparse.ArgumentParser(description="Calculadora simples via terminal.")
    parser.add_argument("num1", type=float, help="Primeiro número")
    parser.add_argument("operador", choices=['+', '-', '*', '/'], help="Operação desejada")
    parser.add_argument("num2", type=float, help="Segundo número")

    args = parser.parse_args()

    if args.operador == '+':
        resultado = args.num1 + args.num2
    elif args.operador == '-':
        resultado = args.num1 - args.num2
    elif args.operador == '*':
        resultado = args.num1 * args.num2
    elif args.operador == '/':
        if args.num2 == 0:
            resultado = "Erro: divisão por zero."
        else:
            resultado = args.num1 / args.num2

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()


### README.md (explicativo)
# Calculadora em Python

Este repositório contém três versões de uma calculadora simples em Python:

- `calculadora.py`: Interativa via terminal
- `calculadora_gui.py`: Interface gráfica usando Tkinter
- `calculadora_argparse.py`: Uso via linha de comando com argumentos

## Como usar

### 1. Versão Interativa
```bash
python calculadora.py
```

### 2. Versão com Interface Gráfica
```bash
python calculadora_gui.py
```

### 3. Versão com Argumentos
```bash
python calculadora_argparse.py 10 + 5
Resultado: 15.0
```

---

Sinta-se à vontade para clonar e adaptar! 🚀
