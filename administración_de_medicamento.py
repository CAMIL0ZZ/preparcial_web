from enum import Enum

class ViaAdministracion(str, Enum):
    ENTERALES = "enterales"
    PARENTERALES = "parenterales"
    TOPICAS = "tópicas"
    RESPIRATORIAS = "respiratorias"