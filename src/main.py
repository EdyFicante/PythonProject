import flet as ft
from ui.componentes.radio_opciones import RadioOpciones


def main(page: ft.Page):
    # Configuración básica
    page.title = "GRANLER - Sistema de Proformas"
    page.window_width = 700
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK

    # Carga la vista inicial
    vista_inicial = RadioOpciones(page)
    page.add(vista_inicial)


ft.app(target=main)