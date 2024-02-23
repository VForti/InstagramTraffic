from __future__ import annotations

from typing import Optional, cast

from sqlalchemy import delete as sql_delete
from sqlalchemy import select as sql_select
from sqlalchemy import update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import BayModel


async def get(session: AsyncSession, bay_id: int) -> BayModel | None:
    return await session.get(
        BayModel, bay_id
    )


async def create(
        session: AsyncSession,
        goal: int,
        now_done: int,
        done: bool,
        role: str


) -> BayModel:
    new_bay = BayModel(
        goal=goal,
        now_done=now_done,
        done=done,
        role=role
    )
    session.add(new_bay)
    await session.commit()
    return new_bay

async def update(
        session: AsyncSession,
        bay_id: int,
        update_context: dict,
) -> None:
    await session.execute(
        sql_update(BayModel).where(BayModel.bay_id == bay_id).values(
            update_context
        )
    )
    await session.commit()


async def delete(session: AsyncSession, bay_id: int) -> None:
    await session.execute(
        sql_delete(BayModel).where(BayModel.bay_id == bay_id)
    )
    await session.commit()


async def get_all(session: AsyncSession,) -> list[BayModel]:
    return cast(list[BayModel], (
        await session.scalars(sql_select(BayModel))
    ).all())


async def get_all_bay_by_role(session: AsyncSession, role: str) -> list[BayModel]:
    return cast(list[BayModel], (
        await session.scalars(
            sql_select(BayModel).where(BayModel.role == role)
        )
    ).all())


