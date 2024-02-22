from __future__ import annotations

from typing import Optional, cast

from sqlalchemy import delete as sql_delete
from sqlalchemy import select as sql_select
from sqlalchemy import update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import VideoModel


async def get(session: AsyncSession, video_id: int) -> VideoModel | None:
    return await session.get(
        VideoModel, video_id
    )


async def create(
        session: AsyncSession,
        pack: int,
        name: str,
        link: str,


) -> VideoModel:
    new_video = VideoModel(
        pack=pack,
        link=link,
        name=name
    )
    session.add(new_video)
    await session.commit()
    return new_video

async def update(
        session: AsyncSession,
        video_id: int,
        update_context: dict,
) -> None:
    await session.execute(
        sql_update(VideoModel).where(VideoModel.video_id == video_id).values(
            update_context
        )
    )
    await session.commit()


async def delete(session: AsyncSession, video_id: int) -> None:
    await session.execute(
        sql_delete(VideoModel).where(VideoModel.video_id == video_id)
    )
    await session.commit()


async def get_all(session: AsyncSession,) -> list[VideoModel]:
    return cast(list[VideoModel], (
        await session.scalars(sql_select(VideoModel))
    ).all())


async def get_all_by_pack_id(session: AsyncSession, pack: int) -> list[VideoModel]:
        return cast(list[VideoModel], (
            await session.scalars(
                sql_select(VideoModel).where(VideoModel.pack == pack)
            )
        ).all())