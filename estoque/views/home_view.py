import tkinter as tk

def criar_tela_inicial():
    janela = tk.Tk()
    janela.title("Sistema de Estoque")
    janela.geometry("900x600")
    janela.configure(bg="#f5f5f5")  # Fundo claro

    # Sidebar
    sidebar = tk.Frame(janela, bg="#2c3e50", width=200)
    sidebar.pack(side="left", fill="y")

    botoes = [
        "Início",
        "Estoque",
        "Funcionários",
        "Saídas",
        "Métricas",
        "Sair"
    ]

    for texto in botoes:
        btn = tk.Button(
            sidebar,
            text=texto,
            fg="white",
            bg="#34495e",
            activebackground="#1abc9c",
            relief="flat",
            font=("Arial", 12),
            padx=10,
            pady=10
        )
        btn.pack(fill="x", padx=5, pady=5)

    # Área principal
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


