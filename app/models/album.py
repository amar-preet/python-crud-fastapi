from pydantic import BaseModel, Field


class Album(BaseModel):
    title: str
    artist: str
    price: float
    year: int


class AlbumResponseApi(Album):
    id: str = Field(
        ...,
        description="Main key to identify album",
        example="1",
    )
