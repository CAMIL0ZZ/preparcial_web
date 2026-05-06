import os
from dotenv import load_dotenv
from sqlmodel import Session, create_engine, select
from model import Farmaco, Cliente
from model import Cliente, Farmaco

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

def create_db_and_tables():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)


# --- operaciones en db para farmaco ---

async def add_farmaco(farmaco: Farmaco):
    with Session(engine) as session:
        session.add(farmaco)
        session.commit()
        session.refresh(farmaco)
        return farmaco

async def get_all_farmacos():
    with Session(engine) as session:
        # Ya no filtramos por "activo", traemos lo que exista
        return session.exec(select(Farmaco)).all()

async def get_farmaco_by_id(f_id: int):
    with Session(engine) as session:
        return session.get(Farmaco, f_id)

async def update_farmaco(f_id: int, data: dict):
    with Session(engine) as session:
        db_farmaco = session.get(Farmaco, f_id)
        if not db_farmaco: return None
        for key, value in data.items():
            setattr(db_farmaco, key, value)
        session.add(db_farmaco)
        session.commit()
        session.refresh(db_farmaco)
        return db_farmaco


async def delete_farmaco_definitivo(f_id: int):

    with Session(engine) as session:
        db_farmaco = session.get(Farmaco, f_id)
        if not db_farmaco:
            return False
        session.delete(db_farmaco)
        session.commit()
        return True


# --- operaciones en db para cliente ---


async def add_cliente(cliente: Cliente):
    with Session(engine) as session:
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        return cliente


async def get_all_clientes():
    with Session(engine) as session:
        return session.exec(select(Cliente)).all()


async def get_cliente_by_id(c_id: int):
    with Session(engine) as session:
        cliente = session.get(Cliente, c_id)
        return cliente


async def update_cliente(c_id: int, data: dict):
    with Session(engine) as session:
        db_cliente = session.get(Cliente, c_id)
        if not db_cliente:
            return None


        for key, value in data.items():
            setattr(db_cliente, key, value)

        session.add(db_cliente)
        session.commit()
        session.refresh(db_cliente)
        return db_cliente


async def delete_cliente_definitivo(c_id: int):
    with Session(engine) as session:
        db_cliente = session.get(Cliente, c_id)
        if not db_cliente:
            return False
        session.delete(db_cliente)
        session.commit()
        return True


