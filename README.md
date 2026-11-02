# GdS - GitHub Actions

[![CI](https://github.com/andyargg/gds-github-actions/actions/workflows/ci.yml/badge.svg)](https://github.com/andyargg/gds-github-actions/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=andyargg_gds-github-actions&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=andyargg_gds-github-actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=andyargg_gds-github-actions&metric=coverage)](https://sonarcloud.io/summary/new_code?id=andyargg_gds-github-actions)

API mínima en FastAPI con suite de tests en pytest, usada para las Actividades 6
(GitHub Actions) y 8 (Calidad de código y DevSecOps) de Gestión de Software.

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
Después de los tests, analiza el código con SonarCloud y espera el resultado
del Quality Gate.
La rama `main` está protegida: solo se puede mergear si el check `tests` pasa
(tests + Quality Gate).

## Calidad y seguridad

- **SonarCloud**: análisis estático (bugs, vulnerabilidades, code smells,
  duplicación y cobertura). Dashboard:
  https://sonarcloud.io/project/overview?id=andyargg_gds-github-actions
- **Dependabot**: alertas de dependencias vulnerables y pull requests
  automáticos de actualización (`.github/dependabot.yml`).

## Estructura

```
.github/workflows/ci.yml   Workflow de CI (tests + SonarCloud + reporte como artifact)
.github/dependabot.yml     Configuración de Dependabot
app/main.py                API FastAPI
tests/test_main.py         Suite de tests (pytest)
requirements.txt           Dependencias
sonar-project.properties   Configuración del análisis de SonarCloud
```
