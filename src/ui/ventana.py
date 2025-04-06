import flet as ft

def configurar_ventana(page: ft.Page):
    page.title = "GRANLER - Alquiler de Herramientas"
    page.window_width = 700
    page.window_height = 1200
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#121212"
    page.update()