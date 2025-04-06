import flet as ft

class PersonaJuridica(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.visible = False
        self.expand = True

        # Campos
        self.campos = {
            'ruc': ft.TextField(label="RUC", width=300, read_only=True),
            'razon_social': ft.TextField(label="Razón Social", width=400),
            'direccion': ft.TextField(label="Dirección Fiscal", width=500, multiline=True)
        }

        self.controls = [
            ft.Text("Datos Jurídicos", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([self.campos['ruc'], self.campos['razon_social']]),
            ft.Row([self.campos['direccion']])
        ]

    def cargar_datos_vacios(self):
        """Prepara campos vacíos para nuevo registro"""
        for campo in self.campos.values():
            campo.value = ""