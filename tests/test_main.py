from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_raiz():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"mensaje": "API funcionando"}


def test_listar_usuarios():
    r = client.get("/usuarios")
    assert r.status_code == 200
    assert len(r.json()) >= 2


def test_obtener_usuario_existente():
    r = client.get("/usuarios/1")
    assert r.status_code == 200
    assert r.json()["nombre"] == "Ana"


def test_obtener_usuario_inexistente():
    r = client.get("/usuarios/999")
    assert r.status_code == 404


def test_saludo():
    r = client.get("/saludo/1")
    assert r.status_code == 200
    assert r.json()["mensaje"] == "Bienvenido, Ana!"


def test_crear_usuario():
    r = client.post("/usuarios", json={"id": 10, "nombre": "Carla"})
    assert r.status_code == 201
    assert r.json()["nombre"] == "Carla"


def test_crear_usuario_duplicado():
    r = client.post("/usuarios", json={"id": 1, "nombre": "Repetido"})
    assert r.status_code == 400
