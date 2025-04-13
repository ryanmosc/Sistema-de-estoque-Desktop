import tkinter as tk
from tkinter import messagebox
from home.home import abrir_tela_estoque, abrir_tela_funcionarios,abrir_tela_saidas,abrir_tela_metricas
from estoque.views_estoque.ler_view import exibir_tela_pesquisa

def criar_tela_inicial():
    janela = tk.Tk()
    janela.title("Sistema de Estoque")
    janela.geometry("900x600")
    janela.configure(bg="#f5f5f5")
    
    
    topbar = tk.Frame(janela, bg="#2c3e50", height=50)
    topbar.pack(side="top", fill="x")
    
    def sair():
        if messagebox.askokcancel("Sair", "Deseja realmente sair?"):
            janela.destroy()

    
    botoes = {
        "Início": lambda: print("Início"),
       "Estoque": lambda: exibir_tela_pesquisa(janela),
        "Funcionários":lambda:abrir_tela_funcionarios(janela),
        "Saídas": lambda: abrir_tela_saidas(janela),
        "Métricas": lambda: abrir_tela_metricas(janela),
        "Sair": lambda:sair()
    }
    

    for texto, comando in botoes.items():
        btn = tk.Button(
            topbar,
            text=texto,
            fg="white",
            bg="#34495e",
            activebackground="#1abc9c",
            relief="flat",
            font=("Arial", 12),
            padx=15,
            pady=10,
            command=comando  
        )
        btn.pack(side="left", padx=5, pady=5)

    area_principal = tk.Frame(janela, bg="#ecf0f1")
    area_principal.pack(expand=True, fill="both")

    label_mensagem = tk.Label(
        area_principal,
        text="👋 Bem-vindo ao Sistema de Estoque!",
        font=("Arial", 20),
        bg="#ecf0f1",
        fg="#2c3e50"
    )
    label_mensagem.pack(expand=True)

    janela.mainloop()


#Comando utilizado para burlar o login, apos terminar favor excluir ou comentar
# criar_tela_inicial()
