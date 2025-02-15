import tkinter as tk

# Função para realizar a operação
def calcular():
    try:
        resultado = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(resultado))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Função para adicionar um número ou operador à entrada
def adicionar(valor):
    entry.insert(tk.END, valor)

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("400x600")  # Tamanho da janela
janela.configure(bg="#f0f0f0")  # Cor de fundo

# Criando a entrada de texto
entry = tk.Entry(janela, width=16, font=('Arial', 32), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Criando os botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Adicionando os botões à interface
linha = 1
coluna = 0
for botao in botoes:
    # Estilo dos botões
    b = tk.Button(janela, text=botao, width=5, height=2, font=('Arial', 24), bg="#ffffff", fg="#000000", 
                  activebackground="#e0e0e0", command=lambda b=botao: adicionar(b))
    b.grid(row=linha, column=coluna, padx=5, pady=5)

    if botao == '=':
        b.config(command=calcular)  # Muda a função do botão '='

    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Estilizando o botão de igual
igual_button = tk.Button(janela, text='=', width=5, height=2, font=('Arial', 24), bg="#4CAF50", fg="#ffffff", 
                         activebackground="#45a049", command=calcular)
igual_button.grid(row=linha, column=3, padx=5, pady=5)

# Iniciando o loop da interface
janela.mainloop()