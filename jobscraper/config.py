# config.py
# Configuración global del proyecto
# Variables de entorno globales, configuración de base de datos, APIs externas, etc.
# Este archivo centraliza toda la configuración del proyecto

from jobscraper.app.core.config import settings

# Re-exportar settings para fácil acceso desde la raíz
__all__ = ["settings"]