from applications.products.models import Product


async def create_product_in_db(product_uuid, title, description, price, main_image, images, session) -> Product:
    """
        uuid_data: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4)

    title: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), index=True, default="")
    price: Mapped[float] = mapped_column(nullable=False)
    main_image: Mapped[str] = mapped_column(nullable=False)
    images: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
    """
    new_product = Product(
        uuid_data=product_uuid,
        title=title,
        description=description,
        price=price,
        main_image=main_image,
        images=images
    )
    session.add(new_product)

    await session.commit()
    return new_product