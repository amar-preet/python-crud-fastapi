from typing import Union
from fastapi import APIRouter
from app.models.album import Album, AlbumResponseApi
from app.services import album_service as service

router = APIRouter(prefix="/albums")


@router.get("/albums/")
async def get_albums():
    return service.get_albums()


@router.get("/albums/{album_id}")
async def get_album_by_id(album_id: str, q: Union[str, None] = None):
    return service.get_album_by_id(album_id=album_id)


@router.post("/albums/")
async def create_album(album: Album):
    return album


@router.delete("/albums/")
async def delete_album(album: Album):
    return album
