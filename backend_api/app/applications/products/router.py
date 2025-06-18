from fastapi import APIRouter, Body, UploadFile

products_router = APIRouter()


@products_router.post('/')
async def create_product(
    main_image: UploadFile,
    images: list[UploadFile],
    title: str = Body(max_length=100),
    description: str = Body(max_length=1000),
    price: float = Body(gt=1),
):
    return

@products_router.get('/{pk}')
async def get_product(pk: int):
    return


@products_router.get('/')
async def get_product():
    return