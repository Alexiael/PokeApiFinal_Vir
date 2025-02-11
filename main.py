# main.py

from fastapi import FastAPI
import uvicorn

# Importamos el router principal
from app.routers.main_router import router as main_router

# Instancia de la aplicación FastAPI
app = FastAPI(
    title="Pokemon FastAPI",
    description="Ejemplo de aplicación con FastAPI",
    version="1.0.0",
)

# Incluimos el router
app.include_router(main_router)

if __name__ == "__main__":
    # Esto se utiliza principalmente en desarrollo local
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

