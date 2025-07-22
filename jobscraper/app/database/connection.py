# connection.py
# Configuración de la conexión a la base de datos
# Setup de SQLAlchemy engine, session y configuración de la BD

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from typing import Generator

# URL de conexión a PostgreSQL desde variable de entorno
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://usuario:password@localhost:5432/jobscraper"
)

# Crear engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Verificar conexiones antes de usar
    pool_recycle=300,    # Reciclar conexiones cada 5 minutos
    echo=False           # Cambiar a True para debug SQL
)

# Configurar sesión de base de datos
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos ORM
Base = declarative_base()

def get_db() -> Generator:
    """
    Generador de sesiones de base de datos para dependency injection en FastAPI.
    Asegura que la sesión se cierre correctamente después de cada request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    Crear todas las tablas definidas en los modelos.
    Usar solo en desarrollo o para inicialización.
    """
    Base.metadata.create_all(bind=engine)

def drop_tables():
    """
    Eliminar todas las tablas.
    Usar con precaución, solo en desarrollo.
    """
    Base.metadata.drop_all(bind=engine)