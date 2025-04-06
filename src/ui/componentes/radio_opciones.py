import flet as ft
from core.personas_juridicas import PersonaJuridica
from core.personas_naturales import PersonaNatural
from core.proformas import FormularioProforma
from core.proyectos import FormularioProyecto


class RadioOpciones(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.spacing = 20
        self.alignment = ft.MainAxisAlignment.START
        self.scroll = ft.ScrollMode.AUTO  # Permitir scroll si hay muchos campos

        # --- 1. Controles SUPERIORES (siempre visibles) ---
        self.radio_group = ft.RadioGroup(
            content=ft.Column([
                ft.Radio(value="juridica", label="Persona Jurídica"),
                ft.Radio(value="natural", label="Persona Natural")
            ]),
            on_change=self._mostrar_campo_busqueda
        )

        # --- 2. Campos de búsqueda (inicialmente ocultos) ---
        self.campo_ruc = ft.TextField(
            label="RUC",
            width=300,
            visible=False,
            border_color=ft.colors.BLUE_400
        )

        self.campo_dni = ft.TextField(
            label="DNI",
            width=300,
            visible=False,
            border_color=ft.colors.BLUE_400
        )

        self.btn_buscar = ft.ElevatedButton(
            "BUSCAR",
            icon=ft.icons.SEARCH,
            visible=False,
            on_click=self._mostrar_modulos_completos
        )

        # --- 3. Contenedor para módulos (inicialmente vacío) ---
        self.modulos_container = ft.Column(
            spacing=30,
            visible=False,
            expand=True
        )

        # --- 4. Inicializar módulos (pero no mostrarlos aún) ---
        self.seccion_juridica = PersonaJuridica(page)
        self.seccion_natural = PersonaNatural(page)
        self.seccion_proforma = FormularioProforma(page)
        self.seccion_proyecto = FormularioProyecto(page)

        # --- Estructura PRINCIPAL ---
        self.controls = [
            ft.Text("Tipo de cliente:", size=18, weight=ft.FontWeight.BOLD),
            self.radio_group,
            ft.Divider(height=20),
            ft.Row([self.campo_ruc, self.campo_dni], visible=False),
            self.btn_buscar,
            ft.Divider(height=30, color=ft.colors.RED),
            self.modulos_container  # Aquí irán los módulos cuando se muestren
        ]

    def _mostrar_campo_busqueda(self, e):
        """Paso 1: Solo muestra RUC/DNI + botón BUSCAR"""
        tipo = e.control.value
        self.campo_ruc.visible = (tipo == "juridica")
        self.campo_dni.visible = (tipo == "natural")
        self.btn_buscar.visible = True
        self.modulos_container.visible = False  # Asegura que los módulos estén OCULTOS
        self.modulos_container.controls = []  # Vacía el contenedor
        self.page.update()

    def _mostrar_modulos_completos(self, e):
        """Paso 2: Muestra módulos según tipo de persona en orden vertical"""
        tipo = self.radio_group.value

        # 1. Limpiar contenedor y prepararlo
        self.modulos_container.controls = []

        # 2. Añadir módulos en el orden deseado
        if tipo == "juridica":
            self.seccion_juridica.visible = True
            self.seccion_juridica.campos['ruc'].value = self.campo_ruc.value
            self.modulos_container.controls.append(self.seccion_juridica)
        else:
            self.seccion_natural.visible = True
            self.seccion_natural.campos['dni'].value = self.campo_dni.value
            self.modulos_container.controls.append(self.seccion_natural)

        # Añadir módulos comunes
        self.seccion_proforma.visible = True
        self.seccion_proyecto.visible = True
        self.modulos_container.controls.extend([
            self.seccion_proforma,
            self.seccion_proyecto
        ])

        # 3. Mostrar el contenedor
        self.modulos_container.visible = True
        self.page.update()