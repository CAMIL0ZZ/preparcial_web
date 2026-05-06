from typing import Optional
from sqlmodel import SQLModel, Field
from administración_de_medicamento import ViaAdministracion

class Farmaco(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    laboratorio: str
    costo: float
    via_administracion: ViaAdministracion
    activo: bool = Field(default=True)  # Estrategia: Borrado lógico

class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    correo: str
    id_farmaco: Optional[int] = Field(default=None, foreign_key="farmaco.id")
    activo: bool = Field(default=True)