from app.models.album import Album, AlbumResponseApi

# TODO connect to a database


def get_albums():
    return AlbumResponseApi(
        id="1",
        title="In Search of Sunrise 1",
        artist="DJ Tiesto",
        price=23.12,
        year=2001,
    )


def get_album_by_id(album_id: str):
    return AlbumResponseApi(
        id=album_id, title="Earth", artist="John OO Fleming", price=13.12, year=2010
    )
