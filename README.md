# JobScraper - Backend de Scraping y Gestión de Ofertas Laborales

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

JobScraper es un backend robusto desarrollado en Python usando FastAPI para el scraping automatizado y gestión inteligente de ofertas laborales. El sistema permite extraer ofertas de trabajo de múltiples sitios web, procesarlas, almacenarlas en una base de datos y proporcionar una API REST completa para su consulta y gestión.

## ✨ Características Principales

- 🚀 **API REST Completa**: Endpoints optimizados para gestionar ofertas laborales
- 🕷️ **Scraping Inteligente**: Extracción automatizada de múltiples sitios web de empleo
- 💾 **Base de Datos Robusta**: Almacenamiento persistente con SQLAlchemy y PostgreSQL
- ✅ **Validación de Datos**: Esquemas Pydantic para validación y serialización
- 🧪 **Testing Completo**: Suite de pruebas unitarias y de integración
- 🔧 **Scripts de Mantenimiento**: Utilidades para migración y administración
- 📊 **Logging Avanzado**: Sistema de logs estructurado para monitoreo
- 🔒 **Configuración Segura**: Gestión de variables de entorno y secretos

## 🏗️ Arquitectura del Proyecto

```
jobscraper/
├── 📁 app/
│   ├── 🌐 api/              # Endpoints y rutas de la API REST
│   ├── 🕷️ scraper/          # Módulos de scraping web
│   ├── 📊 models/           # Modelos de datos y esquemas Pydantic
│   ├── 🗄️ database/         # Configuración y operaciones de BD
│   ├── ⚙️ core/             # Funcionalidades centrales y utilidades
│   └── 🚀 main.py           # Punto de entrada de la aplicación
├── 🧪 tests/               # Pruebas unitarias y de integración
├── 📜 scripts/             # Scripts de mantenimiento y migración
├── ⚙️ config.py            # Configuración global del proyecto
├── 📋 requirements.txt     # Dependencias del proyecto
└── 📖 README.md           # Documentación principal
```

## 🚀 Inicio Rápido

### Prerrequisitos

- Python 3.8 o superior
- PostgreSQL (opcional, se puede usar SQLite para desarrollo)
- Git

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/jobscraper.git
   cd jobscraper
   ```

2. **Crear y activar entorno virtual**
   ```bash
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   ```

5. **Ejecutar migraciones de base de datos**
   ```bash
   python jobmatcher/scripts/migrate_db.py
   ```

## 🎯 Uso

### Ejecutar el servidor de desarrollo

```bash
uvicorn jobscraper.app.main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: `http://localhost:8000`

### Documentación interactiva

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Ejecutar scrapers

```bash
# Ejecutar scraper específico
python jobscraper/scripts/run_scraper.py --site linkedin

# Ejecutar todos los scrapers
python jobscraper/scripts/run_scraper.py --all
```

## 🔧 Configuración

### Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
# Base de datos
DATABASE_URL=postgresql://usuario:password@localhost/jobscraper
# o para desarrollo local
DATABASE_URL=sqlite:///./jobscraper.db

# API Configuration
API_V1_STR=/api/v1
PROJECT_NAME=JobScraper
DEBUG=True

# Scraping Configuration
SCRAPING_DELAY=1
MAX_CONCURRENT_REQUESTS=10
USER_AGENT=JobScraper-Bot/1.0

# Security
SECRET_KEY=tu-clave-secreta-muy-segura
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📡 API Endpoints

### Ofertas Laborales

- `GET /api/v1/jobs` - Listar ofertas con filtros
- `GET /api/v1/jobs/{job_id}` - Obtener detalle de oferta
- `POST /api/v1/jobs` - Crear nueva oferta
- `PUT /api/v1/jobs/{job_id}` - Actualizar oferta
- `DELETE /api/v1/jobs/{job_id}` - Eliminar oferta

### Empresas

- `GET /api/v1/companies` - Listar empresas
- `GET /api/v1/companies/{company_id}` - Detalle de empresa

### Scraping

- `POST /api/v1/scrape/start` - Iniciar proceso de scraping
- `GET /api/v1/scrape/status` - Estado del scraping
- `GET /api/v1/scrape/stats` - Estadísticas de scraping

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con cobertura
pytest --cov=jobscraper

# Ejecutar pruebas específicas
pytest jobscraper/tests/test_api.py
```

## 🛠️ Scripts de Mantenimiento

```bash
# Migrar base de datos
python jobscraper/scripts/migrate_db.py

# Ejecutar scraping programado
python jobscraper/scripts/run_scraper.py

# Limpiar datos duplicados
python jobmatcher/scripts/clean_duplicates.py
```

## 📊 Monitoreo y Logs

Los logs se almacenan en la carpeta `logs/` con rotación automática:

- `logs/app.log` - Logs generales de la aplicación
- `logs/scraper.log` - Logs específicos de scraping
- `logs/error.log` - Logs de errores

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor:

1. **Fork** el proyecto
2. **Crear** una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **Crear** un Pull Request

### Guías de Contribución

- Seguir PEP 8 para el estilo de código
- Escribir tests para nuevas funcionalidades
- Actualizar documentación cuando sea necesario
- Usar commits descriptivos

## 📝 Roadmap

- [ ] Integración con más sitios de empleo
- [ ] Sistema de notificaciones
- [ ] API de matching inteligente
- [ ] Dashboard web
- [ ] Integración con redes sociales
- [ ] Análisis de tendencias del mercado laboral

## 🐛 Reportar Bugs

Si encuentras un bug, por favor crea un issue con:

- Descripción detallada del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Información del entorno (OS, Python version, etc.)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Autores

- **Tu Nombre** - *Desarrollo inicial* - [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- FastAPI por el excelente framework
- SQLAlchemy por el ORM robusto
- Scrapy por las herramientas de scraping
- La comunidad de Python por las librerías increíbles

---

⭐ **¡Si este proyecto te resulta útil, no olvides darle una estrella!** ⭐
