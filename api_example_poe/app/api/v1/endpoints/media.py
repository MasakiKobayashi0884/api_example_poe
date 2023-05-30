import io
from collections.abc import Generator

from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from PIL import Image
from PIL.GifImagePlugin import GifImageFile

from api_example_poe.core.config import settings

router = APIRouter(prefix="/media")


class ImagePngResponse(Response):
    media_type = "image/png"


class ImageGifResponse(Response):
    media_type = "image/gif"


@router.get("/image_pil", response_class=ImagePngResponse)
def image_pil() -> ImagePngResponse:
    path = settings.RESOURCE / "image.png"
    img = Image.open(path)
    img.save(ostream := io.BytesIO(), format=img.format)
    return ImagePngResponse(ostream.getvalue())


def iter_gif_frame(gif: GifImageFile) -> Generator[Image.Image, None, None]:
    for i in range(gif.n_frames):
        gif.seek(i)
        yield gif.copy()


@router.get("/gif", response_class=ImageGifResponse)
def gif() -> ImageGifResponse:
    path = settings.RESOURCE / "sample.gif"
    g = Image.open(path)
    if not isinstance(g, GifImageFile):
        raise TypeError

    top, *body = iter_gif_frame(g)
    top.save(
        ostream := io.BytesIO(),
        format=g.format,
        save_all=True,
        append_images=body,
        duration=g.info["duration"],
        loop=g.info["loop"],
    )

    return ImageGifResponse(ostream.getvalue())


@router.get("/gif/{frame}", response_class=ImagePngResponse)
def gif_frame(frame: int) -> ImagePngResponse:
    path = settings.RESOURCE / "sample.gif"
    g = Image.open(path)
    if frame >= g.n_frames:
        raise HTTPException(400, f"frame is out of range. {frame} >= {g.n_frames}")
    g.seek(frame)
    g.save(ostream := io.BytesIO(), format="PNG")

    return ImagePngResponse(ostream.getvalue())
