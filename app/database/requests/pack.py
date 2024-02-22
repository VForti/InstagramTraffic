from __future__ import annotations

from typing import Optional, cast

from sqlalchemy import delete as sql_delete
from sqlalchemy import select as sql_select
from sqlalchemy import update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import PackModel


async def get(session: AsyncSession, pack_id: int) -> PackModel | None:
    return await session.get(
        PackModel, pack_id
    )


async def create(
        session: AsyncSession,
        name: str,
        role: str



) -> PackModel:
    new_pack = PackModel(
        name=name,
        role=role
    )
    session.add(new_pack)
    await session.commit()
    return new_pack

async def update(
        session: AsyncSession,
        pack_id: int,
        update_context: dict,
) -> None:
    await session.execute(
        sql_update(PackModel).where(PackModel.pack_id == pack_id).values(
            update_context
        )
    )
    await session.commit()


async def delete(session: AsyncSession, pack_id: int) -> None:
    await session.execute(
        sql_delete(PackModel).where(PackModel.pack_id == pack_id)
    )
    await session.commit()


async def get_all(session: AsyncSession,) -> list[PackModel]:
    return cast(list[PackModel], (
        await session.scalars(sql_select(PackModel))
    ).all())


async def get_all_pack_by_role(session: AsyncSession, role: str) -> list[PackModel]:
    return cast(list[PackModel], (
        await session.scalars(
            sql_select(PackModel).where(PackModel.role == role)
        )
    ).all())