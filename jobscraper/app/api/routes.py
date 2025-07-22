# routes.py
# Definición de rutas y endpoints de la API
# Aquí se configurarán los endpoints para gestionar ofertas laborales
# PREPARADO: Router principal que incluirá todos los endpoints

from fastapi import APIRouter

# Crear router principal
router = APIRouter()

@router.get("/")
async def api_root():
    """
    Endpoint raíz de la API v1.
    """
    return {
        "message": "JobScraper API v1",
        "status": "active",
        "endpoints": {
            "auth": "/auth",
            "users": "/users", 
            "companies": "/companies",
            "jobs": "/jobs",
            "scraping": "/scraping",
            "stats": "/stats"
        }
    }

# TODO: Implementar routers específicos para:
# - /auth (autenticación y registro)
# - /users (gestión de usuarios)
# - /companies (gestión de empresas)
# - /jobs (gestión de ofertas laborales)
# - /scraping (gestión de scraping)
# - /stats (estadísticas y analytics)