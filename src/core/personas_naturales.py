import flet as ft

class PersonaNatural(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.visible = False
        self.expand = True

        # Campos
        self.campos = {
            'dni': ft.TextField(label="DNI", width=300),
            'nombre': ft.TextField(label="Nombre Completo", width=400),
            'telefono': ft.TextField(label="Teléfono", width=200)
        }

        self.controls = [
            ft.Text("Datos de Contacto", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([self.campos['dni'], self.campos['nombre']]),
            ft.Row([self.campos['telefono']])
        ]

    def cargar_datos_vacios(self):
        """Prepara campos vacíos"""
        for campo in self.campos.values():
            campo.value = ""