from __future__ import annotations

from typing import Optional, cast

from sqlalchemy import delete as sql_delete
from sqlalchemy import select as sql_select
from sqlalchemy import update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import AccountModel


async def get(session: AsyncSession, account_id: int) -> AccountModel | None:
    return await session.get(
        AccountModel, account_id
    )


async def create(
        session: AsyncSession,
        username: str,
        password: str,


) -> AccountModel:
    new_account = AccountModel(
        username=username,
        password=password,
    )
    session.add(new_account)
    await session.commit()
    return new_account

async def update(
        session: AsyncSession,
        account_id: int,
        update_context: dict,
) -> None:
    await session.execute(
        sql_update(AccountModel).where(AccountModel.account_id == account_id).values(
            update_context
        )
    )
    await session.commit()


async def delete(session: AsyncSession, account_id: int) -> None:
    await session.execute(
        sql_delete(AccountModel).where(AccountModel.account_id == account_id)
    )
    await session.commit()


async def get_all(session: AsyncSession,) -> list[AccountModel]:
    return cast(list[AccountModel], (
        await session.scalars(sql_select(AccountModel))
    ).all())