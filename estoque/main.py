import tkinter as tk
from views.login_view import exibir_tela_login

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Sistema de Estoque - Login")
    app.geometry("300x200")
    exibir_tela_login(app)
    app.mainloop()
