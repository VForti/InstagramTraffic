from typing import Optional
from datetime import datetime, timedelta

from aiogram.types import User
from sqlalchemy.ext.asyncio import AsyncSession

from .models import AccountModel, VideoModel, PackModel
from .requests import account, video, pack

class Database:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_account(self, account_id: int) -> Optional[AccountModel]:
        return await account.get(
            account_id=account_id,
            session=self.session
        )

    async def create_account(self, username: str, password: str) -> AccountModel:
        return await account.create(
            session=self.session,
            username=username,
            password=password,

        )

    async def update_account(self, account_id: int, update_context: dict) -> None:
        await account.update(
            account_id=account_id,
            update_context=update_context,
            session=self.session
        )
    async def delete_account(self, account_id: int) -> None:
        await account.delete(
            account_id=account_id,
            session=self.session
        )

    async def get_all_account(self) -> list[AccountModel]:
        return await account.get_all(
            session=self.session
        )




    async def get_video(self, video_id: int) -> Optional[VideoModel]:
        return await video.get(
            video_id=video_id,
            session=self.session
        )

    async def create_video(self, pack: int, name: str, link: str) -> VideoModel:
        return await video.create(
            session=self.session,
            pack=pack,
            name=name,
            link=link

        )

    async def update_video(self, video_id: int, update_context: dict) -> None:
        await video.update(
            video_id=video_id,
            update_context=update_context,
            session=self.session
        )
    async def delete_video(self, video_id: int) -> None:
        await video.delete(
            video_id=video_id,
            session=self.session
        )



    async def get_all_video(self) -> list[VideoModel]:
        return await video.get_all(
            session=self.session
        )

    async def get_all_by_pack_id(self, pack: int) -> list[VideoModel]:
        return await video.get_all_by_pack_id(
            pack=pack,
            session=self.session,
        )



    async def get_pack(self, pack_id: int) -> Optional[PackModel]:
        return await pack.get(
            pack_id=pack_id,
            session=self.session
        )

    async def create_pack(self, name: str, role: str) -> PackModel:
        return await pack.create(
            session=self.session,
            name=name,
            role=role
        )

    async def update_pack(self, pack_id: int, update_context: dict) -> None:
        await pack.update(
            pack_id=pack_id,
            update_context=update_context,
            session=self.session
        )
    async def delete_pack(self, pack_id: int) -> None:
        await pack.delete(
            pack_id=pack_id,
            session=self.session
        )



    async def get_all_pack(self) -> list[PackModel]:
        return await pack.get_all(
            session=self.session
        )


    async def get_all_pack_by_role(self, role: str) -> list[PackModel]:
        return await pack.get_all_pack_by_role(
            session=self.session,
            role=role
        )

    async def save(self) -> None:
        await self.session.commit()