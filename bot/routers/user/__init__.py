from aiogram import Router

from . import (
    start,
    video_pack,
    video_crud
)


router = Router()

router.include_routers(
    start.router,
    video_pack.router,
    video_crud.router
)