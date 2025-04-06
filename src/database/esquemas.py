from pydantic import BaseModel, EmailStr

class PersonaJuridicaSchema(BaseModel):
    ruc: str
    razon_social: str
    direccion_fiscal: str
    telefono: str
    email: EmailStr | None = None
    gerente_general: str | None = None
    email_gerente: EmailStr | None = None
    dni_gerente: str | None = None

class PersonaNaturalSchema(BaseModel):
    dni: str
    nombre: str
    cargo: str | None = None
    telefono: str
    email: EmailStr | None = None