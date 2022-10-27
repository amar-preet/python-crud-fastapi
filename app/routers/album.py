from typing import Union
from fastapi import APIRouter
from app.models.album import Album, AlbumResponseApi
from app.services import album_service as service

router = APIRouter(prefix="/albums", tags=["albums"])


@router.get("/")
async def get_albums():
    return service.get_albums()


@router.get("/{album_id}")
async def get_album_by_id(album_id: str, q: Union[str, None] = None):
    return service.get_album_by_id(album_id=album_id)


@router.post("/")
async def create_album(album: Album):
    return album


@router.delete("/")
async def delete_album(album: Album):
    return album
