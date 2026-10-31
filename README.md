# GdS - GitHub Actions

[![CI](https://github.com/andyargg/gds-github-actions/actions/workflows/ci.yml/badge.svg)](https://github.com/andyargg/gds-github-actions/actions/workflows/ci.yml)

API mínima en FastAPI con suite de tests en pytest, usada para la Actividad 6
(GitHub Actions) de Gestión de Software.

## Ejecutar en local

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
pytest
```

Levantar la API: `uvicorn app.main:app --reload` → http://localhost:8000/docs

## CI

El workflow `.github/workflows/ci.yml` corre los tests en cada pull request
contra `main` y publica el reporte (HTML + cobertura) como artifact.
La rama `main` está protegida: solo se puede mergear si el check `tests` pasa.

## Estructura

```
.github/workflows/ci.yml   Workflow de CI (tests + reporte como artifact)
app/main.py                API FastAPI
tests/test_main.py         Suite de tests (pytest)
requirements.txt           Dependencias
```
