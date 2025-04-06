import pdfrw
import os
from datetime import datetime
from config.settings import PLANTILLAS_PDF  # Rutas de plantillas


def generar_pdf(tipo_persona: str, datos: dict, ruta_salida: str = None):
    """
    Genera PDF según tipo de persona (jurídica/natural).
    Args:
        tipo_persona: "juridica" o "natural".
        datos: Diccionario con campos a rellenar.
        ruta_salida: Opcional. Si no se especifica, usa carpeta temporal.
    """
    try:
        # 1. Seleccionar plantilla correcta
        ruta_plantilla = PLANTILLAS_PDF[tipo_persona]
        if not os.path.exists(ruta_plantilla):
            raise FileNotFoundError(f"Plantilla no encontrada: {ruta_plantilla}")

        # 2. Mapeo de campos (personaliza según tus plantillas)
        mapeo_campos = {
            "juridica": {
                "razon_social": "CLIENTE",
                "ruc": "RUCCLIENTE",
                # ... (completa con los campos de tu plantilla)
            },
            "natural": {
                "nombre": "CONTACTO",
                "dni": "DNICONTACTO",
                # ...
            }
        }

        # 3. Rellenar PDF
        plantilla = pdfrw.PdfReader(ruta_plantilla)
        for pagina in plantilla.pages:
            if not hasattr(pagina, 'Annots'):
                continue
            for campo in pagina.Annots:
                if campo['/T']:
                    nombre_pdf = campo['/T'][1:-1]  # Elimina paréntesis
                    for clave, valor in datos.items():
                        if nombre_pdf in mapeo_campos[tipo_persona].get(clave, ""):
                            campo.update(pdfrw.PdfDict(V=str(valor)))

        # 4. Guardar
        if not ruta_salida:
            ruta_salida = f"temp/Cotizacion_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

        os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)
        pdfrw.PdfWriter().write(ruta_salida, plantilla)
        return ruta_salida

    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        return None