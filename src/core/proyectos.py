import flet as ft

class FormularioProyecto(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.visible = False

        # Campos
        self.campos = {
            'nombre': ft.TextField(label="Nombre Proyecto", width=400),
            'direccion': ft.TextField(label="Dirección", width=500, multiline=True)
        }

        self.controls = [
            ft.Text("Datos del Proyecto", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([self.campos['nombre']]),
            ft.Row([self.campos['direccion']])
        ]

    def limpiar_formulario(self):
        for campo in self.campos.values():
            campo.value = ""