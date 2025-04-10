import tkinter as tk
from tkinter import ttk
from estoque.functions.cadastrar import enviar
from home.home import abrir_tela_estoque

def exibir_formulario_cadastro(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    tk.Label(janela, text="Cadastro de Produto", font=("Arial", 14, "bold")).pack(pady=10)

    form_frame = tk.Frame(janela)
    form_frame.pack(pady=10)

    entradas = {}

    categorias_opcoes = ["ALIMENTO", "LIMPEZA", "HIGIENE", "BEBIDAS", "OUTROS"]

    campos = [
        "Nome do Produto",
        "Categoria",  
        "Estoque",
        "Preço de Custo",
        "Preço de Venda"
    ]

    for idx, campo in enumerate(campos):
        tk.Label(form_frame, text=campo).grid(row=idx, column=0, sticky="e", pady=5, padx=5)

        if campo == "Categoria":
            combobox = ttk.Combobox(form_frame, values=categorias_opcoes, state="readonly")
            combobox.grid(row=idx, column=1, pady=5, padx=5)
            entradas[campo] = combobox
        else:
            entrada = tk.Entry(form_frame)
            entrada.grid(row=idx, column=1, pady=5, padx=5)
            entradas[campo] = entrada

    tk.Button(janela, text="Salvar", command=lambda: enviar(entradas)).pack(pady=15)
    tk.Button(janela, text="Voltar", command=lambda: abrir_tela_estoque(janela)).pack(pady=5)
