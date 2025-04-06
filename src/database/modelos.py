from pydantic import BaseModel

class ClienteBase(BaseModel):
    ruc: str
    razon_social: str
    direccion_fiscal: str
    telefono: str

class ClienteCreate(ClienteBase):
    email: str | None = None
    gerente_general: str | None = None
    email_gerente: str | None = None
    dni_gerente: str | None = None

# [...] (otros modelos)