import flet as ft
from datetime import datetime, timedelta
import random

class FormularioProforma(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.visible = False

        # Campos
        self.campos = {
            'numero': ft.TextField(label="N° Proforma", value=f"PROF-{random.randint(1000, 9999)}", width=150),
            'fecha': ft.TextField(label="Fecha", value=datetime.now().strftime("%d/%m/%Y"), width=150),
            'dias_validez': ft.TextField(label="Días Validez", width=150, on_change=self._calcular_vencimiento),
            'fecha_vencimiento': ft.TextField(label="Vencimiento", read_only=True, width=150)
        }

        self.controls = [
            ft.Text("Detalles de Proforma", size=18, weight=ft.FontWeight.BOLD),
            ft.Row([self.campos['numero'], self.campos['fecha']]),
            ft.Row([self.campos['dias_validez'], self.campos['fecha_vencimiento']])
        ]

    def _calcular_vencimiento(self, e):
        if self.campos['dias_validez'].value.isdigit():
            dias = int(self.campos['dias_validez'].value)
            fecha = datetime.strptime(self.campos['fecha'].value, "%d/%m/%Y")
            self.campos['fecha_vencimiento'].value = (fecha + timedelta(days=dias)).strftime("%d/%m/%Y")
            self.page.update()

    def limpiar_formulario(self):
        self.campos['dias_validez'].value = ""
        self.campos['fecha_vencimiento'].value = ""