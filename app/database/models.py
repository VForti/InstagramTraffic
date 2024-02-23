from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy import String, DateTime, BigInteger, ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class AccountModel(Base):
    __tablename__ = "account"
    account_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True, index=True)
    username: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)




class PackModel(Base):
    __tablename__ = "pack"
    pack_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)


class VideoModel(Base):
    __tablename__ = "video"
    video_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True, index=True)
    pack: Mapped[int] = mapped_column(BigInteger, ForeignKey('pack.pack_id'))
    name: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)



class BayModel(Base):
    __tablename__ = "bay"
    bay_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, unique=True, index=True)
    goal: Mapped[int] = mapped_column(BigInteger)
    role: Mapped[str] = mapped_column(String)
    now_done: Mapped[int] = mapped_column(BigInteger, default=0)
    done: Mapped[bool] = mapped_column(default=False, server_default="false")




