from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Usuarios - GdS")


class Usuario(BaseModel):
    id: int
    nombre: str


usuarios: list[Usuario] = [
    Usuario(id=1, nombre="Ana"),
    Usuario(id=2, nombre="Bruno"),
]


@app.get("/")
def raiz():
    return {"mensaje": "API funcionando"}


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            return u
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@app.get("/saludo/{usuario_id}")
def saludo(usuario_id: int):
    u = obtener_usuario(usuario_id)
    return {"mensaje": f"Bienvenido, {u.nombre}!"}


@app.post("/usuarios", status_code=201)
def crear_usuario(usuario: Usuario):
    if any(u.id == usuario.id for u in usuarios):
        raise HTTPException(status_code=400, detail="ID duplicado")
    usuarios.append(usuario)
    return usuario


@app.get("/descuento/{precio}")
def descuento(precio: float, cliente: str = "comun"):
    if precio <= 0:
        raise HTTPException(status_code=400, detail="Precio inválido")
    porcentaje = 0
    if precio > 1000:
        porcentaje = 20
    elif precio > 500:
        porcentaje = 10
    if cliente == "vip":
        porcentaje += 5
    elif cliente == "empleado":
        porcentaje += 15
    final = precio * (100 - porcentaje) / 100
    return {"precio": precio, "descuento": porcentaje, "final": final}


@app.get("/envio/{zona}")
def costo_envio(zona: str, precio: float = 0):
    costos = {"caba": 500, "gba": 900, "interior": 1500}
    if zona not in costos:
        raise HTTPException(status_code=404, detail="Zona no encontrada")
    if precio >= 20000:
        return {"zona": zona, "envio": 0}
    return {"zona": zona, "envio": costos[zona]}

