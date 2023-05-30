from fastapi import APIRouter, Response

router = APIRouter(prefix="/customize")


@router.get(
    "/meta",
    tags=["tag1"],
    summary="summary...",
    operation_id="operationId...",
    response_description="Description Of Response",
)
def meta() -> Response:
    """
    docstring of meta

    * **bold**
    * *italic*
    * ~tilde~

    ![embed image](/media/image_pil)

    [Link to FastAPI](https://fastapi.tiangolo.com/ja/)
    """
    return Response()
