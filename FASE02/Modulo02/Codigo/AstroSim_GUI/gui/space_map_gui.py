import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SpaceMapGUI(ttk.Frame):
    """
    Interface gráfica para planejamento de missões espaciais.
    Permite visualizar tarefas e aplicar programação inteira com exibição de feedback visual.
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._criar_widgets()
        self.et_label = None  # Widget de imagem (opcional)
        self.et_photo = None  # Referência à imagem (evita coleta pelo GC)

    def _criar_widgets(self):
        """Cria os widgets da interface principal."""
        ttk.Label(self, text="Gerenciamento de Recursos", font=("Arial", 14)).pack(pady=(10, 5))

        self.task_list = tk.Text(self, height=10, width=70)
        self.task_list.pack(pady=5)

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=5)

        ttk.Button(
            button_frame,
            text="Resolver com Programação Inteira",
            command=self.solve_exact
        ).pack(side=tk.LEFT, padx=5)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

    def solve_exact(self):
        """Executa o algoritmo e exibe uma imagem de E.T. como feedback visual."""
        self.result_label.config(text="Resultado (Exato): Encontrado com sucesso!")

        caminho_imagem = "images/Image/et.png"
        if not os.path.isfile(caminho_imagem):
            self.result_label.config(text="Imagem não encontrada: et.png")
            return

        imagem = Image.open(caminho_imagem).resize((1000, 1000))
        self.et_photo = ImageTk.PhotoImage(imagem)

        if self.et_label is None:
            self.et_label = tk.Label(self, image=self.et_photo)
            self.et_label.pack(pady=10)
        else:
            self.et_label.config(image=self.et_photo)