# Consultas para Personas Jurídicas
BUSCAR_CLIENTE = """
    SELECT id, ruc_cliente, razon_social, direccion_fiscal, 
           telefono, email, gerente_general, email_gerente, dni_gerente 
    FROM clientes_granler 
    WHERE ruc_cliente = %s 
    LIMIT 1
"""

ACTUALIZAR_CLIENTE = """
    UPDATE clientes_granler SET
        razon_social = %s,
        direccion_fiscal = %s,
        telefono = %s,
        email = %s,
        gerente_general = %s,
        email_gerente = %s,
        dni_gerente = %s
    WHERE ruc_cliente = %s
"""

# [...] (todas las demás consultas SQL)