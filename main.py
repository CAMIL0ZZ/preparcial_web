from fastapi import FastAPI, HTTPException, status
from typing import List
from model import Farmaco, Cliente
import operations_DB as db

app = FastAPI(
    title="Sistema de Gestión de Farmacia (API)",
    description="CRUD para fármacos y clientes conectado a servidor Neon"
)


@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()



@app.post("/farmacos/", response_model=Farmaco, status_code=status.HTTP_201_CREATED)
async def create_farmaco(farmaco: Farmaco):
    """inserta farmaco"""
    return await db.add_farmaco(farmaco)

@app.get("/farmacos/", response_model=List[Farmaco])
async def read_all_farmacos():
    """Recupera los registros completos de la tabla farmacos"""
    return await db.get_all_farmacos()

@app.get("/farmacos/{f_id}", response_model=Farmaco)
async def read_farmaco(f_id: int):
    """Encuentra y responde con un registro al consultar x id"""
    farmaco = await db.get_farmaco_by_id(f_id)
    if not farmaco:
        raise HTTPException(status_code=404, detail="Fármaco no encontrado")
    return farmaco

@app.patch("/farmacos/{f_id}", response_model=Farmaco)
async def update_farmaco(f_id: int, farmaco_data: dict):
    """Permite modificar farmaco"""
    updated = await db.update_farmaco(f_id, farmaco_data)
    if not updated:
        raise HTTPException(status_code=404, detail="No se pudo actualizar: Fármaco no existe")
    return updated

@app.delete("/farmacos/{f_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_farmaco(f_id: int):
    """Elimina un fármaco desde /docs"""
    success = await db.delete_farmaco_definitivo(f_id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar: Fármaco no existe")
    return None


# --- ENDPOINTS PARA CLIENTES ---

@app.post("/clientes/", response_model=Cliente, status_code=status.HTTP_201_CREATED)
async def create_cliente(cliente: Cliente):
    """Inserta cliente en la tabla"""
    return await db.add_cliente(cliente)

@app.get("/clientes/", response_model=List[Cliente])
async def read_all_clientes():
    """Recupera registros completos de clientes"""
    return await db.get_all_clientes()

@app.get("/clientes/{c_id}", response_model=Cliente)
async def read_cliente(c_id: int):
    """Encuentra y responde con un registro al consultar x id"""
    cliente = await db.get_cliente_by_id(c_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@app.patch("/clientes/{c_id}", response_model=Cliente)
async def update_cliente(c_id: int, cliente_data: dict):
    """Permite modificar un cliente"""
    updated = await db.update_cliente(c_id, cliente_data)
    if not updated:
        raise HTTPException(status_code=404, detail="No se pudo actualizar: Cliente no existe")
    return updated

@app.delete("/clientes/{c_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente(c_id: int):
    """Elimina definitivamente un cliente desde /docs"""
    success = await db.delete_cliente_definitivo(c_id)
    if not success:
        raise HTTPException(status_code=404, detail="No se pudo eliminar: Cliente no existe")
    return None