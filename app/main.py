from fastapi import FastAPI
from app.routers import album

app = FastAPI()

app.include_router(album.router)
app.router.redirect_slashes = False
