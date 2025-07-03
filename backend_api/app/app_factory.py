from fastapi import FastAPI

from applications.auth.router import router_auth
from applications.users.router import router_users
from settings import settings
from applications.products.router import products_router, cart_router

import sentry_sdk

sentry_sdk.init(
    dsn="https://e9841f2531bd8b7537b6338c9643b4e9@o4509457148346368.ingest.de.sentry.io/4509478950010960",
    send_default_pii=True,
)


def get_application() -> FastAPI:
    app = FastAPI(root_path="/api", root_path_in_servers=True, debug=settings.DEBUG)
    app.include_router(router_users, prefix="/users", tags=["Users"])
    app.include_router(router_auth, prefix="/auth", tags=["Auth"])
    app.include_router(products_router, prefix="/products", tags=['Products'])
    app.include_router(cart_router, prefix="/carts", tags=["Cart"])

    return app
