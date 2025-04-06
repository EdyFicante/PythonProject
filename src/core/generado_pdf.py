from pathlib import Path
import os


class GeneradorPDF:
    def __init__(self, page: ft.Page):
        self.page = page
        # Rutas ABSOLUTAS (para evitar errores de malditos paths relativos)
        self.base_dir = Path("C:/Users/Gw/PycharmProjects/PythonProject/.venv")

        # Plantillas y salida
        self.plantillas = {
            "juridica": self.base_dir / "Plantilla_pJuridica.pdf",
            "natural": self.base_dir / "Plantilla_pNatural.pdf"
        }
        self.salida_pdf = self.base_dir / "Cotizacion_Generada.pdf"

    def generar(self, datos: dict, tipo_persona: str):
        """Genera el PDF en .venv/ con nombre FIJO"""
        try:
            # 1. Validar plantilla
            if not os.path.exists(self.plantillas[tipo_persona]):
                raise FileNotFoundError(f"¡Plantilla {tipo_persona} no encontrada en: {self.plantillas[tipo_persona]}")

            # 2. Generar PDF (tu código con pdfrw)
            # ... (usar self.plantillas[tipo_persona] y self.salida_pdf)

            # 3. Abrir automáticamente el PDF generado
            os.startfile(self.salida_pdf)

        except Exception as e:
            print(f"ERROR: {str(e)}")  # Para que no digas que no te avisé