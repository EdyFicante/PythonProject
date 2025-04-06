from datetime import datetime, timedelta

def calcular_vencimiento(fecha_str: str, dias: int) -> str:
    """Calcula fecha de vencimiento (dd/mm/YYYY) a partir de una fecha base."""
    try:
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        return (fecha + timedelta(days=dias)).strftime("%d/%m/%Y")
    except ValueError:
        return ""