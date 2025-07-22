# __init__.py
# Archivo de inicialización del paquete models
# Definición de modelos de datos y esquemas Pydantic

# Importar modelos de base de datos
from .database_models import Company, JobOffer, User

# Importar esquemas Pydantic principales
from .job_models import (
    # Enums
    JobStatus, ApplicationStatus, ScrapingStatus, UserRole,
    
    # Esquemas de Usuario
    UserCreate, UserUpdate, UserResponse, UserProfile,
    
    # Esquemas de Empresa
    CompanyCreate, CompanyUpdate, CompanyResponse,
    
    # Esquemas de Oferta Laboral
    JobOfferCreate, JobOfferUpdate, JobOfferResponse, JobOfferList,
    
    # Esquemas de Scraping
    ScrapingSourceCreate, ScrapingSourceUpdate, ScrapingSourceResponse,
    ScrapingJobCreate, ScrapingJobResponse,
    
    # Esquemas de Historial
    UserJobInteractionCreate, UserJobInteractionResponse,
    SearchHistoryCreate, SearchHistoryResponse,
    
    # Esquemas de Búsqueda y Filtros
    JobSearchFilters, PaginationParams,
    
    # Esquemas de Autenticación
    Token, TokenData, LoginRequest, PasswordReset, PasswordResetConfirm
)

__all__ = [
    # Modelos ORM
    "Company", "JobOffer", "User",
    
    # Enums
    "JobStatus", "ApplicationStatus", "ScrapingStatus", "UserRole",
    
    # Esquemas Pydantic
    "UserCreate", "UserUpdate", "UserResponse", "UserProfile",
    "CompanyCreate", "CompanyUpdate", "CompanyResponse",
    "JobOfferCreate", "JobOfferUpdate", "JobOfferResponse", "JobOfferList",
    "ScrapingSourceCreate", "ScrapingSourceUpdate", "ScrapingSourceResponse",
    "ScrapingJobCreate", "ScrapingJobResponse",
    "UserJobInteractionCreate", "UserJobInteractionResponse",
    "SearchHistoryCreate", "SearchHistoryResponse",
    "JobSearchFilters", "PaginationParams",
    "Token", "TokenData", "LoginRequest", "PasswordReset", "PasswordResetConfirm"
]