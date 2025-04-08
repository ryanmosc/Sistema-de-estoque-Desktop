import tkinter as tk
from auth.login import verificar_login
from views.registro_view import tela_registro  # importa a tela de cadastro

def exibir_tela_login(janela):
    for widget in janela.winfo_children():
        widget.destroy()

    tk.Label(janela, text="Usuário").pack(pady=5)
    entrada_usuario = tk.Entry(janela)
    entrada_usuario.pack()

    tk.Label(janela, text="Senha").pack(pady=5)
    entrada_senha = tk.Entry(janela, show="*")
    entrada_senha.pack()

    tk.Button(janela, text="Entrar", command=lambda: verificar_login(
        entrada_usuario.get(),
        entrada_senha.get()
    )).pack(pady=10)

    # ✅ Botão para tela de cadastro
    tk.Button(janela, text="Cadastre-se", command=lambda: tela_registro(janela)).pack()
