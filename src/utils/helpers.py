import flet as ft

def mostrar_mensaje(page: ft.Page, texto: str, es_error: bool = False):
    """Muestra un snackbar en la página."""
    page.snack_bar = ft.SnackBar(
        content=ft.Text(texto, color=ft.colors.RED if es_error else ft.colors.GREEN),
        bgcolor="#1E1E1E"
    )
    page.snack_bar.open = True
    page.update()