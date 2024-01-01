import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from colorama import Fore, Style
import pandas as pd

class App:
    def _init_(self, root):
        self.root = root
        self.root.title("Controle de Estoque")
        
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.criar_tabela()

    def criar_tabela(self):
        # Função para ler dados da planilha Excel
        def ler_planilha_excel(caminho_planilha):
            return pd.read_excel(caminho_planilha)

        # Substitua "caminho/para/sua/planilha.xlsx" pelo caminho real para sua planilha Excel
        caminho_planilha = "caminho/para/sua/planilha.xlsx"
        dados_exemplo = ler_planilha_excel(caminho_planilha)

        # Atualiza dias até o vencimento e destaca em vermelho se estiver próximo
        dados_exemplo["Dias até Vencimento"] = (dados_exemplo["Vencimento"] - datetime.now()).dt.days
        dados_exemplo["Estilo"] = ["Red.TLabel" if dias <= 7 else "" for dias in dados_exemplo["Dias até Vencimento"]]

        # Criação da tabela
        self.tree = ttk.Treeview(self.frame, columns=("Prateleira / Andar", "Produto", "Vencimento", "Dias até Vencimento", "Responsável", "Data Chegada", "Responsável Entrada"), show="headings")
        self.tree.heading("#0", text="Prateleira / Andar", anchor=tk.W)
        self.tree.heading("#1", text="Produto", anchor=tk.W)
        self.tree.heading("#2", text="Vencimento", anchor=tk.W)
        self.tree.heading("#3", text="Dias até Vencimento", anchor=tk.W)
        self.tree.heading("#4", text="Responsável", anchor=tk.W)
        self.tree.heading("#5", text="Data Chegada", anchor=tk.W)
        self.tree.heading("#6", text="Responsável Entrada", anchor=tk.W)
        self.tree.grid(row=0, column=0, columnspan=7, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Adiciona dados à tabela
        for index, row in dados_exemplo.iterrows():
            self.tree.insert("", tk.END, values=(row["Prateleira / Andar"], row["Produto"], row["Vencimento"].strftime('%d/%m/%Y'), row["Dias até Vencimento"], row["Responsável"], row["Data Chegada"].strftime('%d/%m/%Y'), row["Responsável Entrada"]), tags=(row["Estilo"]))

        # Adiciona uma linha em branco entre andares
        for _ in range(4):
            self.tree.insert("", tk.END, values=("", "", "", "", "", "", ""))

        # Lista produtos próximos ao vencimento
        print("Produtos Próximos ao Vencimento:")
        for index, row in dados_exemplo[dados_exemplo["Dias até Vencimento"] <= 7].iterrows():
            print(f"Produto: {row['Produto']} | Vencimento: {row['Vencimento'].strftime('%d/%m/%Y')} | Responsável: {row['Responsável']} | Dias até Vencimento: {row['Dias até Vencimento']}")

if _name_ == "_main_":
    root = tk.Tk()
    app = App(root)
    root.mainloop()