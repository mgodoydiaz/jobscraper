# Guía de Instalación y Configuración de PostgreSQL

## 📋 Estado Actual del Proyecto

### ✅ Implementado
- **Modelos de Base de Datos**: Completos con SQLAlchemy ORM
- **CRUD Operations**: Implementación completa para todas las entidades
- **Configuración de Conexión**: SQLAlchemy engine y session configurados
- **Script de Migración**: Utilidad completa para gestionar la BD
- **Dependencias**: psycopg2-binary incluido en requirements.txt

### ⚠️ Pendiente
- **PostgreSQL**: Instalación y configuración del servidor
- **Base de Datos**: Creación de la BD inicial
- **Variables de Entorno**: Configuración del archivo .env

## 🐘 Instalación de PostgreSQL

### Ubuntu/Debian
```bash
# Actualizar repositorios
sudo apt update

# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Verificar instalación
sudo systemctl status postgresql
```

### macOS (con Homebrew)
```bash
# Instalar PostgreSQL
brew install postgresql

# Iniciar servicio
brew services start postgresql
```

### Windows
1. Descargar desde: https://www.postgresql.org/download/windows/
2. Ejecutar el instalador
3. Seguir el asistente de instalación

## ⚙️ Configuración Inicial

### 1. Configurar Usuario y Base de Datos
```bash
# Cambiar a usuario postgres
sudo -u postgres psql

# Crear usuario para la aplicación
CREATE USER jobscraper_user WITH PASSWORD 'tu_password_seguro';

# Crear base de datos
CREATE DATABASE jobscraper OWNER jobscraper_user;

# Otorgar permisos
GRANT ALL PRIVILEGES ON DATABASE jobscraper TO jobscraper_user;

# Salir de psql
\q
```

### 2. Configurar Variables de Entorno
```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar archivo .env
nano .env
```

Actualizar la línea de DATABASE_URL:
```env
DATABASE_URL=postgresql://jobscraper_user:tu_password_seguro@localhost:5432/jobscraper
```

## 🚀 Inicialización del Proyecto

### 1. Instalar Dependencias
```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Verificar instalación de psycopg2
python -c "import psycopg2; print('psycopg2 instalado correctamente')"
```

### 2. Ejecutar Migraciones
```bash
# Verificar conexión a PostgreSQL
python jobscraper/scripts/migrate_db_complete.py check

# Inicializar base de datos completa (recomendado para primera vez)
python jobscraper/scripts/migrate_db_complete.py init

# O paso a paso:
# 1. Crear base de datos
python jobscraper/scripts/migrate_db_complete.py create-db

# 2. Crear tablas
python jobscraper/scripts/migrate_db_complete.py create

# 3. Insertar datos de ejemplo
python jobscraper/scripts/migrate_db_complete.py sample-data
```

### 3. Verificar Instalación
```bash
# Mostrar tablas creadas
python jobscraper/scripts/migrate_db_complete.py tables

# Verificar conexión
python jobscraper/scripts/migrate_db_complete.py check
```

## 📊 Estructura de Base de Datos

### Tablas Principales
- **users**: Usuarios del sistema con autenticación
- **companies**: Empresas que publican ofertas
- **job_offers**: Ofertas laborales scrapeadas
- **scraping_sources**: Configuración de fuentes de scraping
- **scraping_jobs**: Trabajos de scraping ejecutados
- **user_job_interactions**: Interacciones usuario-oferta
- **search_history**: Historial de búsquedas

### Características
- **Relaciones**: Foreign keys entre entidades
- **Índices**: Optimización para consultas frecuentes
- **Enums**: Estados controlados (JobStatus, ScrapingStatus, etc.)
- **JSON Fields**: Almacenamiento flexible para metadatos
- **Timestamps**: Auditoría automática de creación/actualización

## 🔧 Comandos Útiles

### Gestión de Base de Datos
```bash
# Resetear base de datos (CUIDADO: elimina todos los datos)
python jobscraper/scripts/migrate_db_complete.py reset

# Solo eliminar tablas
python jobscraper/scripts/migrate_db_complete.py drop

# Solo crear tablas
python jobscraper/scripts/migrate_db_complete.py create
```

### PostgreSQL
```bash
# Conectar a la base de datos
psql -h localhost -U jobscraper_user -d jobscraper

# Backup de base de datos
pg_dump -h localhost -U jobscraper_user jobscraper > backup.sql

# Restaurar backup
psql -h localhost -U jobscraper_user jobscraper < backup.sql
```

## 🐛 Solución de Problemas

### Error de Conexión
```bash
# Verificar que PostgreSQL esté ejecutándose
sudo systemctl status postgresql

# Reiniciar PostgreSQL
sudo systemctl restart postgresql
```

### Error de Autenticación
1. Verificar credenciales en .env
2. Confirmar que el usuario existe en PostgreSQL
3. Verificar permisos del usuario

### Error de psycopg2
```bash
# Ubuntu/Debian: instalar dependencias de desarrollo
sudo apt install libpq-dev python3-dev

# Reinstalar psycopg2
pip uninstall psycopg2-binary
pip install psycopg2-binary
```

## ✅ Verificación Final

Ejecutar estos comandos para confirmar que todo está funcionando:

```bash
# 1. Verificar PostgreSQL
psql --version

# 2. Verificar conexión Python-PostgreSQL
python -c "
from jobscraper.app.database.connection import engine
from sqlalchemy import text
with engine.connect() as conn:
    result = conn.execute(text('SELECT version()'))
    print('Conexión exitosa:', result.fetchone()[0])
"

# 3. Verificar tablas
python jobscraper/scripts/migrate_db_complete.py tables

# 4. Verificar datos de ejemplo
python -c "
from jobscraper.app.database.connection import SessionLocal
from jobscraper.app.database.crud import get_companies
db = SessionLocal()
companies = get_companies(db)
print(f'Empresas en BD: {len(companies)}')
for company in companies:
    print(f'- {company.nombre}')
db.close()
"
```

Si todos estos comandos se ejecutan sin errores, ¡la instalación está completa! 🎉